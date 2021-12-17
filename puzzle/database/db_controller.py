import os
import traceback
import pathlib
import glob

from typing import Tuple, List, Union
from puzzle.utils import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .tables import Base, User, Image, Game, SavedGame, Record, DifficultyParams


engine = create_engine(f'sqlite:///database_puzzle.db', echo=True)

# Создание таблицы
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

NEW_LINE = '\n'
BETWEEN_NUMS = ','
SEP_TOP_AND_BOTTOM = "|"
SEP_NUMS = ":"
TOP_NUMS = f"top{SEP_NUMS}"
BOTTOM_NUMS = f"bottom{SEP_NUMS}"


FOLDER_PATH = pathlib.Path().resolve()
FOLDER_PATH = "."
PATH_TEMP_DATA = f"{FOLDER_PATH}/temp"
PATH_GAMES_DATA = f"{PATH_TEMP_DATA}/games"
PATH_SAVED_GAMES_DATA = f'{PATH_TEMP_DATA}/saved_games'
PATH_DB = f'{FOLDER_PATH}/database_puzzle.db'

os.makedirs(f"{PATH_TEMP_DATA}", exist_ok=True)
os.makedirs(f"{PATH_GAMES_DATA}", exist_ok=True)
os.makedirs(f"{PATH_SAVED_GAMES_DATA}", exist_ok=True)


