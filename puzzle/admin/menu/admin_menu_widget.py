import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget
from .admin_menu import Ui_AdminMenu
from puzzle.common.signals import SignalSenderChangePage
from puzzle.admin.utils import (SIGNAL_ABOUT_CREATORS_INDX, SIGNAL_GALLERY_INDX, SIGNAL_SETUP_LEVEL_INDX,
                                SIGNAL_CREATE_GAME_INDX)


class QAdminMenuWidget(QWidget):

    SIZE_WINDOW_W = 200
    SIZE_WINDOW_H = 200

    def __init__(self, signal_change_page: SignalSenderChangePage):
        super().__init__()
        self.ui = Ui_AdminMenu()
        self.ui.setupUi(self)
        self.__signal_change_page = signal_change_page
        # Buttons
        self.ui.gallery_pushButton.clicked.connect(self.clicked_gallery)
        self.ui.level_control_pushButton.clicked.connect(self.clicked_setup_level)
        self.ui.create_game_pushButton.clicked.connect(self.clicked_create_game)
        self.ui.about_creators_pushButton.clicked.connect(self.clicked_about_creators)
        self.ui.exit_pushButton.clicked.connect(self.clicked_exit)
        # Other settings
        self.ui.menu_vlayout.setAlignment(Qt.AlignHCenter)
        self.setLayout(self.ui.menu_vlayout)

    def clicked_about_creators(self):
        self.__signal_change_page.signal.emit(SIGNAL_ABOUT_CREATORS_INDX)

    def clicked_gallery(self):
        self.__signal_change_page.signal.emit(SIGNAL_GALLERY_INDX)

    def clicked_setup_level(self):
        self.__signal_change_page.signal.emit(SIGNAL_SETUP_LEVEL_INDX)

    def clicked_create_game(self):
        self.__signal_change_page.signal.emit(SIGNAL_CREATE_GAME_INDX)

    def clicked_exit(self):
        self.close()
        self.__signal_change_page.signal.emit(-1)

