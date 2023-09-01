# -*- coding: utf-8 -*-
import sys


def builtin(name):
    """
    Provide the correct import name for builtins on Python 2 or Python 3
    """
    if sys.version_info >= (3,):
        return f'builtins.{name}'
    else:
        return f'__builtin__.{name}'
