from .qfield_frame import OnFieldRectangleFrame
from puzzle.user.game.new_game.puzzle_game.common.constants import FRAME_H, FRAME_W
from .game_on_field_rectangle_ui import Ui_Form

from puzzle.user.game.new_game.puzzle_game.common.game_base_widget import GameBaseWidget
from puzzle.database import DatabaseController


class GameOnFieldRectangleWidget(GameBaseWidget):

    def __init__(
            self, user_login: str, id_img: str, diff: str,
            size_block_w: int, size_block_h: int, score_type: str, saved_game_id: int = None):
        super().__init__(
            user_login=user_login, id_img=id_img, diff=diff,
            score_type=score_type, saved_game_id=saved_game_id
        )
        self._size_block_w = size_block_w
        self._size_block_h = size_block_h
        self._game_frame: OnFieldRectangleFrame = None
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.build_game()
        # Buttons
        self.ui.save_game_pushButton.clicked.connect(self.clicked_save_game)
        self.ui.look_full_image_pushButton.clicked.connect(super().preview_full_image)

        self.setLayout(self.ui.game_gridLayout)

    def clicked_save_game(self):
        # Take info from game
        indx_position = self._game_frame.get_game_info()
        # Take score value
        score_value = int(self.ui.score_value_label.text())
        DatabaseController.save_game_rectangle(
            user_login=self._user_login, position_indx=indx_position,
            diff=self._diff, score_value=score_value, id_img=self._id_img,
            score_type=self._score_type
        )

    def update_score(self):
        max_placed, bad_placed = self._game_frame.get_all_num_and_bad_placeses()
        score_value = super().take_new_score(bad_placed=bad_placed, max_placed=max_placed)

        self.ui.score_value_label.setText(str(score_value))

    def current_game_state(self) -> bool:
        """
        Return True if game is ended otherwise - False

        """
        _, bad_placed = self._game_frame.get_all_num_and_bad_placeses()
        return bad_placed == 0

    def build_game(self):
        self._game_frame = OnFieldRectangleFrame(
            self._img_path, game_config=self._game_config,
            size_block_w=self._size_block_w, size_block_h=self._size_block_h
        )
        self._game_frame.setFixedWidth(FRAME_W)
        self._game_frame.setFixedHeight(FRAME_H)

        self.ui.score_value_label.setText(str(self._start_score))
        self.ui.game_gridLayout.addWidget(self._game_frame, 2, 0, 1, 6)

        self.start_game()