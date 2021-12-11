import sys

from PySide6.QtWidgets import QApplication
from puzzle.common.resizable_main_window import ResizableMainWindow
from puzzle.user.user_menu_controller import UserMenuController


def main():
    app = QApplication(sys.argv)
    ex = UserMenuController.init_widget_with_resizable_form(user_login='admin')

    sys.exit(app.exec())


if __name__ == "__main__":
    main()