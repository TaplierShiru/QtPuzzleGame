from puzzle.common.resizable_main_window import ResizableMainWindowInitBase
from puzzle.common.signals.signal_change_size_form import SignalSenderChangeSizeWidget


class MenuControllerBase(ResizableMainWindowInitBase):

    def __init__(self, user_login: str, signal_change_size: SignalSenderChangeSizeWidget, **kwargs):
        super().__init__(signal_change_size=signal_change_size)
        self.__user_login = user_login



