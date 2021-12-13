from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import  QPalette


from PySide6.QtWidgets import QWidget, QScrollArea, QAbstractScrollArea, QSizePolicy

from puzzle import DatabaseController
from puzzle.common.qmess_boxes import return_qmess_box_connect_db_error
from puzzle.user.game.new_game.puzzle_game.common.signals import SignalSenderSendDataImageTriangle

from .game_on_lenta_triangle_ui import Ui_GameTriangleOnLenta
from .qlenta_area_widget import ScrolledTriangleFrame
from .qlenta_frame import OnLentaTriangleFrame

from puzzle.user.game.new_game.puzzle_game.common.game_base_widget import GameBaseWidget

from puzzle.utils import FRAME_H, FRAME_W


class PuzzleGameOnLentaTriangleWidget(GameBaseWidget):

    def __init__(
            self, user_login: str, id_img: str, diff: str,
            size_block_w: int, size_block_h: int, score_type: str, saved_game_id: int = None):
        super().__init__(
            user_login=user_login, id_img=id_img, diff=diff,
            score_type=score_type, saved_game_id=saved_game_id,
            size_block_w=size_block_w, size_block_h=size_block_h
        )
        self._game_frame: OnLentaTriangleFrame = None
        self._lenta_frame: ScrolledTriangleFrame = None
        self.ui = Ui_GameTriangleOnLenta()
        self.ui.setupUi(self)

        self.build_game()
        # Buttons
        self.ui.save_game_pushButton.clicked.connect(self.clicked_save_game)
        self.ui.look_full_image_pushButton.clicked.connect(super().preview_full_image)
        self.setLayout(self.ui.game_gridLayout)

    def clicked_save_game(self):
        # Take info from game
        position_frame_top_indx, position_frame_bottom_indx = self._game_frame.get_game_info()
        position_lenta_top_indx, position_lenta_bottom_indx = self._lenta_frame.get_game_info()
        # Take score value
        score_value = int(self.ui.score_value_label.text())
        result = DatabaseController.save_game_lenta_triangle(
            user_login=self._user_login,
            position_frame_top_indx=position_frame_top_indx, position_frame_bottom_indx=position_frame_bottom_indx,
            position_lenta_top_indx=position_lenta_top_indx, position_lenta_bottom_indx=position_lenta_bottom_indx,
            diff=self._diff, score_value=score_value, id_img=self._id_img,
            score_type=self._score_type
        )

        if not result:
            self._qmess_box = return_qmess_box_connect_db_error()
            self._qmess_box.show()
            return

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
        signal_sender_on_scroll = SignalSenderSendDataImageTriangle()

        self._game_frame = OnLentaTriangleFrame(
            self._img_path,
            size_block_w=self._size_block_w, size_block_h=self._size_block_h,
            signal_sender_on_scroll=signal_sender_on_scroll,
            game_config=self._game_config
        )
        self._game_frame.setFixedWidth(FRAME_W)
        self._game_frame.setFixedHeight(FRAME_H)
        self._game_frame.setObjectName(u"game_frame")
        self._game_frame.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self._game_frame.sizePolicy().hasHeightForWidth())
        self._game_frame.setSizePolicy(sizePolicy1)

        self.ui.game_gridLayout.addWidget(self._game_frame, 2, 0, 1, 6)

        self._lenta_frame = ScrolledTriangleFrame(
            self._img_path,
            size_block_w=self._size_block_w, size_block_h=self._size_block_h,
            signal_sender_on_scroll=signal_sender_on_scroll,
            game_config=self._game_config
        )
        self._lenta_frame.setObjectName(u"_lenta_frame")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self._lenta_frame.sizePolicy().hasHeightForWidth())
        self._lenta_frame.setSizePolicy(sizePolicy2)
        self._lenta_frame.setMinimumSize(QSize(0, 100))

        scrollArea = QScrollArea()
        scrollArea.setBackgroundRole(QPalette.Dark)
        scrollArea.setWidgetResizable(True)
        scrollArea.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        scrollArea.setWidget(self._lenta_frame)
        puzz_h = FRAME_H // self._size_block_h
        puzz_scroll_h = puzz_h + 20
        scrollArea.setFixedWidth(FRAME_W)
        scrollArea.setFixedHeight(puzz_scroll_h)

        self.ui.score_value_label.setText(str(self._start_score))
        self.ui.game_gridLayout.addWidget(scrollArea, 3, 0, 1, 6)

        self.start_game()
