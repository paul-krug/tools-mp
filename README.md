# tools-mp

This Python library provides a convenient one-line multiprocessing option that can be used as follows:

```Python
from tools_mp import multiprocess
from tools_mp import process

def any_function( arg_1, arg_2, ..., arg_n ):
    do something
    return result

args = [ 
    {
        'arg_1': arg_1,
        'arg_2': arg_2,
        ...
        'arg_n': arg_n,
        } for arg_1, arg_2, ..., arg_n in arguments
    ]

data = multiprocess(
    function = any_function,
    args = args,
    return_data = True,
    verbose = True,
    workers = 8,
    **kwargs,
    )

data = process(
    function = any_function,
    args = args,
    return_data = True,
    verbose = True,
    workers = 8,
    mp_threshold = 4, # <- if the number of tasks is less than this value,
	# the process function will use single core processing, otherwise it
	# will use multiprocessing. This can speed up the processing of small
	# tasks significantly, as the overhead of multiprocessing is avoided.
    **kwargs,
    )


```

If verbose=True, the progress of the calculation will be visualized via the [tqdm](https://pypi.org/project/tqdm/) library.
If workers=None (default) all available CPU cores will be used for processing.
**kwargs will be passed to 'multiprocessing.Pool' as keyword arguments. This is important if you would like to initialize the workers with a specific function or variables for example.



# Installation

    pip install tools-mp