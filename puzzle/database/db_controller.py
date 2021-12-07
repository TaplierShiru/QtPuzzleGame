import copy
import os

from skimage import io, transform
import pathlib
import glob
import json
import random

from typing import Tuple, List
from puzzle.utils import *


NEW_LINE = '\n'
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
PATH_GAMES_DATA = f"{PATH_TEMP_DATA}/games"
PATH_SAVED_GAMES_DATA = f'{PATH_TEMP_DATA}/saved_games'

with open(f"{FOLDER_PATH}/test/saved_imgs.json") as fp:
    ID_TO_IMG_PATH_DICT = json.load(fp)

DIFF2PARAMS = {
    DIFFIC_LIST[0]: (NUM_FRAGMENTS[0], NUM_FRAGMENTS[0], TYPE_BUILD_PUZZLE[0], TYPE_PUZZLES[0]),
    DIFFIC_LIST[1]: (NUM_FRAGMENTS[1], NUM_FRAGMENTS[2], TYPE_BUILD_PUZZLE[1], TYPE_PUZZLES[1]),
    DIFFIC_LIST[2]: (NUM_FRAGMENTS[6], NUM_FRAGMENTS[6], TYPE_BUILD_PUZZLE[0], TYPE_PUZZLES[1]),
}

with open(f'{FOLDER_PATH}/test/saved_games.json') as fp:
    ID_GAME_TO_PARAMS = json.load(fp)

with open(f'{FOLDER_PATH}/test/saved_user_by_games.json') as fp:
    ID_SAVED_USER_BY_GAMES_TO_PARAMS = json.load(fp)

with open(f'{FOLDER_PATH}/test/saved_records.json') as fp:
    ID_RECORD_BY_PARAMS = json.load(fp)



