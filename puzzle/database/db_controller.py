import glob

from typing import Tuple, List

from puzzle.utils import *


# DEBUG
USERS_FAKE = [
    ['admin', 'admin']
]

IGNORE_ID_SET = set()
IMG_AND_ID = [
    (path, i*100+8) for i, path in enumerate(
        glob.glob("D:/University/Tech.prog/Labs/program/QtPuzzleGame/puzzle/tests/test_admin/test_images/*.png")
    )
]


class DatabaseController:

    @staticmethod
    def take_all_imgs() -> List[Tuple[str, int]]:
        """
        return list of tuples
        First element - path to img
        Second element - id of image

        """
        new_img_and_ids_list = []
        for img_s, id_s in IMG_AND_ID:
            if str(id_s) not in IGNORE_ID_SET:
                new_img_and_ids_list += [[img_s, id_s]]
        return new_img_and_ids_list

    @staticmethod
    def get_img(id_img: int) -> str:
        for path_s, id_s in IMG_AND_ID:
            if id_s == id_img:
                return path_s

    @staticmethod
    def remove_img(id_img: int):
        IGNORE_ID_SET.add(str(id_img))

    @staticmethod
    def add_image(path: str, name: str):
        pass

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
