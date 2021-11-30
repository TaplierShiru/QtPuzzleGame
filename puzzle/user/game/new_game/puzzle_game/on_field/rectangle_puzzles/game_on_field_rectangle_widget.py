
from PySide6.QtWidgets import QWidget, QGridLayout

from .qfield_frame import CustomOnFieldFrame
from puzzle.user.game.new_game.puzzle_game.common.constants import FRAME_H, FRAME_W

from .game_on_field_rectangle_ui import Ui_Form


class GameOnFieldRectangleWidget(QWidget):

    def __init__(self, img_path: str, size_block_w: int, size_block_h: int):
        super().__init__()
        self._img_path = img_path
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.init_ui(size_block_h=size_block_h, size_block_w=size_block_w)

    def init_ui(self, size_block_w: int, size_block_h: int):

        self._custom_frame = CustomOnFieldFrame(
            self._img_path,
            size_block_w=size_block_w, size_block_h=size_block_h
        )
        self._custom_frame.setFixedWidth(FRAME_W)
        self._custom_frame.setFixedHeight(FRAME_H)

        self.ui.game_gridLayout.addWidget(self._custom_frame, 2, 0, 1, 6)
        self.setLayout(self.ui.game_gridLayout)

