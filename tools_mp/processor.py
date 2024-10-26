

import multiprocessing
import tqdm


def _worker( args ):
    function, arg = args
    return function( **arg )

def multiprocess(
    function,
    args,
    return_data: bool = False,
    verbose = True,
    workers: int = None,
    **kwargs,
    ):
    if workers == None:
        workers = multiprocessing.cpu_count()

    # Set up the pool with workers and kwargs
    with multiprocessing.Pool(
        workers,
        **kwargs,
    ) as pool:
        tasks = ((function, x) for x in args)
        if return_data:
            data = []
            if verbose :
                for x in tqdm.tqdm(pool.imap(_worker, tasks), total=len(args)):
                    data.append(x)
            else:
                for x in pool.imap(_worker, tasks):
                    data.append(x)
        else:
            data = None
            if verbose:
                for x in tqdm.tqdm(pool.imap(_worker, tasks), total=len(args)):
                    pass
            else:
                pool.imap(_worker, tasks)
    return data

def process(
        function,
        args,
        return_data: bool = False,
        verbose = True,
        workers: int = None,
        mp_threshold: int = 4,
        **kwargs,
        ):
    if len( args ) < mp_threshold:
        return single_process(
            function = function,
            args = args,
            return_data = return_data,
            verbose = verbose,
            )
    else:
        return multiprocess(
            function = function,
            args = args,
            return_data = return_data,
            verbose = verbose,
            workers = workers,
            **kwargs,
            )

def single_process(
        function,
        args,
        return_data: bool = False,
        verbose = True,
        ):
    y = tqdm.tqdm( args ) if verbose else args
    if return_data:
        data = [ function( **x ) for x in y ]
    else:
        [ function( **x ) for x in y ]
        data = None
    return data