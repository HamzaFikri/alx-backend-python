#!/usr/bin/env python3
""" Module for the function safely_get_value """

from typing import Mapping, Any, TypeVar, Union

T = TypeVar("T")


def safely_get_value(dct, key, default = None):
    ''' Return dct[key] if it exists, otherwise return `default`. '''
    if key in dct:
        return dct[key]
    else:
        return default