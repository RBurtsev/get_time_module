from setuptools import setup

setup(
    name='get_time_module',
    version='0.1',
    description='Library for work with time',
    author='RBurtsev',
    packages=['get_time_package', 'pretty_print'],
    install_requires=['requests==2.26.0'],
    entry_points={
        'console_scripts': [
            'get_time=get_time_package.get_time_module:main',
            'get_time_pretty=pretty_print.pretty_print_module:main'
        ]
    }
)