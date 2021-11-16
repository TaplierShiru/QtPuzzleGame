import sys

import PySide6
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow, QApplication, QLabel, QWidget, QGridLayout
from test_stacked import Ui_Form


class QTestWidget(QWidget, Ui_Form):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        grid = QGridLayout()
        grid.addWidget(self.stackedWidget, 0, 0)
        self.stackedWidget.setCurrentIndex(0)
        self.menu_page.setLayout(self.menu_vlayout)
        self.menu_vlayout.setAlignment(Qt.AlignHCenter)
        self.gallery_page.setLayout(self.gallery_gridLayout)
        self.setLayout(grid)


class ExampleApp(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self._test_widget = QTestWidget()
        self.setCentralWidget(self._test_widget)
        self.resize(400, 200)
        self.center()

        self.setWindowTitle('Center window')
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = self.screen().geometry().center()
        qr.moveCenter(cp)

        self.move(qr.topLeft())


def main():
    app = QApplication(sys.argv)
    ex = ExampleApp()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()