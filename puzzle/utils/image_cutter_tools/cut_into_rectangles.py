import numpy as np
from PIL import Image, ImageQt

from typing import List
from PySide6.QtGui import QImage


def cut_image_into_rectangles(
        source_img: np.ndarray, size_block_w: int, size_block_h: int,
        thick_of_border_line: int = 5) -> List[QImage]:
    """
    Cut input image into rectangles

    Parameters
    ----------
    source_img : np.ndarray
        Image to cut
    size_block_w : int
        Number of block per Width
    size_block_h : int
        Number of block per Height
    thick_of_border_line : int
        Width of border lines

    Return
    ------
    list
        Each element - qimage

    """
    size = source_img.shape
    step_w = int(size[1] // size_block_w)
    step_h = int(size[0] // size_block_h)
    rectangles_list = []
    for i in range(size_block_h):
        for j in range(size_block_w):
            peases = (source_img[i * step_h: (i + 1) * step_h,
                                 j * step_w: (j + 1) * step_w]
            ).astype(np.uint8)
            peases[:thick_of_border_line, :, 1] = 255  # Top line
            peases[:, :thick_of_border_line, 1] = 255  # Left line
            peases[-thick_of_border_line:, :, 1] = 255  # Bottom line
            peases[:, -thick_of_border_line:, 1] = 255  # Right line

            qimage = ImageQt.ImageQt(Image.fromarray(peases))
            rectangles_list.append(qimage)

    return rectangles_list

