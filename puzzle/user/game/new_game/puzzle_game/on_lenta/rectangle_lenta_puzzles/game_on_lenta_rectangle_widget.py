from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import  QPalette


from PySide6.QtWidgets import QWidget, QScrollArea, QAbstractScrollArea, QSizePolicy

from puzzle import DatabaseController
from puzzle.user.game.new_game.puzzle_game.common.signals import SignalSenderSendDataImage

from .game_on_lenta_rectangle_ui import Ui_Form
from .qlenta_area_widget import ScrolledRectangleFrame
from .qfield_frame import CustomOnLentaRectangleFrame

from puzzle.utils import FRAME_H, FRAME_W


class PuzzleGameOnLentaRectangleWidget(QWidget):

    def __init__(self, id_img: str, diff: str, size_block_w: int, size_block_h: int):
        super().__init__()
        self._id_img = id_img
        self._diff = diff
        self._img_path = DatabaseController.get_img(id_img)

        self.ui = Ui_Form()
        self.ui.setupUi(self)
        game_config = DatabaseController.get_game_config(diff=diff, id_img=id_img)
        signal_sender_on_scroll = SignalSenderSendDataImage()

        self.game_widget = CustomOnLentaRectangleFrame(
            self._img_path,
            size_block_w=size_block_w, size_block_h=size_block_h,
            signal_sender_on_scroll=signal_sender_on_scroll,
            prestart_position=None
        )
        self.game_widget.setFixedWidth(FRAME_W)
        self.game_widget.setFixedHeight(FRAME_H)
        self.game_widget.setObjectName(u"game_widget")
        self.game_widget.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.game_widget.sizePolicy().hasHeightForWidth())
        self.game_widget.setSizePolicy(sizePolicy1)

        self.ui.game_gridLayout.addWidget(self.game_widget, 2, 0, 1, 6)

        self.lenta_widget = ScrolledRectangleFrame(
            self._img_path,
            size_block_w=size_block_w, size_block_h=size_block_h,
            signal_sender_on_scroll=signal_sender_on_scroll,
            prestart_position=None
        )
        self.lenta_widget.setObjectName(u"lenta_widget")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.lenta_widget.sizePolicy().hasHeightForWidth())
        self.lenta_widget.setSizePolicy(sizePolicy2)
        self.lenta_widget.setMinimumSize(QSize(0, 100))

        scrollArea = QScrollArea()
        scrollArea.setBackgroundRole(QPalette.Dark)
        scrollArea.setWidgetResizable(True)
        scrollArea.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        scrollArea.setWidget(self.lenta_widget)
        puzz_h = FRAME_H // size_block_h
        puzz_scroll_h = puzz_h + 20
        scrollArea.setFixedWidth(FRAME_W)
        scrollArea.setFixedHeight(puzz_scroll_h)

        self.ui.game_gridLayout.addWidget(scrollArea, 3, 0, 1, 6)
        self.setLayout(self.ui.game_gridLayout)

