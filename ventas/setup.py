from setuptools import setup

setup(
    name = 'dv',
    version = '0.1',
    py_modules = ['dv'],
    install_requires = ['Click', ],
    entry_points = '''[console_scripts]
    dv = dv:cli
    '''

)