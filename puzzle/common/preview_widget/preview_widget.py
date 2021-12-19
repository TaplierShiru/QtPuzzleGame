import os

from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QWidget, QMessageBox
from puzzle.common.qmess_boxes import return_qmess_box
from puzzle.database import DatabaseController
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

        if not os.path.isfile(path_to_image):
            self.__qmess_box = return_qmess_box(
                title='Ошибка', text='Изображение не было найдено.',
                icon=QMessageBox.Icon.Critical
            )
            self.__qmess_box.show()
            DatabaseController.clear_temp()
        self.setWindowFlags(Qt.CustomizeWindowHint | Qt.WindowCloseButtonHint)

