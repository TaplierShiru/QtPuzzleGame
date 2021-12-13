import numpy as np
from PIL import Image, ImageQt, ImageDraw

from typing import List, Tuple, Union
from PySide6.QtGui import QImage


def get_empty_triangle(
        size_w: int, size_h: int,
        thick_of_border_line: int = 1, map_to_qimage=True) -> Union[np.ndarray, QImage]:
    """
    Cut input image into triangles

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
    # Cut peases on top and bot
    polygon = [(0, 0), (size_w, size_h), (0, size_h), (0, 0)]
    img = Image.new('L', (size_w, size_h), 0)
    ImageDraw.Draw(img).polygon(polygon, outline=1, fill=1)
    mask = np.array(img)

    empty_pease = np.zeros((size_h, size_w, 4), dtype=np.uint8)
    empty_pease[:thick_of_border_line, :, 1] = 255  # Top line
    empty_pease[:, :thick_of_border_line, 1] = 255  # Left line
    empty_pease[-thick_of_border_line:, :, 1] = 255  # Bottom line
    empty_pease[:, -thick_of_border_line:, 1] = 255  # Right line
    pil_peases = Image.fromarray(empty_pease)
    draw = ImageDraw.Draw(pil_peases)
    draw.line(
        (0, 0, empty_pease.shape[1], empty_pease.shape[0]),
        fill=(0, 255, 0, 0), width=thick_of_border_line
    )
    empty_pease = np.array(pil_peases)

    empty_pease[..., -1] = ((empty_pease[..., 1] == 255) * 255)

    if map_to_qimage:
        qimage = ImageQt.ImageQt(Image.fromarray(empty_pease))
        return qimage
    return empty_pease

