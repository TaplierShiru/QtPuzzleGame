from typing import Tuple

import numpy as np


def shuffle_peases(size_of_peases: int) -> np.ndarray:
    """
    Return shuffled indexes

    """
    arr = np.arange(size_of_peases)
    np.random.shuffle(arr)
    return arr


def shuffle_rectangle_peases(rectangle_list: list) -> Tuple[list, np.ndarray]:
    size_of_peases = len(rectangle_list)
    indx_shuffled = shuffle_peases(size_of_peases)
    return np.asarray(rectangle_list)[indx_shuffled].tolist(), indx_shuffled


def shuffle_triangle_peases(
        triangle_top_list: list,
        triangle_bottom_list: list) -> Tuple[Tuple[list, np.ndarray], Tuple[list, np.ndarray]]:
    assert len(triangle_bottom_list) == len(triangle_top_list)
    size_of_peases = len(triangle_top_list)
    indx_top_shuffled = shuffle_peases(size_of_peases)
    indx_bottom_shuffled = shuffle_peases(size_of_peases)
    shuffled_triangle_top_list = np.asarray(triangle_top_list)[indx_top_shuffled].tolist()
    shuffled_triangle_bottom_list = np.asarray(triangle_bottom_list)[indx_bottom_shuffled].tolist()
    return (shuffled_triangle_top_list, indx_top_shuffled), (shuffled_triangle_bottom_list, indx_bottom_shuffled)
