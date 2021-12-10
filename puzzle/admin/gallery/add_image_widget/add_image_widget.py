from PySide6.QtWidgets import QWidget, QFileDialog, QMessageBox

from puzzle.common.qmess_boxes import return_qmess_box_connect_db_error
from .add_image import Ui_AddImage
from puzzle.database import DatabaseController
from ..utils import SignalAddImage
from puzzle.utils import check_image_content


class QAddImageWidget(QWidget):

    def __init__(self, signal_add_image: SignalAddImage):
        super().__init__()
        self.ui = Ui_AddImage()
        self.ui.setupUi(self)
        self.__signal_add_image = signal_add_image
        self.ui.save_pushButton.clicked.connect(self.clicked_save)
        self.ui.choose_pushButton.clicked.connect(self.folder_view)
        self.__qmess_box: QMessageBox = None

    def folder_view(self):
        dir = QFileDialog.getOpenFileName(
            self, "Choose image", "", "Images (*.png)"
        )
        if dir is not None and len(dir[0]) != 0:
            self.ui.path_lineEdit.setText(dir[0])
            self.ui.name_image_lineEdit.setText(dir[0].split('/')[-1].split('.')[0])

    def clicked_save(self):
        path_img = self.ui.path_lineEdit.text()
        name_img = self.ui.name_image_lineEdit.text()
        # Check image
        if check_image_content(path_img):
            # Good img
            result = DatabaseController.add_image(path_img, name_img)

            if not result:
                self.__qmess_box = return_qmess_box_connect_db_error()
                self.__qmess_box.show()
                return
            self.__qmess_box = self.__generate_qmess_box(
                "Изображение успешно добавлено.",
                QMessageBox.Icon.Information
            )
            self.__signal_add_image.add.emit()
        else:
            # Bad img
            self.__qmess_box = self.__generate_qmess_box(
                "Изображение невозможно добавить\n" +\
                "Неправильный путь или изображение поврежденно.",
                QMessageBox.Icon.Critical
            )
        self.__qmess_box.show()

    def __generate_qmess_box(self, text: str, icon: QMessageBox.Icon) -> QMessageBox:
        qmess_box = QMessageBox()
        qmess_box.setText(text)
        qmess_box.setWindowTitle("Результат добавления")
        qmess_box.setIcon(icon)
        return qmess_box

