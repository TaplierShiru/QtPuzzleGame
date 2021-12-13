from PIL import Image


def save_img_in_temp(path: str, size_w: int, size_h: int, path_save_to: str) -> bool:
    try:
        img: Image.Image = Image.open(path)
        img = img.resize((size_w, size_h))
        img.save(path_save_to)
    except Exception:
        return False

    return True

