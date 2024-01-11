#!/usr/bin/env python3
"""
This module provides a function for zooming in an array.
"""

from typing import Tuple

def zoom_array(lst: Tuple[int], factor: int = 2) -> Tuple[int]:
    """
    Zooms in the given array by repeating each element based on the specified factor.

    Args:
        lst (Tuple[int]): The input array.
        factor (int): The factor by which each element should be repeated. Default is 2.

    Returns:
        Tuple[int]: The zoomed-in array.

    Examples:
        >>> zoom_array((1, 2, 3))
        (1, 1, 2, 2, 3, 3)
    """
    zoomed_in: Tuple[int] = tuple(
        item for item in lst
        for i in range(factor)
    )
    return zoomed_in

# Example usage
array = (12, 72, 91)
zoom_2x = zoom_array(array)
zoom_3x = zoom_array(array, 3)
