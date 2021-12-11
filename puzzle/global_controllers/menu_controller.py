from typing import Union, Dict
from puzzle.common.resizable_main_window import ResizableMainWindow, ResizableMainWindowInitBase


class MenuController:
    NAME2CLASS: Dict[str, ResizableMainWindowInitBase] = {}

    @staticmethod
    def add_new_menu(menu_class, role: str):
        MenuController.NAME2CLASS[str(role)] = menu_class

    @staticmethod
    def get_widget_by_role(user_login: str, role: str) -> ResizableMainWindow:
        taken_class = MenuController.NAME2CLASS.get(str(role))
        if taken_class is None:
            return
        init_widget = ResizableMainWindow(
            resizable_init=taken_class, allow_exit_button=False, user_login=user_login
        )
        return init_widget
