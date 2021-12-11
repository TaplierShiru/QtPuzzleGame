import sys

from PySide6.QtWidgets import QApplication
from puzzle.global_controllers import MenuController
from puzzle.utils import ROLE_USER


def main():
    app = QApplication(sys.argv)
    ex = MenuController.get_widget_by_role(user_login='admin', role=ROLE_USER)
    ex.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()