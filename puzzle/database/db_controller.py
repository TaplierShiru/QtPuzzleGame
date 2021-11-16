import glob

from typing import Tuple, List

from puzzle.admin.constants import *

# DEBUG
USERS_FAKE = [
    ['admin', 'admin']
]


class DatabaseController:

    @staticmethod
    def take_all_imgs() -> List[Tuple[str, int]]:
        """
        return list of tuples
        First element - path to img
        Second element - id of image

        """
        return [
            (path, i*100+8) for i, path in enumerate(
                glob.glob("D:/University/Tech.prog/Labs/program/QtPuzzleGame/puzzle/tests/test_admin/test_images/*.png")
            )
        ]

    @staticmethod
    def get_img(id_img: int) -> str:
        return glob.glob("D:/University/Tech.prog/Labs/program/QtPuzzleGame/puzzle/tests/test_admin/test_images/*.png")[0]

    @staticmethod
    def remove_img(id_img: int):
        pass

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
