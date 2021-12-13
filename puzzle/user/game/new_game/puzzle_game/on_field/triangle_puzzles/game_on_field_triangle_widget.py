from puzzle.common.qmess_boxes import return_qmess_box_connect_db_error
from puzzle.user.game.new_game.puzzle_game.common.constants import FRAME_H, FRAME_W

from .game_on_field_triangle_ui import Ui_GameTriangleOnField
from PySide6.QtWidgets import QWidget

from .qfield_triangle_frame import OnFieldTriangleFrame

from puzzle.user.game.new_game.puzzle_game.common.game_base_widget import GameBaseWidget
from puzzle.database import DatabaseController


class GameOnFieldTriangleWidget(GameBaseWidget):

    def __init__(
            self, user_login: str, id_img: str, diff: str,
            size_block_w: int, size_block_h: int, score_type: str, saved_game_id: int = None):
        super().__init__(
            user_login=user_login, id_img=id_img, diff=diff,
            score_type=score_type, saved_game_id=saved_game_id,
            size_block_w=size_block_w, size_block_h=size_block_h
        )
        self._custom_frame: OnFieldTriangleFrame = None
        self.ui = Ui_GameTriangleOnField()
        self.ui.setupUi(self)

        self.ui.save_game_pushButton.clicked.connect(self.clicked_save_game)
        self.ui.look_full_image_pushButton.clicked.connect(super().preview_full_image)

        self.setLayout(self.ui.game_gridLayout)
        self.build_game()

    def clicked_save_game(self):
        # Take info from game
        position_top_indx, position_bottom_indx = self._custom_frame.get_game_info()
        # Take score value
        score_value = int(self.ui.score_value_label.text())
        result = DatabaseController.save_game_triangle(
            user_login=self._user_login, position_top_indx=position_top_indx,
            position_bottom_indx=position_bottom_indx,
            diff=self._diff, score_value=score_value, id_img=self._id_img,
            score_type=self._score_type
        )

        if not result:
            self._qmess_box = return_qmess_box_connect_db_error()
            self._qmess_box.show()
            return

    def update_score(self):
        max_placed, bad_placed = self._custom_frame.get_all_num_and_bad_placeses()
        score_value = super().take_new_score(bad_placed=bad_placed, max_placed=max_placed)

        self.ui.score_value_label.setText(str(score_value))

    def current_game_state(self) -> bool:
        """
        Return True if game is ended otherwise - False

        """
        _, bad_placed = self._custom_frame.get_all_num_and_bad_placeses()
        return bad_placed == 0

    def build_game(self):
        self._custom_frame = OnFieldTriangleFrame(
            self._img_path, game_config=self._game_config,
            size_block_w=self._size_block_w, size_block_h=self._size_block_h
        )
        self._custom_frame.setFixedWidth(FRAME_W)
        self._custom_frame.setFixedHeight(FRAME_H)

        self.ui.score_value_label.setText(str(self._start_score))
        self.ui.game_gridLayout.addWidget(self._custom_frame, 2, 0, 1, 6)

        self.start_game()


