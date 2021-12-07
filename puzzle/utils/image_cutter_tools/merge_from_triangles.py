import numpy as np


def merge_from_triangles(triangle_top_list: list, triangle_bottom_list: list, mask: np.ndarray,
                         size_block_w: int, size_block_h: int) -> np.ndarray:
    assert len(triangle_top_list) != 0 and len(triangle_bottom_list) == len(triangle_top_list)
    h, w, c = np.asarray(triangle_top_list[0]).shape
    source_image = np.zeros((h * size_block_h, w * size_block_w, c), dtype=np.uint8)
    step_w = int(source_image.shape[1] // size_block_w)
    step_h = int(source_image.shape[0] // size_block_h)
    counter = 0

    for i in range(size_block_h):
        for j in range(size_block_w):
            single_top_pease = np.array(triangle_top_list[counter])
            single_bottom_pease = np.array(triangle_bottom_list[counter])
            origin_img = single_top_pease.copy()
            origin_img = origin_img * (1.0 - np.expand_dims(mask, axis=-1)) + single_bottom_pease * np.expand_dims(mask, axis=-1)

            source_image[i * step_h: (i + 1) * step_h,
                         j * step_w: (j + 1) * step_w] = origin_img.astype(np.uint8, copy=False)

            counter += 1

    return source_image
