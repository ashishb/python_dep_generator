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
--------------
```
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
```

```
$ ./generate_dep.py samples

samples/module1.py
|_ os
|_ sys

samples/module2.py
|_ sys
|_ time
|_ /home/ashishb/src/python_dep_generator/samples/module1.py
```

```
$ ./generate_dep.py -s samples

samples/module1.py

samples/module2.py
|_ /home/ashishb/src/python_dep_generator/samples/module1.py

```


[![Bitdeli Badge](https://d2weczhvl823v0.cloudfront.net/ashishb/python_dep_generator/trend.png)](https://bitdeli.com/free "Bitdeli Badge")

