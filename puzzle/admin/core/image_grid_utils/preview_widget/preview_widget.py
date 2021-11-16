from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QWidget
from .preview import Ui_Form


class QPreviewWidget(QWidget):

    def __init__(self, path_to_image: str, image_name: str):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.frame_label.setPixmap(QPixmap(path_to_image))
        self.ui.image_label.setText(image_name)
        self.ui.frame_label.setAlignment(Qt.AlignCenter)

        self.setLayout(self.ui.verticalLayout)

