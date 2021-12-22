from puzzle.auth import AuthRegController
from puzzle.common.resizable_main_window import ResizableMainWindowInitBase, ResizableMainWindow


class AuthController:

    AUTH_WIDGET: ResizableMainWindowInitBase = None

    @staticmethod
    def init_auth_widget():
        AuthController.AUTH_WIDGET = ResizableMainWindow(AuthRegController, allow_exit_button=True)
        AuthController.AUTH_WIDGET.show()
