import os

from skimage import io, transform
import pathlib
import glob

from typing import Tuple, List
from puzzle.utils import *

from puzzle.utils import FRAME_H, FRAME_W


# DEBUG
USERS_FAKE = [
    ['admin', 'admin']
]

FOLDER_PATH = pathlib.Path(__file__).parent.resolve()
PATH_TEMP_DATA = f"{FOLDER_PATH}/temp"

IGNORE_ID_SET = set()
IMG_AND_ID_DICT = dict([
    (str(i*100+8), [path, path.split('/')[-1].split("\\")[-1]]) for i, path in enumerate(
        glob.glob(f"{PATH_TEMP_DATA}/*.png")
    )
])

COUNTER_ADD = 0


class DatabaseController:

    @staticmethod
    def take_all_imgs() -> List[Tuple[str, str]]:
        """
        return list of tuples
        First element - path to img
        Second element - id of image

        """
        new_img_and_ids_list = []
        for id_s, (img_s, _) in IMG_AND_ID_DICT.items():
            if id_s not in IGNORE_ID_SET:
                new_img_and_ids_list += [[img_s, id_s]]
        return new_img_and_ids_list

    @staticmethod
    def get_img(id_img: str) -> str:
        return IMG_AND_ID_DICT.get(str(id_img))[0] # return path

    @staticmethod
    def get_img_name(id_img: str) -> str:
        img_data = IMG_AND_ID_DICT.get(str(id_img))
        if img_data is None:
            return
        return img_data[-1]

    @staticmethod
    def remove_img(id_img: str):
        if IMG_AND_ID_DICT.get(str(id_img)) is not None:
            del IMG_AND_ID_DICT[str(id_img)]

    @staticmethod
    def add_image(path: str, name: str):
        global COUNTER_ADD
        id_img = str(100000 + COUNTER_ADD)
        img = io.imread(path)
        img_resized = transform.resize(img, (FRAME_H, FRAME_W))
        path_new_save = os.path.join(PATH_TEMP_DATA, name + f'_id_{id_img}.png')
        io.imsave(
            path_new_save,
            img_resized
        )
        IMG_AND_ID_DICT[str(id_img)] = [path_new_save, name]
        COUNTER_ADD += 1

    @staticmethod
    def add_user(login: str, password: str):
        if not DatabaseController.find_user(login, password):
            USERS_FAKE.append([login, password])

    @staticmethod
    def find_user(login: str, password: str) -> bool:
        for log, pas in USERS_FAKE:
            if log == login and password == pas:
                return True

        return False

    @staticmethod
    def update_diff(diff: str, frag_h: int, frag_v: int, type_build: str, type_puzzle: str):
        pass

    @staticmethod
    def get_diff_params(diff: str) -> Tuple[int, int, str, str]:
        """

        Parameters
        ----------
        diff : str
            pass

        Returns
        -------
        int
            frag_h
        int
            frag_v
        str
            type_build
        str
            type_puzzle

        """
        return NUM_FRAGMENTS[0], NUM_FRAGMENTS[0], TYPE_BUILD_PUZZLE[0], TYPE_PUZZLES[0]
