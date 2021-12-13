import numpy as np
from PIL import ImageQt, Image
from PySide6.QtGui import QPixmap


def get_triangle_img_wo_border(
        mask: np.ndarray, qpixmap: QPixmap,
        value_zero_zone=0, channels_count=4) -> QPixmap:
    image = qpixmap.toImage()
    b = image.bits()
    arr = np.frombuffer(b, np.uint8).reshape(mask.shape[0], mask.shape[1], channels_count)
    arr *= np.expand_dims((mask == value_zero_zone), axis=-1)
    arr = np.stack([arr[..., 2], arr[..., 1], arr[..., 0], arr[..., -1]], axis=-1)
    return QPixmap(ImageQt.ImageQt(Image.fromarray(arr)))
