import os

from skimage import io, transform
import pathlib
import glob
import json
import random

from typing import Tuple, List
from puzzle.utils import *

from puzzle.utils import FRAME_H, FRAME_W, DIFFIC_LIST


BETWEEN_NUMS = ','
SEP_TOP_AND_BOTTOM = "|"
SEP_NUMS = ":"
TOP_NUMS = f"top{SEP_NUMS}"
BOTTOM_NUMS = f"bottom{SEP_NUMS}"


# DEBUG
USERS_FAKE = [
    ['admin', 'admin']
]

FOLDER_PATH = pathlib.Path(__file__).parent.resolve()
PATH_TEMP_DATA = f"{FOLDER_PATH}/temp"

with open(f"{FOLDER_PATH}/test/saved_imgs.json") as fp:
    ID_TO_IMG_PATH_DICT = json.load(fp)

DIFF2PARAMS = {
    DIFFIC_LIST[0]: (NUM_FRAGMENTS[0], NUM_FRAGMENTS[0], TYPE_BUILD_PUZZLE[0], TYPE_PUZZLES[1]),
    DIFFIC_LIST[1]: (NUM_FRAGMENTS[4], NUM_FRAGMENTS[4], TYPE_BUILD_PUZZLE[0], TYPE_PUZZLES[0]),
    DIFFIC_LIST[2]: (NUM_FRAGMENTS[6], NUM_FRAGMENTS[6], TYPE_BUILD_PUZZLE[0], TYPE_PUZZLES[1]),
}

with open(f'{FOLDER_PATH}/test/saved_games.json') as fp:
    ID_GAME_TO_PARAMS = json.load(fp)


class DatabaseController:

    @staticmethod
    def take_all_imgs() -> List[Tuple[str, str]]:
        """
        return list of tuples
        First element - path to img
        Second element - id of image

        """
        new_img_and_ids_list = []
        for id_s, img_s in ID_TO_IMG_PATH_DICT.items():
            new_img_and_ids_list += [[img_s, id_s]]
        return new_img_and_ids_list

    @staticmethod
    def get_img(id_img: str) -> str:
        return ID_TO_IMG_PATH_DICT.get(str(id_img)) # return path

    @staticmethod
    def get_img_name(id_img: str) -> str:
        img_data = ID_TO_IMG_PATH_DICT.get(str(id_img))
        if img_data is None:
            return
        img_name = img_data.split('/')[-1].split('.')[0]
        return img_name

    @staticmethod
    def remove_img(id_img: str):
        if ID_TO_IMG_PATH_DICT.get(str(id_img)) is not None:
            del ID_TO_IMG_PATH_DICT[str(id_img)]

    @staticmethod
    def add_image(path: str, name: str):
        all_ids = set(ID_TO_IMG_PATH_DICT.keys())
        id_img = random.randint(0, 1_000_000)
        while id_img in all_ids:
            id_img = random.randint(0, 1_000_000)
        img = io.imread(path)
        img_resized = transform.resize(img, (FRAME_H, FRAME_W))
        path_new_save = os.path.join(PATH_TEMP_DATA, name + f'_id_{id_img}.png')
        io.imsave(
            path_new_save,
            img_resized
        )
        ID_TO_IMG_PATH_DICT[str(id_img)] = path_new_save
        # Update json
        with open(f"{FOLDER_PATH}/test/saved_imgs.json", 'w') as fp:
            json.dump(ID_TO_IMG_PATH_DICT, fp)

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
    def add_new_game(id_img: str, indx_position: list, type_puzzle: str, diff: str):
        global ID_GAME_TO_PARAMS
        # As bd
        # -----
        id_save = random.randint(0, 1_000_000)
        all_ids_set = set(ID_GAME_TO_PARAMS.keys())
        while id_save in all_ids_set:
            id_save = random.randint(0, 1_000_000)
        config_path = f"{PATH_TEMP_DATA}/{id_save}.sage"
        game_dict = {
            f"{id_save}": {
                "diff": diff,
                "type_puzzle": type_puzzle,
                'id_img': id_img,
                'config_path': config_path
            }
        }
        ID_GAME_TO_PARAMS.update(game_dict)
        with open(f"{FOLDER_PATH}/test/saved_games.json", 'w') as fp:
            json.dump(ID_GAME_TO_PARAMS, fp)
        # -----

        if type_puzzle == TRIANGLE_PUZZLES:
            data_top_str = TOP_NUMS
            data_bottom_str = BOTTOM_NUMS
            top_indx_position, bottom_indx_position = indx_position
            data_top_str += BETWEEN_NUMS.join(map(str, top_indx_position))
            data_bottom_str += BETWEEN_NUMS.join(map(str, bottom_indx_position))
            all_data = data_top_str + SEP_TOP_AND_BOTTOM + data_bottom_str
        elif type_puzzle == RECTANGLE_PUZZLES:
            all_data = BETWEEN_NUMS.join(map(str, indx_position))
        else:
            raise ValueError()

        with open(config_path, 'w+') as fp:
            fp.write(all_data)

    @staticmethod
    def get_game_imgs(diff: str) -> list:
        found_imgs_list = []
        for elem in ID_GAME_TO_PARAMS.values():
            if elem['diff'] == diff:
                found_imgs_list.append(elem['id_img'])

        return found_imgs_list

    @staticmethod
    def get_game_config(diff: str, id_img: str) -> str:
        for elem in ID_GAME_TO_PARAMS.values():
            if elem['diff'] == diff and elem['id_img'] == id_img:
                return elem['config_path']

        return None

    @staticmethod
    def parse_rectangle_config(game_config: str) -> list:
        # Read stored file
        with open(game_config, 'r') as fp:
            data = fp.readline()
        # Parse it
        return list(map(int, data.split(",")))

    @staticmethod
    def parse_triangle_config(game_config: str) -> Tuple[List[int], List[int]]:
        # Read stored file
        with open(game_config, 'r') as fp:
            data = fp.readline()
        # Cut into top and bottom
        top_str, bottom_str = data.split(SEP_TOP_AND_BOTTOM)
        top_str = top_str.split(SEP_NUMS)[-1]
        bottom_str = bottom_str.split(SEP_NUMS)[-1]

        top_pos_list = list(map(int, top_str.split(',')))
        bottom_pos_list = list(map(int, bottom_str.split(',')))

        return top_pos_list, bottom_pos_list

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
        return DIFF2PARAMS[diff]
