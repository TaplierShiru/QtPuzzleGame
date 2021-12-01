import numpy as np
from PIL import Image, ImageQt, ImageDraw

from typing import List, Tuple
from PySide6.QtGui import QImage


def cut_image_into_triangles(
        source_img: np.ndarray, size_block_w: int, size_block_h: int,
        thick_of_border_line: int = 1, map_to_qimage=True) -> Tuple[List[QImage], List[QImage], QImage]:
    """
    Cut input image into triangles

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

    Return
    ------
    list
        List of top qimage elements of original image
    list
        List of bottom qimage element of original image
    np.ndarray
        Mask in order to classify bottom and top place

    """
    size = source_img.shape
    step_w = int(size[1] // size_block_w)
    step_h = int(size[0] // size_block_h)
    triangles_top_list = []
    triangles_bottom_list = []

    # Cut peases on top and bot
    polygon = [(0, 0), (step_w, step_h), (0, step_h), (0, 0)]
    img = Image.new('L', (step_w, step_h), 0)
    ImageDraw.Draw(img).polygon(polygon, outline=1, fill=1)
    mask = np.array(img)

    for i in range(size_block_h):
        for j in range(size_block_w):
            peases = (source_img[i * step_h: (i + 1) * step_h,
                                 j * step_w: (j + 1) * step_w]
            ).astype(np.uint8)

            peases[:thick_of_border_line, :, 1] = 255  # Top line
            peases[:, :thick_of_border_line, 1] = 255  # Left line
            peases[-thick_of_border_line:, :, 1] = 255  # Bottom line
            peases[:, -thick_of_border_line:, 1] = 255  # Right line
            pil_peases = Image.fromarray(peases.astype(np.uint8))
            draw = ImageDraw.Draw(pil_peases)
            draw.line(
                (0, 0, peases.shape[1], peases.shape[0]),
                fill=(0, 255, 0, 0), width=thick_of_border_line
            )
            peases = np.array(pil_peases)
            # Top pease
            arr_top = np.zeros((peases.shape[0], peases.shape[1], 4), dtype=np.uint8)
            arr_top[..., :-1] = peases.copy()
            arr_top[..., -1] += (1.0 - mask).astype(np.uint8) * 255
            # Bot pease
            arr_bot = np.zeros((peases.shape[0], peases.shape[1], 4), dtype=np.uint8)
            arr_bot[..., :-1] = peases.copy()
            arr_bot[..., -1] += mask.astype(np.uint8) * 255

            if map_to_qimage:
                image_top = ImageQt.ImageQt(Image.fromarray(arr_top))
                image_bot = ImageQt.ImageQt(Image.fromarray(arr_bot))
            else:
                image_top = arr_top
                image_bot = arr_bot
            triangles_top_list.append(image_top)
            triangles_bottom_list.append(image_bot)

    return triangles_top_list, triangles_bottom_list, mask

