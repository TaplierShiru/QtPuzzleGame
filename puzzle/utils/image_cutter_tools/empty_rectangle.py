import numpy as np
from PIL import Image, ImageQt

from typing import Union
from PySide6.QtGui import QImage


def get_empty_rectangle(
        size_w: int, size_h: int,
        thick_of_border_line: int = 1, map_to_qimage=True) -> Union[QImage, np.ndarray]:
    """
    Cut input image into rectangles

    Parameters
    ----------
    size_w : int
        Width
    size_h : int
        Height
    thick_of_border_line : int
        Width of border lines
    map_to_qimage : bool
        If true, peases will be mapped to QImage

    Return
    ------
    QImage
        QImage with lines, if map_to_qimage is true
    np.ndarray
        Array with lines, if map_to_qimage is false

    """
    empty_pease = np.zeros((size_h, size_w, 4), dtype=np.uint8)
    empty_pease[:thick_of_border_line, :, 1] = 255  # Top line
    empty_pease[:, :thick_of_border_line, 1] = 255  # Left line
    empty_pease[-thick_of_border_line:, :, 1] = 255  # Bottom line
    empty_pease[:, -thick_of_border_line:, 1] = 255  # Right line

    empty_pease[..., -1] = ((empty_pease[..., 1] == 255) * 255)

    if map_to_qimage:
        qimage = ImageQt.ImageQt(Image.fromarray(empty_pease))
        return qimage
    return empty_pease

