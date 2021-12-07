import sys

from PySide6.QtWidgets import QApplication
from puzzle.common.resizable_main_window import ResizableMainWindow
from puzzle.user.user_menu_controller import UserMenuController


def main():
    app = QApplication(sys.argv)
    ex = ResizableMainWindow(
        lambda signal_change_size: UserMenuController(user_login="admin", signal_change_size=signal_change_size)
    )

    sys.exit(app.exec())


if __name__ == "__main__":
    main()