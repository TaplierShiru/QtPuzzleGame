import os

from PIL import Image


def check_image_content(image_path: str, type_img: str = 'png') -> bool:
    """
    Return True - if image is good, otherwise False

    """
    try:
        if os.path.isfile(image_path):
            return False

        img = Image.open(image_path)
        img.verify()

        if f".{type_img}" not in image_path:
            return False # Wrong type

        return True # Good img
    except Exception:
        # Bad image
        return False # Bad image

