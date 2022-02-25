#!/usr/bin/env python



import sys
import logging
#import subprocess
#import shutil

from setuptools import setup, find_packages
#from setuptools.command.build_py import build_py
#from setuptools.extension import Extension

#import numpy as np
#from Cython.Build import cythonize
#import cmake



# Set up the logging environment
logging.basicConfig()
log = logging.getLogger()

# Handle the -W all flag
if 'all' in sys.warnoptions:
    log.level = logging.DEBUG

# Get version from the module
with open('tools_mp/__init__.py') as f:
    for line in f:
        if line.find('__version__') >= 0:
            version = line.split('=')[1].strip()
            version = version.strip('"')
            version = version.strip("'")
            continue




# Dependencies
DEPENDENCIES = [
    'tqdm>=4.62.1',
]


CLASSIFIERS = """
Development Status :: 3 - Alpha
Intended Audience :: Science/Research
Intended Audience :: Developers
License :: OSI Approved :: MIT License
Programming Language :: Python
Programming Language :: Python :: 3
Programming Language :: Python :: 3.8
Programming Language :: Python :: 3.9
Topic :: Software Development
Topic :: Scientific/Engineering
Typing :: Typed
Operating System :: Microsoft :: Windows
Operating System :: POSIX
Operating System :: Unix
"""



setup_args = dict(
    name='tools-mp',
    version=version,
    description='Convenient multiprocessing function for Python',
    #long_description= DOCLINES,
    url='https://github.com/paul-krug/tools-mp',
    #download_url=,
    author='Paul Krug',
    author_email='paul_konstantin.krug@tu-dresden.de',
    license='MIT',
    classifiers = [_f for _f in CLASSIFIERS.split('\n') if _f],
    keywords=[ 'multiprocessing', 'Python' ],
    #ext_modules=EXT_MODULES,
    #cmdclass = cmdclass,
    #include_dirs=np.get_include(),
    packages=find_packages(),
    package_dir={'tools-mp': 'tools_mp'},
    #include_package_data = True,
    install_requires=DEPENDENCIES,
    #use_scm_version=True,
    #setup_requires=['setuptools_scm'],
    zip_safe= True,
)






setup(**setup_args)