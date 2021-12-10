from typing import List, Tuple

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QLabel, QSizePolicy, QMessageBox

from .choose_image import Ui_Form
from puzzle.common.signals import SignalSenderChooseImage, SignalSenderPreview
from puzzle.common.preview_widget import QPreviewWidget
from puzzle.common.custom_qlabels import QLabelPickedAndPreviewImage

from puzzle.database import DatabaseController
from puzzle.common.signals import SignalSenderBackToMenu, SignalSenderPicked
from ..qmess_boxes import return_qmess_box_connect_db_error
from ...database.tables import Image


class QChooseImageWidget(QWidget):

    MAXIMUM_COLUMN = 3

    def __init__(self, signal_choose_image: SignalSenderChooseImage, user_type: bool = False, **kwargs):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.scrollAreaWidgetContents.setLayout(self.ui.image_gridLayout)
        # Additional params
        self._user_type = user_type
        self._kwargs = kwargs

        self.__qmess_box: QMessageBox = None
        self.choosen_image_indx = -1
        self.grid_raw = 0
        self.grid_column = 0
        self.pixmap_images_list: List[QLabelPickedAndPreviewImage] = []
        self.ui.image_gridLayout.setSpacing(10)
        self.setLayout(self.ui.choose_image_gridLayout)
        # Buttons
        self.ui.choose_pushButton.clicked.connect(self.choose_button_clicked)
        # Signal
        self.signal_picked = SignalSenderPicked()
        self.signal_preview = SignalSenderPreview()
        self.signal_choose_image = signal_choose_image
        self.signal_preview.preview.connect(self.preview_image)
        self.signal_picked.signal.connect(self.choose_image)
        self.update()

    def add_image(self, path_to_img: str, img_id: int, image_name: str):
        pixmap = self.create_qlabel_w_pixmap(
            path_to_img, img_id=img_id, image_name=image_name, indx=len(self.pixmap_images_list)
        )
        self.pixmap_images_list.append(pixmap)
        self.ui.image_gridLayout.addWidget(
            pixmap,
            self.grid_raw, self.grid_column, Qt.AlignLeft
        )
        self.grid_column += 1
        if self.grid_column == QChooseImageWidget.MAXIMUM_COLUMN:
            self.grid_column = 0
            self.grid_raw += 1

    def create_qlabel_w_pixmap(
            self, path_to_img: str, img_id: int,
            image_name: str, indx=0) -> QLabelPickedAndPreviewImage:
        return QLabelPickedAndPreviewImage(
            indx=indx, path_to_img=path_to_img, img_id=img_id, img_name=image_name,
            signal_sender_picked=self.signal_picked, signal_preview=self.signal_preview
        )

    def add_list_images(self, img_data_list: List[Image]):
        for img_s in img_data_list:
            self.add_image(img_s.image_path, img_id=img_s.id, image_name=img_s.get_img_name())

    def choose_image(self, indx: int):
        if self.choosen_image_indx != -1:
            self.pixmap_images_list[self.choosen_image_indx].switch_effect()
        self.choosen_image_indx = indx

    def preview_image(self, indx: int):
        img_path = self.pixmap_images_list[indx].path_to_img
        preview_widget = QPreviewWidget(path_to_image=img_path, image_name='test')
        preview_widget.show()
        self.preview_widget = preview_widget

    def choose_button_clicked(self):
        if not self.__check_choosen_img(
                "Ошибка",
                "Ошибка выбора изображения\nИзображение не было выбрано."):
            return

        self.signal_choose_image.signal.emit(self.pixmap_images_list[self.choosen_image_indx].img_id)
        self.close()

    def update(self) -> None:
        super().update()
        # Clear grid of images
        for _ in range(len(self.pixmap_images_list)):
            item = self.ui.image_gridLayout.takeAt(0)
            widget = item.widget()
            self.ui.image_gridLayout.removeItem(item)
            if widget is not None:
                del widget
        # Clear pixmap what we want to delete
        self.grid_column = 0
        self.grid_raw = 0
        # TODO: Load path from DataBase and update it
        # DEBUG
        self.pixmap_images_list = []
        self.choosen_image_indx = -1
        if self._user_type:
            available_games_img_ids = DatabaseController.get_game_imgs(self._kwargs['diff'])

            if available_games_img_ids is None:
                self.__qmess_box = return_qmess_box_connect_db_error()
                self.__qmess_box.show()
                return

            imgs_list = []
            for id_img in available_games_img_ids:
                imgs_list.append(DatabaseController.get_img(id_img, return_as_class=True))
                if imgs_list[-1] is None:
                    self.__qmess_box = return_qmess_box_connect_db_error()
                    self.__qmess_box.show()
                    return
        else:
            imgs_list = DatabaseController.take_all_imgs()

            if imgs_list is None:
                self.__qmess_box = return_qmess_box_connect_db_error()
                self.__qmess_box.show()
                return
        self.add_list_images(imgs_list)

    def __check_choosen_img(self, window_title: str, text: str, icon=QMessageBox.Icon.Warning) -> bool:
        if self.choosen_image_indx == -1:
            qmess_box = QMessageBox()
            qmess_box.setIcon(icon)
            qmess_box.setText(text)
            qmess_box.setWindowTitle(window_title)
            qmess_box.show()
            self.__qmess_box = qmess_box
            return False
        return True