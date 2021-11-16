import glob

from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QWidget, QLabel, QSizePolicy

from .gallery import Ui_Form
from ..core import BackToMenu, QPreviewWidget, QLabelPickedImage
from .utils import SignalAddImage, SignalGalleryPreview
from .add_image_widget import QAddImageWidget

from puzzle.database import DatabaseController
from ..core.signals import SignalSenderBackToMenu


class QGalleryWidget(QWidget, BackToMenu):

    MAXIMUM_COLUMN = 3

    def __init__(self, signal_back_to_menu: SignalSenderBackToMenu, ui_form = None):
        super().__init__()
        if ui_form is None:
            self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setup_back_to_menu_signal(signal_back_to_menu=signal_back_to_menu)
        self.ui.scrollAreaWidgetContents.setLayout(self.ui.image_gridLayout)
        # Additional params
        self.choosen_image_indx = -1
        self.grid_raw = 0
        self.grid_column = 0
        self.pixmap_images_list = []
        self.ui.image_gridLayout.setSpacing(10)
        self.setLayout(self.ui.gallery_gridLayout)
        # Buttons
        self.ui.delete_pushButton.clicked.connect(self.delete_image)
        self.ui.back_pushButton.clicked.connect(self.emit_signal_back_to_menu)
        self.ui.add_pushButton.clicked.connect(self.add_image_button_clicked)
        # Signal
        self.signal_add_image = SignalAddImage
        self.signal_preview = SignalGalleryPreview()
        self.signal_preview.preview.connect(self.preview_image)
        self.signal_add_image.add.connect(self.update)
        self.update()

    def add_image(self, path_to_img: str):
        pixmap = self.create_qlabel_w_pixmap(path_to_img, indx=len(self.pixmap_images_list))
        self.pixmap_images_list.append(pixmap)
        self.ui.image_gridLayout.addWidget(
            pixmap,
            self.grid_raw, self.grid_column, Qt.AlignLeft
        )
        self.grid_column += 1
        if self.grid_column == QGalleryWidget.MAXIMUM_COLUMN:
            self.grid_column = 0
            self.grid_raw += 1

    def create_qlabel_w_pixmap(self, path_to_img, indx=0) -> QLabelPickedImage:
        return QLabelPickedImage(indx=indx, path_to_img=path_to_img)

    def add_list_images(self, path_to_img_list: list):
        for path_s in path_to_img_list:
            self.add_image(path_s)

    def delete_image(self):
        if self.choosen_image_indx == -1:
            return
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
        print('size array: ', len(self.pixmap_images_list))
        self.pixmap_images_list[self.choosen_image_indx].hide()
        del self.pixmap_images_list[self.choosen_image_indx]
        is_last = self.choosen_image_indx != len(self.pixmap_images_list)-1
        #self.ui.image_gridLayout.removeWidget(self.pixmap_images_list[-1])
        #item = self.ui.image_gridLayout.takeAt(len(self.pixmap_images_list)-1)
        #widget = item.widget()
        #self.ui.image_gridLayout.removeItem(item)
        #if widget is not None:
        #    del widget
        # Append all other widgets
        indx_shift = 0
        for indx in range(len(self.pixmap_images_list)):
            if indx == self.choosen_image_indx:
                indx_shift = 1
                print('was deleted indx: ', indx)
            self.pixmap_images_list[indx].indx -= indx_shift
            self.ui.image_gridLayout.addWidget(
                self.pixmap_images_list[indx],
                self.grid_raw, self.grid_column, Qt.AlignLeft
            )
            self.grid_column += 1
            if self.grid_column == QGalleryWidget.MAXIMUM_COLUMN:
                self.grid_column = 0
                self.grid_raw += 1
        print('Delete: ', self.choosen_image_indx)
        # After deletion - we choose nothing (-1)
        self.choosen_image_indx = -1
        self.update()
        print('-----------------')

    def choose_image(self, indx: int):
        if self.choosen_image_indx != -1:
            self.pixmap_images_list[self.choosen_image_indx].switch_effect()
        print('Choose: ', indx)
        self.choosen_image_indx = indx

    def preview_image(self, indx: int):
        print('preview: ', indx)
        img_path = self.pixmap_images_list[indx].path_to_img
        preview_widget = QPreviewWidget(path_to_image=img_path, image_name='test')
        preview_widget.show()
        self.preview_widget = preview_widget

    def add_image_button_clicked(self):
        add_image_widget = QAddImageWidget()
        self.add_image_widget = add_image_widget
        self.add_image_widget.show()

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
        imgs_list = DatabaseController.take_all_imgs()
        self.add_list_images(imgs_list)
