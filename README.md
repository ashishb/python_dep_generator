python_dep_generator
====================

Generates python code dependency graph

usage: generate_dep.py [-h] [-s] path

positional arguments:

  path              path (or dir) of the python file (or all python files
                    under it).

optional arguments:
  
  -h, --help        show this help message and exit
  
  -s, --small_list  Pass -s to hide system packages and get a smaller list.


Sample outputs
====================
$./generate_dep.py generate_dep.py
generate_dep.py
|_ argparse
|_ importlib
|_ inspect
|_ logging
|_ os
|_ sys
|_ traceback
|_ types

