import numpy as np
from PIL import Image, ImageQt

from typing import List, Tuple
from PySide6.QtGui import QImage
from skimage import transform


def cut_image_into_rectangles(
        source_img: np.ndarray, size_block_w: int, size_block_h: int,
        thick_of_border_line: int = 1, map_to_qimage=True, resize_to: Tuple[int, int] = None) -> List[QImage]:
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
    map_to_qimage : bool
        If true, peases will be mapped to QImage
    resize_to : tuple
        Tuple of (H, W) - final img size by using resize

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

            if resize_to is not None:
                peases = (transform.resize(
                    peases, (resize_to[0], resize_to[1]),
                    anti_aliasing=True
                ) * 255).astype(np.uint8)

            peases[:thick_of_border_line, :, 1] = 255  # Top line
            peases[:, :thick_of_border_line, 1] = 255  # Left line
            peases[-thick_of_border_line:, :, 1] = 255  # Bottom line
            peases[:, -thick_of_border_line:, 1] = 255  # Right line
            if map_to_qimage:
                qimage = ImageQt.ImageQt(Image.fromarray(peases))
                rectangles_list.append(qimage)
            else:
                rectangles_list.append(peases)

    return rectangles_list

