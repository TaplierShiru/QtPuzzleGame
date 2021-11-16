from PySide6.QtWidgets import QWidget, QFileDialog
from .add_image import Ui_Form
from puzzle.database import DatabaseController
from ..utils import SignalAddImage


class QAddImageWidget(QWidget):

    def __init__(self, signal_add_image: SignalAddImage):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.signal_add_image = signal_add_image
        self.ui.save_pushButton.clicked.connect(self.clicked_save)
        self.ui.choose_pushButton.clicked.connect(self.folder_view)

    def folder_view(self):
        dir = QFileDialog.getOpenFileName(
            self, "Choose image", "D:/", "Images (*.png)"
        )
        if dir is not None and len(dir[0]) != 0:
            self.ui.path_lineEdit.setText(dir[0])
            self.ui.name_image_lineEdit.setText(dir[0].split('/')[-1])

    def clicked_save(self):
        path_img = self.ui.path_lineEdit.text()
        name_img = self.ui.path_label.text()
        # TODO: Check errors and type of image
        DatabaseController.add_image(path_img, name_img)
        self.signal_add_image.add.emit()

