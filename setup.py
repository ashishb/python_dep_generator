from setuptools import setup

setup(name='python_dep_generator',
        version='0.1',
        description='Generates python code dependency graph',
        url='https://github.com/ashishb/python_dep_generator',
        author='Ashish Bhatia',
        author_email='ashishbhatia.ab@gmail.com',
        license='MIT',
        packages=['python_dep_generator'],
        # install_requires=['argparse', 'importlib', 'inspect', 'logging', 'sys'],
        entry_points = {
                'console_scripts': ['generate-dep=python_dep_generator.generate_dep:main'],
                },
        zip_safe=False)
