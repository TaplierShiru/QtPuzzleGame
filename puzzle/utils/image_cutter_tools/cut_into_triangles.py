import numpy as np
from PIL import Image, ImageQt, ImageDraw

from typing import List, Tuple
from PySide6.QtGui import QImage


def cut_image_into_triangles(
        source_img: np.ndarray, size_block_w: int, size_block_h: int,
        thick_of_border_line: int = 1,
        map_to_qimage=True) -> Tuple[List[Tuple[QImage, QImage]], List[Tuple[QImage, QImage]], QImage]:
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
        List of tuples - top qimage and qimage wo borders
    list
        List of tuples - bottom qimage and qimage wo border
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
            h, w, c = peases.shape
            peases_lines = np.zeros((h, w))
            peases_lines[:thick_of_border_line, :] = 255  # Top line
            peases_lines[:, :thick_of_border_line] = 255  # Left line
            peases_lines[-thick_of_border_line:, :] = 255  # Bottom line
            peases_lines[:, -thick_of_border_line:] = 255  # Right line
            pil_peases = Image.fromarray(peases_lines.astype(np.uint8))
            draw = ImageDraw.Draw(pil_peases)
            draw.line(
                (0, 0, w, h),
                fill=(255), width=thick_of_border_line
            )
            peases_lines = np.array(pil_peases)
            window_lines = peases_lines == 255
            # Top pease
            arr_top = np.zeros((peases.shape[0], peases.shape[1], 4), dtype=np.uint8)
            arr_top[..., :3] = peases.copy()[..., :3] # Skip alpha channel
            arr_top[..., -1] += (1.0 - mask).astype(np.uint8) * 255
            arr_top *= np.expand_dims((1.0 - mask).astype(np.uint8), axis=-1)
            arr_top[..., :-1] *= (1 - np.expand_dims(window_lines, axis=-1)).astype(np.uint8)
            arr_top[..., 1] = (
                    (1 - window_lines) * arr_top[..., 1] +\
                    255 * window_lines
            ).astype(np.uint8)
            arr_top[window_lines, -1] = 255
            arr_top = np.clip(arr_top, 0, 255)
            # Bot pease
            arr_bot = np.zeros((peases.shape[0], peases.shape[1], 4), dtype=np.uint8)
            arr_bot[..., :3] = peases.copy()[..., :3] # Skip alpha channel
            arr_bot[..., -1] += mask.astype(np.uint8) * 255
            arr_bot *= np.expand_dims(mask.astype(np.uint8), axis=-1)
            arr_bot[..., :-1] *= (1 - np.expand_dims(window_lines, axis=-1)).astype(np.uint8)
            arr_bot[..., 1] = (
                    (1 - window_lines) * arr_bot[..., 1] +\
                    255 * window_lines
            ).astype(np.uint8)
            arr_bot[window_lines, -1] = 255
            arr_bot = np.clip(arr_bot, 0, 255)

            if map_to_qimage:
                image_top = QImage(ImageQt.ImageQt(Image.fromarray(arr_top)))
                image_bot = QImage(ImageQt.ImageQt(Image.fromarray(arr_bot)))
            else:
                image_top = arr_top
                image_bot = arr_bot
            triangles_top_list.append(image_top)
            triangles_bottom_list.append(image_bot)

    return triangles_top_list, triangles_bottom_list, mask

