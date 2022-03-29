# tools-mp

This Python library provides a convenient one-line multiprocessing option that can be used as follows:

```Python
from tools_mp import multiprocess

def any_function(arg):
	do something
	return result

args = [ (arg) for arg in arguments ]

data = multiprocess(
	any_function,
	args,
	return_data = True,
	verbose = True,
	workers = 8,
	)
```

If verbose=True, the progress of the calculation will be visualized via the [tqdm](https://pypi.org/project/tqdm/) library.
If workers=None (default) all available CPU cores will be used for processing.


# Installation

    pip install tools-mp