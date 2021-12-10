from PySide6.QtWidgets import QWidget, QFileDialog, QMessageBox

from puzzle.common.qmess_boxes import return_qmess_box_connect_db_error
from .add_image import Ui_Form
from puzzle.database import DatabaseController
from ..utils import SignalAddImage
from puzzle.utils import check_image_content


class QAddImageWidget(QWidget):

    def __init__(self, signal_add_image: SignalAddImage):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.signal_add_image = signal_add_image
        self.ui.save_pushButton.clicked.connect(self.clicked_save)
        self.ui.choose_pushButton.clicked.connect(self.folder_view)
        self._qmess_box: QMessageBox = None

    def folder_view(self):
        dir = QFileDialog.getOpenFileName(
            self, "Choose image", "D:/", "Images (*.png)"
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
                self._qmess_box = return_qmess_box_connect_db_error()
                self._qmess_box.show()
                return

            qmess_box = QMessageBox()
            qmess_box.setText("Изображение успешно добавлено.")
            qmess_box.setWindowTitle("Результат добавления")
            qmess_box.setIcon(QMessageBox.Icon.Information)
            qmess_box.show()
            self._qmess_box = qmess_box

            self.signal_add_image.add.emit()
        else:
            # Bad img
            qmess_box = QMessageBox()
            qmess_box.setText("Изображение невозможно добавить\nНеправильный путь или изображение поврежденно.")
            qmess_box.setWindowTitle("Результат добавления")
            qmess_box.setIcon(QMessageBox.Icon.Critical)
            qmess_box.show()

