import numpy as np


def merge_from_rectangles(rectangles_list: list, size_block_w: int, size_block_h: int) -> np.ndarray:
    assert len(rectangles_list) != 0
    h, w, c = np.asarray(rectangles_list[0]).shape
    source_image = np.zeros((h * size_block_h, w * size_block_w, c), dtype=np.uint8)
    step_w = int(source_image.shape[1] // size_block_w)
    step_h = int(source_image.shape[0] // size_block_h)
    counter = 0

    for i in range(size_block_h):
        for j in range(size_block_w):
            single_pease = rectangles_list[counter]

            source_image[i * step_h: (i + 1) * step_h,
                         j * step_w: (j + 1) * step_w] = np.array(single_pease, dtype=np.uint8)

            counter += 1

    return source_image