class DatabaseController:

    NUM_MAX_RECORDS = 10

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
        config_path = f"{PATH_GAMES_DATA}/{id_save}.sage"
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
        _, _, type_build, _ = DatabaseController.get_diff_params(diff)
        if type_puzzle == TRIANGLE_PUZZLES:
            top_indx_position, bottom_indx_position = indx_position
            if type_build == BUILD_AREA:
                all_data = DatabaseController.create_game_triangle_config(top_indx_position, bottom_indx_position, score_value=0)
            elif type_build == BUILD_LENTA:
                indx_position_top_frame = [-1] * len(top_indx_position)
                indx_position_bottom_frame = [-1] * len(bottom_indx_position)
                all_data = DatabaseController.create_game_lenta_triangle_config(
                    indx_position_top_frame=indx_position_top_frame, indx_position_bottom_frame=indx_position_bottom_frame,
                    indx_position_top_scroll=top_indx_position, indx_position_bottom_scroll=bottom_indx_position,
                    score_value=0
                )
            else:
                raise ValueError()
        elif type_puzzle == RECTANGLE_PUZZLES:
            if type_build == BUILD_AREA:
                all_data = DatabaseController.create_game_rectangle_config(indx_position, score_value=0)
            elif type_build == BUILD_LENTA:
                indx_position_frame = [-1] * len(indx_position)
                all_data = DatabaseController.create_game_lenta_rectangle_config(
                    indx_position_frame, indx_position,
                    score_value=0)
            else:
                raise ValueError()
        else:
            raise ValueError()

        with open(config_path, 'w+') as fp:
            fp.write(all_data)

    @staticmethod
    def create_game_rectangle_config(indx_position: list, score_value: int = None) -> str:
        all_data = BETWEEN_NUMS.join(map(str, indx_position))
        if score_value is not None:
            all_data += NEW_LINE + str(score_value)
        return all_data

    @staticmethod
    def create_game_triangle_config(top_indx_position: list, bottom_indx_position: list, score_value: int = None) -> str:
        data_top_str = TOP_NUMS
        data_bottom_str = BOTTOM_NUMS
        data_top_str += BETWEEN_NUMS.join(map(str, top_indx_position))
        data_bottom_str += BETWEEN_NUMS.join(map(str, bottom_indx_position))
        all_data = data_top_str + SEP_TOP_AND_BOTTOM + data_bottom_str
        if score_value is not None:
            all_data += NEW_LINE + str(score_value)
        return all_data

    @staticmethod
    def create_game_lenta_rectangle_config(indx_position_frame: list, indx_position_scroll: list, score_value: int) -> str:
        # First - write about frame position
        frame_data = DatabaseController.create_game_rectangle_config(indx_position_frame)
        # Second - write about scroll position
        scroll_data = DatabaseController.create_game_rectangle_config(indx_position_scroll)
        # Connect two configs
        all_data = frame_data + NEW_LINE + scroll_data
        all_data += NEW_LINE + str(score_value)
        return all_data

    @staticmethod
    def create_game_lenta_triangle_config(
            indx_position_top_frame: list, indx_position_bottom_frame: list,
            indx_position_top_scroll: list, indx_position_bottom_scroll: list, score_value: int) -> str:
        # First - write about frame position
        frame_data = DatabaseController.create_game_triangle_config(
            indx_position_top_frame, indx_position_bottom_frame,
        )
        # Second - write about scroll position
        scroll_data = DatabaseController.create_game_triangle_config(
            indx_position_top_scroll, indx_position_bottom_scroll
        )
        # Connect two configs
        all_data = frame_data + NEW_LINE + scroll_data
        all_data += NEW_LINE + str(score_value)
        return all_data

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
    def parse_rectangle_config(game_config: str) -> List[int]:
        # Read stored file
        with open(game_config, 'r') as fp:
            data = fp.readlines()
        if len(data) != 2: # position and score
            raise ValueError()

        data = data[0]
        # Parse it
        return DatabaseController.parse_rectangle_data_str_to_position(data)

    @staticmethod
    def parse_triangle_config(game_config: str) -> Tuple[List[int], List[int]]:
        # Read stored file
        with open(game_config, 'r') as fp:
            data = fp.readlines()
        if len(data) != 2: # position and score
            raise ValueError()

        data = data[0]
        return DatabaseController.parse_triangle_data_str_to_top_and_bottom_position(data)

    @staticmethod
    def parse_lenta_scroll_rectangle_config(game_config: str) -> List[int]:
        # Read stored file
        with open(game_config, 'r') as fp:
            data = fp.readlines()
        if len(data) != 3: # position frame/position lenta/score
            raise ValueError()

        data = data[1] # Take scroll info
        # Parse it
        return DatabaseController.parse_rectangle_data_str_to_position(data)

    @staticmethod
    def parse_lenta_frame_rectangle_config(game_config: str) -> List[int]:
        # Read stored file
        with open(game_config, 'r') as fp:
            data = fp.readlines()
        if len(data) != 3: # position frame/position lenta/score
            raise ValueError()

        data = data[0] # Take frame info
        # Parse it
        return DatabaseController.parse_rectangle_data_str_to_position(data)

    @staticmethod
    def parse_lenta_scroll_triangle_config(game_config: str) -> Tuple[List[int], List[int]]:
        # Read stored file
        with open(game_config, 'r') as fp:
            data = fp.readlines()
        if len(data) != 3: # position frame/position lenta/score
            raise ValueError()

        data = data[1] # Take scroll info
        return DatabaseController.parse_triangle_data_str_to_top_and_bottom_position(data)

    @staticmethod
    def parse_lenta_frame_triangle_config(game_config: str) -> Tuple[List[int], List[int]]:
        # Read stored file
        with open(game_config, 'r') as fp:
            data = fp.readlines()
        if len(data) != 3: # position frame/position lenta/score
            raise ValueError()

        data = data[0] # Take frame info
        return DatabaseController.parse_triangle_data_str_to_top_and_bottom_position(data)

    @staticmethod
    def parse_rectangle_data_str_to_position(data: str) -> list:
        return list(map(int, data.split(",")))

    @staticmethod
    def parse_triangle_data_str_to_top_and_bottom_position(data: str) -> Tuple[List[int], List[int]]:
        # Cut into top and bottom
        top_str, bottom_str = data.split(SEP_TOP_AND_BOTTOM)
        top_str = top_str.split(SEP_NUMS)[-1]
        bottom_str = bottom_str.split(SEP_NUMS)[-1]

        top_pos_list = list(map(int, top_str.split(',')))
        bottom_pos_list = list(map(int, bottom_str.split(',')))

        return top_pos_list, bottom_pos_list

    @staticmethod
    def parse_score_config(game_config: str) -> int:
        # Read stored file
        with open(game_config, 'r') as fp:
            data = fp.readlines()
        if len(data) != 3 and len(data) != 2: # position frame/position lenta/score
            raise ValueError()

        data = data[-1] # Take score info, always last dimension
        return int(data)

    @staticmethod
    def save_game_rectangle(user_login: str, position_indx: list, diff: str, score_value: int, id_img: int, score_type: str):
        # Create config file and saved it
        all_data = DatabaseController.create_game_rectangle_config(indx_position=position_indx, score_value=score_value)

        id_saved_user_by_game = DatabaseController.take_unique_id(list(ID_SAVED_USER_BY_GAMES_TO_PARAMS.keys()))
        config_path = f"{PATH_SAVED_GAMES_DATA}/{id_saved_user_by_game}.sage"
        with open(config_path, 'w+') as fp:
            fp.write(all_data)

        DatabaseController.save_game_in_database(
            user_login=user_login, id_img=id_img, id_saved_user_by_game=id_saved_user_by_game,
            diff=diff, score_type=score_type, config_path=config_path
        )

    @staticmethod
    def save_game_triangle(
            user_login: str, position_top_indx: list,
            position_bottom_indx: list, diff: str, score_value: int, id_img: int, score_type: str):
        # Create config file and saved it
        all_data = DatabaseController.create_game_triangle_config(
            top_indx_position=position_top_indx, bottom_indx_position=position_bottom_indx,
            score_value=score_value
        )

        id_saved_user_by_game = DatabaseController.take_unique_id(list(ID_SAVED_USER_BY_GAMES_TO_PARAMS.keys()))
        config_path = f"{PATH_SAVED_GAMES_DATA}/{id_saved_user_by_game}.sage"
        with open(config_path, 'w+') as fp:
            fp.write(all_data)
        DatabaseController.save_game_in_database(
            user_login=user_login, id_img=id_img, id_saved_user_by_game=id_saved_user_by_game,
            diff=diff, score_type=score_type, config_path=config_path
        )

    @staticmethod
    def save_game_lenta_rectangle(
            user_login: str, position_frame_indx: list, position_lenta_indx: list,
            diff: str, score_value: int, id_img: int, score_type: str):
        # Create config file and saved it
        all_data = DatabaseController.create_game_lenta_rectangle_config(
            indx_position_frame=position_frame_indx, indx_position_scroll=position_lenta_indx,
            score_value=score_value
        )

        id_saved_user_by_game = DatabaseController.take_unique_id(list(ID_SAVED_USER_BY_GAMES_TO_PARAMS.keys()))
        config_path = f"{PATH_SAVED_GAMES_DATA}/{id_saved_user_by_game}.sage"
        with open(config_path, 'w+') as fp:
            fp.write(all_data)
        DatabaseController.save_game_in_database(
            user_login=user_login, id_img=id_img, id_saved_user_by_game=id_saved_user_by_game,
            diff=diff, score_type=score_type, config_path=config_path
        )

    @staticmethod
    def save_game_lenta_triangle(
            user_login: str, position_frame_top_indx: list, position_frame_bottom_indx: list,
            position_lenta_top_indx: list, position_lenta_bottom_indx: list,
            diff: str, score_value: int, id_img: int, score_type: str):
        # Create config file and saved it
        all_data = DatabaseController.create_game_lenta_triangle_config(
            indx_position_top_frame=position_frame_top_indx, indx_position_bottom_frame=position_frame_bottom_indx,
            indx_position_top_scroll=position_lenta_top_indx, indx_position_bottom_scroll=position_lenta_bottom_indx,
            score_value=score_value
        )

        id_saved_user_by_game = DatabaseController.take_unique_id(list(ID_SAVED_USER_BY_GAMES_TO_PARAMS.keys()))
        config_path = f"{PATH_SAVED_GAMES_DATA}/{id_saved_user_by_game}.sage"
        with open(config_path, 'w+') as fp:
            fp.write(all_data)
        DatabaseController.save_game_in_database(
            user_login=user_login, id_img=id_img, id_saved_user_by_game=id_saved_user_by_game,
            diff=diff, score_type=score_type, config_path=config_path
        )

    @staticmethod
    def save_game_in_database(
            user_login: str, id_saved_user_by_game: int, id_img: int,
            config_path: str, diff: str, score_type: str):
        global ID_SAVED_USER_BY_GAMES_TO_PARAMS, ID_GAME_TO_PARAMS

        ID_SAVED_USER_BY_GAMES_TO_PARAMS.update(
            {
                f"{id_saved_user_by_game}": {
                    "login": user_login,
                    "diff": diff,
                    "score_type": score_type,
                    'id_img': id_img,
                    'config_path': config_path
                }
            }
        )

        with open(f"{FOLDER_PATH}/test/saved_user_by_games.json", 'w') as fp:
            json.dump(ID_SAVED_USER_BY_GAMES_TO_PARAMS, fp)

    @staticmethod
    def get_saved_game(saved_game_id: int) -> str:
        for k in ID_SAVED_USER_BY_GAMES_TO_PARAMS.keys():
            if int(k) == int(saved_game_id):
                return ID_SAVED_USER_BY_GAMES_TO_PARAMS[k]['config_path']

        return None

    @staticmethod
    def get_all_saved_games_by_user(user_login: str) -> List[dict]:
        saved_games_info = []
        for k, v in ID_SAVED_USER_BY_GAMES_TO_PARAMS.items():
            if v['login'] == user_login:
                saved_games_info.append(
                    {
                        "id_img": v['id_img'],
                        'diff': v['diff'],
                        'score_type': v['score_type'],
                        "saved_game_id": k
                    }
                )

        return saved_games_info

    @staticmethod
    def remove_saved_game_by_user(saved_game_id: int):
        global ID_SAVED_USER_BY_GAMES_TO_PARAMS
        game_found = ID_SAVED_USER_BY_GAMES_TO_PARAMS.get(str(saved_game_id))
        if game_found is not None:
            del ID_SAVED_USER_BY_GAMES_TO_PARAMS[str(saved_game_id)]
            # Delete saved file
            os.remove(f'{PATH_SAVED_GAMES_DATA}/{saved_game_id}.sage')

    @staticmethod
    def add_record(user_login: str, diff: str, score_value: int, score_type: str):
        global ID_RECORD_BY_PARAMS

        all_records = DatabaseController.get_all_records(score_type)
        if len(all_records) == DatabaseController.NUM_MAX_RECORDS:
            is_bigger = False
            for elem in all_records:
                if elem['score_value'] < score_value:
                    is_bigger = True
                    break

            if is_bigger:
                # Delete lower
                DatabaseController.delete_record(all_records[0]['score_id'])
            else:
                # Otherwise - all other record has much more scores
                return

        id_record = DatabaseController.take_unique_id(list(ID_RECORD_BY_PARAMS.keys()))

        ID_RECORD_BY_PARAMS.update(
            {
                f"{id_record}":{
                    "user_login": user_login,
                    "diff": diff,
                    "score_value": score_value,
                    "score_type": score_type,
                }
            }
        )

        with open(f'{FOLDER_PATH}/test/saved_records.json', 'w') as fp:
            json.dump(ID_RECORD_BY_PARAMS, fp)

    @staticmethod
    def get_all_records(score_type: str):
        global ID_RECORD_BY_PARAMS
        records_data_dict = []
        for k, v in ID_RECORD_BY_PARAMS.items():
            if v['score_type'] == score_type:
                records_data_dict.append({
                    "user_login": v["user_login"],
                    "diff": v["diff"],
                    "score_value": v["score_value"],
                    "score_id": int(k)
                })
        # From lower to bigger
        records_data_dict = sorted(records_data_dict, key=lambda x: x['score_value'])
        return records_data_dict

    @staticmethod
    def delete_record(id_record: int):
        global ID_RECORD_BY_PARAMS
        taken = ID_RECORD_BY_PARAMS.get(str(id_record))
        if taken is not None:
            del ID_RECORD_BY_PARAMS[str(id_record)]

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

    @staticmethod
    def take_unique_id(id_copies: list):
        id_save = random.randint(0, 1_000_000)
        all_ids_set = set(list(map(int, id_copies)))
        while id_save in all_ids_set:
            id_save = random.randint(0, 1_000_000)
        return id_save

