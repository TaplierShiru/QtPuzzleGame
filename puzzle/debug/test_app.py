import sys

import PySide6
from PySide6.QtWidgets import QMainWindow, QApplication, QLabel


class ExampleApp(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self._hello_label = QLabel("Hello world!")
        self.setCentralWidget(self._hello_label)
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