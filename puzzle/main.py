import sys

from PySide6.QtWidgets import QApplication
from puzzle.global_controllers.auth_controller import AuthController


def main():
    app = QApplication(sys.argv)
    ex = AuthController.init_auth_widget()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()