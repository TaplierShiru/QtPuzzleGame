from PySide6.QtGui import QPixmap, Qt
from PySide6.QtWidgets import QWidget, QMessageBox

from .create_game import Ui_CreateGame
from puzzle.common.back_to_menu import BackToMenu
from puzzle.utils import (DIFFIC_LIST, cut_image_into_rectangles, cut_image_into_triangles,
                          shuffle_rectangle_peases, shuffle_triangle_peases, merge_from_rectangles,
                          TRIANGLE_PUZZLES, RECTANGLE_PUZZLES, merge_from_triangles)
from puzzle.common.signals import SignalSenderBackToMenu, SignalSenderChooseImage
from puzzle.common.choose_image import QChooseImageWidget

from puzzle.database import DatabaseController
from PIL import Image, ImageQt
import numpy as np

from ...common.qmess_boxes import return_qmess_box_connect_db_error


class QCreateGameWidget(QWidget, BackToMenu):

    SIZE_LABEL = (200, 200)
    SIZE_WINDOW_W = 600
    SIZE_WINDOW_H = 300

    def __init__(self, signal_back_to_menu: SignalSenderBackToMenu):
        super().__init__()
        self.ui = Ui_CreateGame()
        self.ui.setupUi(self)
        self.setup_back_to_menu_signal(signal_back_to_menu=signal_back_to_menu)

        self.ui.shuffle_image_label_placeholder.setFixedWidth(self.SIZE_LABEL[1])
        self.ui.shuffle_image_label_placeholder.setFixedHeight(self.SIZE_LABEL[0])

        self.ui.source_image_label_placeholder.setFixedWidth(self.SIZE_LABEL[1])
        self.ui.source_image_label_placeholder.setFixedHeight(self.SIZE_LABEL[0])

        # Buttons
        self.ui.back_pushButton.clicked.connect(self.emit_signal_back_to_menu)
        self.ui.choose_image_pushButton.clicked.connect(self.clicked_choose_image)
        self.ui.shuffle_pushButton.clicked.connect(self.clicked_shuffle_button)
        self.ui.save_pushButton.clicked.connect(self.clicked_save_button)
        # Signals
        self.signal_choose_img = SignalSenderChooseImage()
        self.signal_choose_img.signal.connect(self.update_source_image)

        self.ui.diff_comboBox.addItems(DIFFIC_LIST)
        self.ui.diff_comboBox.currentIndexChanged.connect(self.changed_diff)
        self.ui.diff_comboBox.setCurrentIndex(0)
        self.setLayout(self.ui.create_game_gridLayout)

        # Additional variables
        self.__id_img: int = None
        self.__path_to_img: str = None
        self.__shuffle_indx: list = None
        self.__type_puzzle: str = None
        self.__qmess_box: QMessageBox = None
        self._choose_image_widget: QChooseImageWidget = None

    def clicked_choose_image(self):
        self._choose_image_widget = QChooseImageWidget(self.signal_choose_img)
        self._choose_image_widget.show()

    def clicked_save_button(self):
        result = DatabaseController.add_new_game(
            id_img=self.__id_img, indx_position=self.__shuffle_indx,
            diff=self.ui.diff_comboBox.currentText()
        )

        if not result:
            self.__qmess_box = return_qmess_box_connect_db_error()
            self.__qmess_box.show()
            return

    def clicked_shuffle_button(self):
        if self.__id_img is not None:
            self._shuffle_image()
            self.update()

    def changed_diff(self, indx: int):
        self.ui.diff_comboBox.setCurrentIndex(indx)

        if self.__id_img is not None:
            self._shuffle_image()
            self.update()

    def update_source_image(self, id_img: int):
        path_to_img = DatabaseController.get_img(id_img)

        if path_to_img is None:
            self.__qmess_box = return_qmess_box_connect_db_error()
            self.__qmess_box.show()
            return

        self.__id_img = id_img
        self.__path_to_img = path_to_img
        # Source
        pixmap = QPixmap(path_to_img)
        pixmap = pixmap.scaled(self.SIZE_LABEL[1], self.SIZE_LABEL[1], aspectMode=Qt.IgnoreAspectRatio)
        self.ui.source_image_label_placeholder.setPixmap(pixmap)
        # Shuffle
        self._shuffle_image()
        self.update()

    def _shuffle_image(self):
        frag_h, frag_w, type_build, type_puzzle = DatabaseController.get_diff_params(
            self.ui.diff_comboBox.currentText()
        )

        if frag_h is None:
            self.__qmess_box = return_qmess_box_connect_db_error()
            self.__qmess_box.show()
            return

        frag_h, frag_w = int(frag_h), int(frag_w)
        self.__type_puzzle = type_puzzle
        source_image = np.array(Image.open(self.__path_to_img))
        if type_puzzle == RECTANGLE_PUZZLES:
            peases_of_image = cut_image_into_rectangles(source_image, size_block_w=frag_w, size_block_h=frag_h, map_to_qimage=False)
            shuffled_peases, indx_shuffled = shuffle_rectangle_peases(peases_of_image)
            combined_image = merge_from_rectangles(shuffled_peases, size_block_w=frag_w, size_block_h=frag_h)
            qimage = ImageQt.ImageQt(Image.fromarray(combined_image))
            self.__shuffle_indx = indx_shuffled
        else:
            triangles_top_list, triangles_bottom_list, mask = cut_image_into_triangles(source_image, size_block_w=frag_w, size_block_h=frag_h, map_to_qimage=False)
            (shuffled_triangle_top_list, indx_top_shuffled), (shuffled_triangle_bottom_list, indx_bottom_shuffled) = shuffle_triangle_peases(
                triangle_top_list=triangles_top_list, triangle_bottom_list=triangles_bottom_list
            )
            combined_image = merge_from_triangles(
                triangle_top_list=shuffled_triangle_top_list, triangle_bottom_list=shuffled_triangle_bottom_list,
                mask=mask, size_block_w=frag_w, size_block_h=frag_h
            )
            qimage = ImageQt.ImageQt(Image.fromarray(combined_image))
            self.__shuffle_indx = (indx_top_shuffled, indx_bottom_shuffled)
        pixmap = QPixmap(qimage)
        pixmap = pixmap.scaled(self.SIZE_LABEL[1], self.SIZE_LABEL[1], aspectMode=Qt.IgnoreAspectRatio)
        self.ui.shuffle_image_label_placeholder.setPixmap(pixmap)

