from puzzle.user.game.new_game.puzzle_game.common.constants import FRAME_H, FRAME_W

from .game_on_field_triangle_ui import Ui_Form
from PySide6.QtWidgets import QWidget

from .qfield_triangle_frame import OnFieldTriangleFrame

from puzzle.database import DatabaseController


class GameOnFieldTriangleWidget(QWidget):

    def __init__(self, id_img: str, diff: str, size_block_w: int, size_block_h: int):
        super().__init__()
        self._id_img = id_img
        self._diff = diff
        self._img_path = DatabaseController.get_img(id_img)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        game_config = DatabaseController.get_game_config(diff=diff, id_img=id_img)
        self._custom_frame = OnFieldTriangleFrame(
            self._img_path, game_config=game_config,
            size_block_w=size_block_w, size_block_h=size_block_h
        )
        self._custom_frame.setFixedWidth(FRAME_W)
        self._custom_frame.setFixedHeight(FRAME_H)

        self.ui.game_gridLayout.addWidget(self._custom_frame, 2, 0, 1, 6)
        self.setLayout(self.ui.game_gridLayout)


