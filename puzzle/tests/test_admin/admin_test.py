import sys

from PySide6.QtWidgets import QApplication
from puzzle.common.resizable_main_window import ResizableMainWindow
from puzzle.admin.administrator_menu_controller import AdministratorMenuController


def main():
    app = QApplication(sys.argv)
    ex = ResizableMainWindow(AdministratorMenuController)

    sys.exit(app.exec())


if __name__ == "__main__":
    main()