from puzzle.common.signals import SignalSenderBackToMenu


class BackToMenu:

    def __init__(self, *args):
        self.signal_back_to_menu = None

    def setup_back_to_menu_signal(self, signal_back_to_menu: SignalSenderBackToMenu):
        self.signal_back_to_menu = signal_back_to_menu

    def emit_signal_back_to_menu(self):
        assert self.signal_back_to_menu is not None
        self.signal_back_to_menu.signal.emit()

