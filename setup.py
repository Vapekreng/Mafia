# coding: utf-8

from cx_Freeze import setup, Executable

executables = [Executable('start.py')]


zip_include_packages = ['collections', 'encodings', 'importlib']

options = {
    'build_exe': {
        'excludes': ['unicodedata', 'logging', 'unittest', 'email', 'html', 'http', 'urllib', 'xml', 'pydoc', 'doctest',
                     'argparse', 'datetime', 'zipfile', 'subprocess', 'pickle', 'threading', 'locale', 'calendar',
                     'functools', 'weakref', 'tokenize', 'base64', 'gettext', 'heapq', 're', 'operator', 'bz2',
                     'fnmatch', 'getopt', 'reprlib', 'string', 'stringprep', 'contextlib', 'quopri', 'copy', 'imp',
                     'keyword', 'linecache']
    }
}

setup(name='Mafia',
      version='1.0.1',
      description='Mafia game master intarface',
      executables=executables,
      options = options,
      requires=['bearlibterminal'])