from PySide6.QtWidgets import QWidget, QStackedWidget, QGridLayout

from .menu import QAdminMenuWidget
from .about_creators import QAboutCreatorsWidget
from .gallery import QGalleryWidget
from .create_game import QCreateGameWidget
from .setup_level import QSetupLevelWidget
from .core.signals import SignalSenderBackToMenu, SignalSenderChangePage
from .constants import (SIGNAL_ABOUT_CREATORS_INDX, SIGNAL_GALLERY_INDX, SIGNAL_SETUP_LEVEL_INDX,
                        SIGNAL_MENU_INDX, SIGNAL_CREATE_GAME_INDX)


class MenuController(QWidget):

    def __init__(self):
        super().__init__()
        # Setup signal if need back to menu
        self.signal_back_to_menu = SignalSenderBackToMenu()
        self.signal_back_to_menu.signal.connect(lambda: self._stacked_widget.setCurrentIndex(0))

        self.signal_change_page = SignalSenderChangePage()
        self.signal_change_page.signal.connect(self.change_page)
        self.setupUI()

    def setupUI(self):
        grid = QGridLayout()
        stacked_widget = QStackedWidget()
        # Init menu, 0
        menu = QAdminMenuWidget(signal_change_page=self.signal_change_page)
        stacked_widget.addWidget(menu)
        # Init gallery, 1
        gallery = QGalleryWidget(signal_back_to_menu=self.signal_back_to_menu)
        stacked_widget.addWidget(gallery)
        # Init change level, 2
        setup_level = QSetupLevelWidget(signal_back_to_menu=self.signal_back_to_menu)
        stacked_widget.addWidget(setup_level)
        # Init create game, 3
        create_game = QCreateGameWidget(signal_back_to_menu=self.signal_back_to_menu)
        stacked_widget.addWidget(create_game)
        # Init about system, 4
        # Init about creators, 5
        about_creators = QAboutCreatorsWidget(signal_back_to_menu=self.signal_back_to_menu)
        stacked_widget.addWidget(about_creators)

        self.num_to_widget_dict = {
            str(SIGNAL_MENU_INDX)           : menu,
            str(SIGNAL_GALLERY_INDX)        : gallery,
            str(SIGNAL_SETUP_LEVEL_INDX)    : setup_level,
            str(SIGNAL_CREATE_GAME_INDX)    : create_game,
            str(SIGNAL_ABOUT_CREATORS_INDX) : about_creators,
        }
        stacked_widget.setCurrentIndex(0)
        self._stacked_widget = stacked_widget
        grid.addWidget(stacked_widget, 0, 0)
        self.setLayout(grid)

    def change_page(self, target_page: int):
        self.num_to_widget_dict[str(target_page)].update()
        self._stacked_widget.setCurrentIndex(target_page)

