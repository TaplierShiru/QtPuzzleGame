import glob
from typing import Tuple, List

from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QWidget, QLabel, QSizePolicy, QMessageBox

from .gallery import Ui_Form
from .utils import SignalAddImage
from .add_image_widget import QAddImageWidget

from puzzle.common.back_to_menu import BackToMenu
from puzzle.common.signals import SignalSenderBackToMenu, SignalSenderPicked, SignalSenderPreview
from puzzle.common.custom_qlabels import QLabelPickedAndPreviewImage
from puzzle.common.preview_widget import QPreviewWidget
from puzzle.common.qmess_boxes import return_qmess_box_connect_db_error
from puzzle.database import DatabaseController
from ...database.tables import Image


class QGalleryWidget(QWidget, BackToMenu):

    MAXIMUM_COLUMN = 3
    SIZE_WINDOW_W = 500
    SIZE_WINDOW_H = 400

    def __init__(self, signal_back_to_menu: SignalSenderBackToMenu):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setup_back_to_menu_signal(signal_back_to_menu=signal_back_to_menu)
        self.ui.scrollAreaWidgetContents.setLayout(self.ui.image_gridLayout)
        # Additional params
        self.choosen_image_indx = -1
        self.grid_raw = 0
        self.grid_column = 0
        self._qmess_box: QMessageBox = None
        self.pixmap_images_list: List[QLabelPickedAndPreviewImage] = []
        self.ui.image_gridLayout.setSpacing(10)
        self.setLayout(self.ui.gallery_gridLayout)
        # Buttons
        self.ui.delete_pushButton.clicked.connect(self.delete_image)
        self.ui.back_pushButton.clicked.connect(self.emit_signal_back_to_menu)
        self.ui.add_pushButton.clicked.connect(self.add_image_button_clicked)
        # Signal
        self.signal_picked = SignalSenderPicked()
        self.signal_add_image = SignalAddImage()
        self.signal_preview = SignalSenderPreview()
        self.signal_preview.preview.connect(self.preview_image)
        self.signal_add_image.add.connect(self.update)
        self.signal_picked.signal.connect(self.choose_image)
        self.update()

    def add_image(self, path_to_img: str, img_id: int, img_name: str):
        pixmap = self.create_qlabel_w_pixmap(path_to_img, img_id=img_id, img_name=img_name, indx=len(self.pixmap_images_list))
        self.pixmap_images_list.append(pixmap)
        self.ui.image_gridLayout.addWidget(
            pixmap,
            self.grid_raw, self.grid_column, Qt.AlignLeft
        )
        self.grid_column += 1
        if self.grid_column == QGalleryWidget.MAXIMUM_COLUMN:
            self.grid_column = 0
            self.grid_raw += 1

    def create_qlabel_w_pixmap(self, path_to_img: str, img_id: int, img_name: str, indx=0) -> QLabelPickedAndPreviewImage:
        return QLabelPickedAndPreviewImage(
            indx=indx, path_to_img=path_to_img, img_id=img_id, img_name=img_name,
            signal_sender_picked=self.signal_picked, signal_preview=self.signal_preview
        )

    def add_list_images(self, imgs_data_list: List[Image]):
        for img_s in imgs_data_list:
            self.add_image(img_s.image_path, img_id=img_s.id, img_name=img_s.get_img_name())

    def delete_image(self):
        print(self.choosen_image_indx)
        if self.choosen_image_indx == -1:
            return
        # TODO: Send message to Database in order to delete img
        print('idx delete: ', self.pixmap_images_list[self.choosen_image_indx].img_id)
        result = DatabaseController.remove_img(self.pixmap_images_list[self.choosen_image_indx].img_id)

        if not result:
            self._qmess_box = return_qmess_box_connect_db_error()
            self._qmess_box.show()
            return

        # After deletion - we choose nothing (-1)
        self.choosen_image_indx = -1
        self.update()
        print('-----------------')

    def choose_image(self, indx: int):
        if self.choosen_image_indx != -1:
            self.pixmap_images_list[self.choosen_image_indx].switch_effect()
        self.choosen_image_indx = indx
        print('Choose: ', indx, ' id: ', self.pixmap_images_list[self.choosen_image_indx].img_id)

    def preview_image(self, indx: int):
        print('preview: ', indx)
        img_path, name_img = (
            self.pixmap_images_list[indx].path_to_img,
            self.pixmap_images_list[indx].img_name
        )
        preview_widget = QPreviewWidget(path_to_image=img_path, image_name=name_img)
        preview_widget.show()
        self.preview_widget = preview_widget

    def add_image_button_clicked(self):
        add_image_widget = QAddImageWidget(self.signal_add_image)
        self.add_image_widget = add_image_widget
        self.add_image_widget.show()

    def update(self) -> None:
        super().update()
        # Clear grid of images
        for _ in range(len(self.pixmap_images_list)):
            item = self.ui.image_gridLayout.takeAt(0)
            widget = item.widget()
            widget.hide()
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
        imgs_data_list = DatabaseController.take_all_imgs()

        if imgs_data_list is None:
            self._qmess_box = return_qmess_box_connect_db_error()
            self._qmess_box.show()
        else:
            self.add_list_images(imgs_data_list)