class DatabaseController:

    NUM_MAX_RECORDS = 10

    @staticmethod
    def take_all_imgs() -> List[Image]:
        """
        return list of tuples
        First element - path to img
        Second element - id of image

        """
        global session
        try:
            image_list = session.query(Image).all()
        except Exception:
            traceback.print_exc()
            return None

        return image_list

    @staticmethod
    def get_img(id_img: int, return_as_class: bool = False) -> Union[str, Image]:
        global session
        try:
            founded_image: Image = session.query(Image).filter_by(id=int(id_img)).first()
            if return_as_class:
                return founded_image
            return founded_image.image_path # return path
        except Exception:
            return None

    @staticmethod
    def get_img_name(id_img: int) -> str:
        image_path = DatabaseController.get_img(id_img, return_as_class=True)
        if image_path is None:
            return
        return image_path.get_img_name()

    @staticmethod
    def remove_img(id_img: int) -> bool:
        global session
        try:
            img: Image = session.query(Image).filter_by(id=int(id_img)).first()
            if os.path.isfile(img.image_path):
                os.remove(img.image_path)
            session.delete(img)
            session.commit()
        except Exception:
            traceback.print_exc()
            return False

        return True

    @staticmethod
    def is_img_exist_by_name(image_name: str) -> bool:
        """
        Return
            True - if image with this path does not exist
            False - if image with this path exist
            None - error while connect to db

        """
        global session
        try:
            path_img_in_temp = os.path.join(PATH_TEMP_DATA, f'{image_name}.png')
            result: Image = session.query(Image).filter_by(image_path=path_img_in_temp).first()
            if result is not None:
                return False

            return True
        except Exception:
            traceback.print_exc()
            return None

    @staticmethod
    def add_image(path: str, name: str) -> bool:
        path_new_save = os.path.join(PATH_TEMP_DATA, f'{name}.png')
        result = save_img_in_temp(path, size_w=FRAME_W, size_h=FRAME_H, path_save_to=path_new_save)
        if not result:
            # cannot  save or read img
            return False

        image = Image(image_path=path_new_save)
        try:
            session.add(image)
            session.commit()
        except Exception:
            traceback.print_exc()
            return False

        return True

    @staticmethod
    def add_user(login: str, password: str, role: str = ROLE_USER) -> bool:
        """
        Return:
            True - if user was added into database
            None - if was some error while connecting/add user into database

        """
        user = User(login, password, role)
        try:
            if DatabaseController.find_user(login, password):
                return False
            session.add(user)
            session.commit()
        except Exception:
            traceback.print_exc()
            return None

        return True

    @staticmethod
    def get_role_user(login: str) -> str:
        """
        Return role of certain user with `login`

        """
        try:
            founded_user: User = session.query(User).filter_by(login=login).first()
            return founded_user.role
        except Exception:
            return None

    @staticmethod
    def find_user(login: str, password: str) -> bool:
        """
        Return:
            True - if user exist
            False - not found

        """
        global session
        try:
            founded_user: User = session.query(User).filter_by(login=login, password=password).first()
            if founded_user is None:
                return False

            return True
        except Exception:
            return None

    @staticmethod
    def add_new_game(id_img: int, indx_position: list, diff: str) -> bool:

        # Check id img
        found_img = DatabaseController.get_img(id_img)
        if found_img is None:
            return False # Img is not in DataBase

        # Save game in db
        config_path = f"{PATH_GAMES_DATA}/{diff}_{id_img}.sage"
        game = Game(diff=diff, id_img=id_img, config_path=config_path)
        try:
            session.add(game)
            session.commit()
        except Exception:
            traceback.print_exc()
            return False
        # ---
        _, _, type_build, type_puzzle = DatabaseController.get_diff_params(diff)

        if type_puzzle is None:
            return False

        if type_puzzle == TRIANGLE_PUZZLES:
            top_indx_position, bottom_indx_position = indx_position
            if type_build == BUILD_AREA:
                all_data = DatabaseController.create_game_triangle_config(
                    top_indx_position, bottom_indx_position, score_value=0
                )
            elif type_build == BUILD_LENTA:
                indx_position_top_frame = [-1] * len(top_indx_position)
                indx_position_bottom_frame = [-1] * len(bottom_indx_position)
                all_data = DatabaseController.create_game_lenta_triangle_config(
                    indx_position_top_frame=indx_position_top_frame, indx_position_bottom_frame=indx_position_bottom_frame,
                    indx_position_top_scroll=top_indx_position, indx_position_bottom_scroll=bottom_indx_position,
                    score_value=0
                )
            else:
                return False
        elif type_puzzle == RECTANGLE_PUZZLES:
            if type_build == BUILD_AREA:
                all_data = DatabaseController.create_game_rectangle_config(indx_position, score_value=0)
            elif type_build == BUILD_LENTA:
                indx_position_frame = [-1] * len(indx_position)
                all_data = DatabaseController.create_game_lenta_rectangle_config(
                    indx_position_frame, indx_position,
                    score_value=0)
            else:
                return False
        else:
            return False

        with open(config_path, 'w+') as fp:
            fp.write(all_data)

        return True

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
    def get_all_games() -> List[Game]:
        global session
        try:
            game_list: List[Game] = session.query(Game).all()
            return game_list
        except Exception:
            traceback.print_exc()
            return None # Something goes wrong

    @staticmethod
    def get_game_imgs(diff: str) -> list:
        global session
        try:
            game_list: List[Game] = session.query(Game).all()
        except Exception:
            traceback.print_exc()
            return None # Something goes wrong

        found_imgs_list = []
        for game_s in game_list:
            if game_s.diff == diff:
                found_imgs_list.append(game_s.id_img)

        return found_imgs_list

    @staticmethod
    def get_game_config(diff: str, id_img: str) -> str:
        global session
        try:
            game: Game = session.query(Game).filter_by(diff=diff, id_img=int(id_img)).first()
            if game is None:
                return None
            return game.config_path
        except Exception:
            traceback.print_exc()
            return None # Something goes wrong

    @staticmethod
    def delete_game(game_id: int) -> bool:
        global session
        try:
            game: Game = session.query(Game).filter_by(id=int(game_id)).first()
            session.delete(game)
            session.commit()
            return True
        except Exception:
            traceback.print_exc()
            return False # Something goes wrong

    @staticmethod
    def parse_rectangle_config(game_config: str) -> List[int]:
        # Read stored file
        try:
            with open(game_config, 'r') as fp:
                data = fp.readlines()
        except Exception:
            return None
        if len(data) != 2: # position and score
            raise ValueError()

        data = data[0]
        # Parse it
        return DatabaseController.parse_rectangle_data_str_to_position(data)

    @staticmethod
    def parse_triangle_config(game_config: str) -> Tuple[List[int], List[int]]:
        # Read stored file
        try:
            with open(game_config, 'r') as fp:
                data = fp.readlines()
        except Exception:
            return None, None
        if len(data) != 2: # position and score
            raise ValueError()

        data = data[0]
        return DatabaseController.parse_triangle_data_str_to_top_and_bottom_position(data)

    @staticmethod
    def parse_lenta_scroll_rectangle_config(game_config: str) -> List[int]:
        # Read stored file
        try:
            with open(game_config, 'r') as fp:
                data = fp.readlines()
        except Exception:
            return None
        if len(data) != 3: # position frame/position lenta/score
            raise ValueError()

        data = data[1] # Take scroll info
        # Parse it
        return DatabaseController.parse_rectangle_data_str_to_position(data)

    @staticmethod
    def parse_lenta_frame_rectangle_config(game_config: str) -> List[int]:
        # Read stored file
        try:
            with open(game_config, 'r') as fp:
                data = fp.readlines()
        except Exception:
            return None
        if len(data) != 3: # position frame/position lenta/score
            raise ValueError()

        data = data[0] # Take frame info
        # Parse it
        return DatabaseController.parse_rectangle_data_str_to_position(data)

    @staticmethod
    def parse_lenta_scroll_triangle_config(game_config: str) -> Tuple[List[int], List[int]]:
        # Read stored file
        try:
            with open(game_config, 'r') as fp:
                data = fp.readlines()
        except Exception:
            return None, None
        if len(data) != 3: # position frame/position lenta/score
            raise ValueError()

        data = data[1] # Take scroll info
        return DatabaseController.parse_triangle_data_str_to_top_and_bottom_position(data)

    @staticmethod
    def parse_lenta_frame_triangle_config(game_config: str) -> Tuple[List[int], List[int]]:
        # Read stored file
        try:
            with open(game_config, 'r') as fp:
                data = fp.readlines()
        except Exception:
            return None
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
        try:
            with open(game_config, 'r') as fp:
                data = fp.readlines()
        except Exception:
            return None
        if len(data) != 3 and len(data) != 2: # position frame/position lenta/score
            return None

        data = data[-1] # Take score info, always last dimension
        return int(data)

    @staticmethod
    def save_game_rectangle(
            user_login: str, position_indx: list, diff: str,
            score_value: int, id_img: int, score_type: str) -> bool:
        # Create config file and saved it
        all_data = DatabaseController.create_game_rectangle_config(
            indx_position=position_indx, score_value=score_value
        )
        config_path = f"{PATH_SAVED_GAMES_DATA}/{user_login}_{diff}_{id_img}_{score_type}.sage"
        with open(config_path, 'w+') as fp:
            fp.write(all_data)

        return DatabaseController.save_game_in_database(
            user_login=user_login, id_img=id_img,
            diff=diff, score_type=score_type, config_path=config_path
        )

    @staticmethod
    def save_game_triangle(
            user_login: str, position_top_indx: list,
            position_bottom_indx: list, diff: str, score_value: int, id_img: int, score_type: str) -> bool:
        # Create config file and saved it
        all_data = DatabaseController.create_game_triangle_config(
            top_indx_position=position_top_indx, bottom_indx_position=position_bottom_indx,
            score_value=score_value
        )
        config_path = f"{PATH_SAVED_GAMES_DATA}/{user_login}_{diff}_{id_img}_{score_type}.sage"
        with open(config_path, 'w+') as fp:
            fp.write(all_data)

        return DatabaseController.save_game_in_database(
            user_login=user_login, id_img=id_img,
            diff=diff, score_type=score_type, config_path=config_path
        )

    @staticmethod
    def save_game_lenta_rectangle(
            user_login: str, position_frame_indx: list, position_lenta_indx: list,
            diff: str, score_value: int, id_img: int, score_type: str) -> bool:
        # Create config file and saved it
        all_data = DatabaseController.create_game_lenta_rectangle_config(
            indx_position_frame=position_frame_indx, indx_position_scroll=position_lenta_indx,
            score_value=score_value
        )
        config_path = f"{PATH_SAVED_GAMES_DATA}/{user_login}_{diff}_{id_img}_{score_type}.sage"
        with open(config_path, 'w+') as fp:
            fp.write(all_data)

        return DatabaseController.save_game_in_database(
            user_login=user_login, id_img=id_img,
            diff=diff, score_type=score_type, config_path=config_path
        )

    @staticmethod
    def save_game_lenta_triangle(
            user_login: str, position_frame_top_indx: list, position_frame_bottom_indx: list,
            position_lenta_top_indx: list, position_lenta_bottom_indx: list,
            diff: str, score_value: int, id_img: int, score_type: str) -> bool:
        # Create config file and saved it
        all_data = DatabaseController.create_game_lenta_triangle_config(
            indx_position_top_frame=position_frame_top_indx, indx_position_bottom_frame=position_frame_bottom_indx,
            indx_position_top_scroll=position_lenta_top_indx, indx_position_bottom_scroll=position_lenta_bottom_indx,
            score_value=score_value
        )
        config_path = f"{PATH_SAVED_GAMES_DATA}/{user_login}_{diff}_{id_img}_{score_type}.sage"
        with open(config_path, 'w+') as fp:
            fp.write(all_data)

        return DatabaseController.save_game_in_database(
            user_login=user_login, id_img=id_img,
            diff=diff, score_type=score_type, config_path=config_path
        )

    @staticmethod
    def save_game_in_database(
            user_login: str, id_img: int,
            config_path: str, diff: str, score_type: str) -> bool:
        global session
        saved_game = SavedGame(
            login=user_login, id_img=id_img,
            diff=diff, config_path=config_path,
            score_type=score_type
        )
        try:
            # We must rewrite saved game with same params
            saved_double_game: SavedGame = session.query(SavedGame).filter_by(
                login=user_login, id_img=id_img, diff=diff, score_type=score_type
            ).first()

            if saved_double_game is not None:
                DatabaseController.delete_saved_game(saved_double_game.id, delete_file=False)

            session.add(saved_game)
            session.commit()
        except Exception:
            traceback.print_exc()
            return False

        return True

    @staticmethod
    def delete_saved_game(saved_game_id: int, delete_file=True) -> bool:
        global session
        try:
            founded_saved_game: SavedGame = session.query(SavedGame).filter_by(id=int(saved_game_id)).first()
            if delete_file and os.path.isfile(founded_saved_game.config_path):
                os.remove(founded_saved_game.config_path)
            session.delete(founded_saved_game)
            session.commit()
        except Exception:
            traceback.print_exc()
            return False # Something goes wrong
        return True

    @staticmethod
    def get_saved_game(saved_game_id: int) -> str:
        global session
        try:
            founded_saved_game: SavedGame = session.query(SavedGame).filter_by(id=int(saved_game_id)).first()
            return founded_saved_game.config_path
        except Exception:
            traceback.print_exc()
            return None # Something goes wrong
        return None

    @staticmethod
    def get_all_saved_games() -> List[SavedGame]:
        global session
        try:
            founded_saved_game: List[SavedGame] = session.query(SavedGame).all()
            return founded_saved_game
        except Exception:
            traceback.print_exc()
            return None # Something goes wrong

    @staticmethod
    def get_all_saved_games_by_user(user_login: str) -> List[dict]:
        global session
        try:
            founded_saved_game: List[SavedGame] = session.query(SavedGame).filter_by(login=user_login).all()
        except Exception:
            traceback.print_exc()
            return None # Something goes wrong
        saved_games_info = []
        for saved_game_s in founded_saved_game:
            if saved_game_s.login == user_login:
                saved_games_info.append(
                    {
                        "id_img": saved_game_s.id_img,
                        'diff': saved_game_s.diff,
                        'score_type': saved_game_s.score_type,
                        "saved_game_id": saved_game_s.id
                    }
                )

        return saved_games_info

    @staticmethod
    def remove_saved_game_by_user(saved_game_id: int) -> bool:
        global session
        try:
            saved_game: SavedGame = session.query(SavedGame).filter_by(id=int(saved_game_id)).first()
            if os.path.isfile(saved_game.config_path):
                os.remove(saved_game.config_path)
            session.delete(saved_game)
            session.commit()
        except Exception:
            traceback.print_exc()
            return False

        return True

    @staticmethod
    def add_record_top10(user_login: str, diff: str, score_value: int, score_type: str) -> bool:
        global session

        all_records: List[Record] = DatabaseController.get_all_records(score_type)

        if all_records is None:
            return False

        if len(all_records) == DatabaseController.NUM_MAX_RECORDS:
            if all_records[0].score_value < score_value:
                # We must delete first record and append new one
                DatabaseController.delete_record(all_records[0].id)
                # Append new one
                return DatabaseController.add_record(
                    user_login=user_login, diff=diff,
                    score_type=score_type, score_value=score_value
                )
        # If count less than maximum - append current record
        return DatabaseController.add_record(
            user_login=user_login, diff=diff,
            score_type=score_type, score_value=score_value
        )

    @staticmethod
    def add_record(user_login: str, diff: str, score_value: int, score_type: str) -> bool:
        try:
            new_record = Record(
                login=user_login, diff=diff,
                score_value=score_value, score_type=score_type
            )
            session.add(new_record)
            session.commit()
        except Exception:
            traceback.print_exc()
            return False  # Something goes wrong

        return True

    @staticmethod
    def get_all_records(score_type: str) -> List[Record]:
        global session
        try:
            all_records: List[Record] = session.query(Record).filter_by(
                score_type=score_type
            ).order_by(Record.score_value.desc()).all()
        except Exception:
            traceback.print_exc()
            return None
        return all_records

    @staticmethod
    def delete_record(id_record: int):
        global session
        try:
            record = session.query(Record).filter_by(id=int(id_record)).first()
            session.delete(record)
            session.commit()
        except Exception:
            traceback.print_exc()
            return False # Something goes wrong

    @staticmethod
    def update_diff(diff: str, frag_h: int, frag_v: int, type_build: str, type_puzzle: str) -> bool:
        global session
        try:
            # Delete old config
            old_diff = session.query(DifficultyParams).filter_by(diff=diff).first()
            session.delete(old_diff)
            # Append new one
            new_diff_params = DifficultyParams(
                diff=diff, frag_h=frag_h, frag_v=frag_v,
                type_build=type_build, type_puzzle=type_puzzle
            )
            session.add(new_diff_params)
            session.commit()
        except Exception:
            traceback.print_exc()
            return False # Something goes wrong

        return True

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
        global session
        try:
            diff_params: DifficultyParams = session.query(DifficultyParams).filter_by(diff=diff).first()
            # If we do not found our setup - define default params
            if diff_params is None:
                # Reset params
                DatabaseController.define_default_diff_params()
            # Take it again
            diff_params: DifficultyParams = session.query(DifficultyParams).filter_by(diff=diff).first()
        except Exception:
            traceback.print_exc()
            return None, None, None, None # Something goes wrong
        return diff_params.frag_h, diff_params.frag_v, diff_params.type_build, diff_params.type_puzzle

    @staticmethod
    def define_default_diff_params():
        global session
        for diff in DIFFIC_LIST:
            diff_params: DifficultyParams = session.query(DifficultyParams).filter_by(diff=diff).first()
            if diff_params is None:
                # Add param
                diff_params = DifficultyParams(
                    diff=diff, frag_h=NUM_FRAGMENTS[0], frag_v=NUM_FRAGMENTS[0],
                    type_build=TYPE_BUILD_PUZZLE[0], type_puzzle=TYPE_PUZZLES[0]
                )
                session.add(diff_params)

        session.commit()

    @staticmethod
    def clear_temp():

        if not os.path.isfile(PATH_DB):
            return

        def get_file_name(file: str) -> str:
            return file.split('/')[-1].split('\\')[-1]

        def remove_list_files(list_files: list):
            for s_file in list_files:
                if os.path.isfile(s_file):
                    os.remove(s_file)

        need_remove_list = []
        need_remove_from_db_list = []
        # Clear games
        games_list = DatabaseController.get_all_games()
        if games_list is not None:
            all_games_in_temp = glob.glob(PATH_GAMES_DATA + '/*.sage')
            set_games_db = set([
                get_file_name(game_s.config_path)
                for game_s in games_list
            ])
            dict_games_db = dict([
                (get_file_name(game_s.config_path), game_s)
                for game_s in games_list
            ])
            for game_s in all_games_in_temp:
                if get_file_name(game_s) not in set_games_db:
                    need_remove_list.append(game_s)
                else:
                    del dict_games_db[get_file_name(game_s)]
            remove_list_files(need_remove_list)
            # Remove remain data from db
            for game_s in dict_games_db.values():
                DatabaseController.delete_game(game_s.id)

        need_remove_list = []
        # Clear saved games
        saved_games_list = DatabaseController.get_all_saved_games()
        if saved_games_list is not None:
            all_saved_games_in_temp = glob.glob(PATH_SAVED_GAMES_DATA + '/*.sage')
            set_saved_games_db = set([
                get_file_name(saved_game_s.config_path)
                for saved_game_s in saved_games_list
            ])
            dict_saved_games_db = dict([
                (get_file_name(saved_game_s.config_path), saved_game_s)
                for saved_game_s in saved_games_list
            ])
            for saved_game_s in all_saved_games_in_temp:
                if get_file_name(saved_game_s) not in set_saved_games_db:
                    need_remove_list.append(saved_game_s)
                else:
                    del dict_saved_games_db[get_file_name(saved_game_s)]
            remove_list_files(need_remove_list)
            # Remove remain data from db
            for saved_game_s in dict_saved_games_db.values():
                DatabaseController.delete_saved_game(saved_game_s.id)
        need_remove_list = []
        # Clear images
        all_imgs_list = DatabaseController.take_all_imgs()
        if all_imgs_list is not None:
            all_img_in_temp = glob.glob(PATH_TEMP_DATA + '/*.png')
            set_img_db = set([
                get_file_name(img_s.image_path)
                for img_s in all_imgs_list
            ])
            dict_img_db = dict([
                (get_file_name(img_s.image_path), img_s)
                for img_s in all_imgs_list
            ])
            for img_s in all_img_in_temp:
                if get_file_name(img_s) not in set_img_db:
                    need_remove_list.append(img_s)
                else:
                    del dict_img_db[get_file_name(img_s)]
            remove_list_files(need_remove_list)
            # Remove remain data from db
            for img_s in dict_img_db.values():
                DatabaseController.remove_img(img_s.id)

# Clear at the start
DatabaseController.clear_temp()