from puzzle.database import DatabaseController
from puzzle.utils import DIFFIC_LIST, TYPE_SCORE, BUILD_AREA, BUILD_LENTA, TRIANGLE_PUZZLES, RECTANGLE_PUZZLES
from .on_field import GameOnFieldRectangleWidget, GameOnFieldTriangleWidget
from .on_lenta import PuzzleGameOnLentaRectangleWidget, PuzzleGameOnLentaTriangleWidget


class BuildGameWidgetController:

    @staticmethod
    def build_widget(diff: str, score_type: str, user_login: str, id_img: int, saved_game_id: int = None):
        # Is img can be set with this diff?
        result_config = DatabaseController.get_game_config(diff, id_img)
        if result_config is None:
            return None # I.e. game with this img does not exist

        # Create widget game...
        frag_h, frag_v, type_build, type_puzzle = DatabaseController.get_diff_params(diff)
        if frag_h is None:
            return None
        if type_build == BUILD_AREA:
            if type_puzzle == RECTANGLE_PUZZLES:
                widget_game = GameOnFieldRectangleWidget(
                    user_login=user_login, id_img=id_img, diff=diff,
                    size_block_h=int(frag_h), size_block_w=int(frag_v), score_type=score_type,
                    saved_game_id=saved_game_id
                )
            elif type_puzzle == TRIANGLE_PUZZLES:
                widget_game = GameOnFieldTriangleWidget(
                    user_login=user_login, id_img=id_img, diff=diff,
                    size_block_h=int(frag_h), size_block_w=int(frag_v),
                    score_type=score_type,
                    saved_game_id=saved_game_id
                )
            else:
                raise ValueError(f"Unknown type of puzzle: {type_build}, while type build: {type_build}")
        elif type_build == BUILD_LENTA:
            if type_puzzle == RECTANGLE_PUZZLES:
                widget_game = PuzzleGameOnLentaRectangleWidget(
                    user_login=user_login, id_img=id_img, diff=diff,
                    size_block_h=int(frag_h), size_block_w=int(frag_v),
                    score_type=score_type,
                    saved_game_id=saved_game_id
                )
            elif type_puzzle == TRIANGLE_PUZZLES:
                widget_game = PuzzleGameOnLentaTriangleWidget(
                    user_login=user_login, id_img=id_img, diff=diff,
                    size_block_h=int(frag_h), size_block_w=int(frag_v),
                    score_type=score_type,
                    saved_game_id=saved_game_id
                )
            else:
                raise ValueError(f"Unknown type of puzzle: {type_build}, while type build: {type_build}")
        else:
            raise ValueError(f"Unknown type build: {type_build}")

        return widget_game
