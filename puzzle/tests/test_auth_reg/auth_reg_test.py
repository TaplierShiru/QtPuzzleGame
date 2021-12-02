import sys

from PySide6.QtWidgets import QMainWindow, QApplication

from puzzle.auth import AuthRegController


class ExampleApp(QMainWindow):

    def __init__(self):
        super().__init__()

        self._test_widget = AuthRegController()
        self.initUI()

    def initUI(self):
        self.setCentralWidget(self._test_widget)
        self.resize(600, 500)
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
