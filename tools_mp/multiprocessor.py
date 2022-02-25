#####################################################################################################################################################
#---------------------------------------------------------------------------------------------------------------------------------------------------#
#	- This file is a part of 
#---------------------------------------------------------------------------------------------------------------------------------------------------#
#
#
#---------------------------------------------------------------------------------------------------------------------------------------------------#
#####################################################################################################################################################
#---------------------------------------------------------------------------------------------------------------------------------------------------#

#---------------------------------------------------------------------------------------------------------------------------------------------------#
#####################################################################################################################################################
#---------------------------------------------------------------------------------------------------------------------------------------------------#
# Load essential packages:
import multiprocessing as mp
import tqdm
#---------------------------------------------------------------------------------------------------------------------------------------------------#
#####################################################################################################################################################


#####################################################################################################################################################
#---------------------------------------------------------------------------------------------------------------------------------------------------#
def multiprocess(
	function,
	args,
	return_data: bool = False,
	verbose = True,
	workers: int = None,
	):
	if workers == None:
		workers = mp.cpu_count()
	pool = mp.Pool( workers )
	tasks = ( ( function, x ) for x in args)
	data = None
	if return_data:
		data = []
		if verbose:
			for x in tqdm.tqdm( pool.imap( _worker, tasks ), total=len( args ) ):
				data.append( x )
		else:
			for x in pool.imap( _worker, tasks ):
				data.append( x )
	else:
		if verbose:
			for x in tqdm.tqdm( pool.imap( _worker, tasks ), total=len( args ) ):
				pass
		else:
			pool.imap( _worker, tasks )
	pool.close()
	pool.join()
	return data
#---------------------------------------------------------------------------------------------------------------------------------------------------#
def _worker( args ):
	function, arg = args
	return function( arg )
#---------------------------------------------------------------------------------------------------------------------------------------------------#
#####################################################################################################################################################