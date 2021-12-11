import sys

from PySide6.QtWidgets import QApplication
from puzzle.common.resizable_main_window import ResizableMainWindow
from puzzle.auth import AuthRegController


def main():
    app = QApplication(sys.argv)
    ex = ResizableMainWindow(AuthRegController, allow_exit_button=True)

    sys.exit(app.exec())


if __name__ == "__main__":
    main()