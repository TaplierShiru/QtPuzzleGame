from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QWidget

from .create_game import Ui_Form
from ..core import BackToMenu
from ..constants import DIFFIC_LIST
from ..core.signals import SignalSenderBackToMenu
from .choose_image import QChooseImageWidget
from .utils import SignalSenderChooseImage

from puzzle.database import DatabaseController


class QCreateGameWidget(QWidget, BackToMenu):

    SIZE_LABEL = (200, 200)

    def __init__(self, signal_back_to_menu: SignalSenderBackToMenu):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setup_back_to_menu_signal(signal_back_to_menu=signal_back_to_menu)

        self.ui.shuffle_image_label_placeholder.setFixedWidth(self.SIZE_LABEL[1])
        self.ui.shuffle_image_label_placeholder.setFixedHeight(self.SIZE_LABEL[0])

        self.ui.source_image_label_placeholder.setFixedWidth(self.SIZE_LABEL[1])
        self.ui.source_image_label_placeholder.setFixedHeight(self.SIZE_LABEL[0])

        # Buttons
        self.ui.back_pushButton.clicked.connect(self.emit_signal_back_to_menu)
        self.ui.choose_image_pushButton.clicked.connect(self.clicked_choose_image)
        self.ui.shuffle_pushButton.clicked.connect(self.clicked_shuffle_button)
        # Signals
        self.signal_choose_img = SignalSenderChooseImage()
        self.signal_choose_img.signal.connect(self.update_source_image)
        self.ui.diff_comboBox.addItems(DIFFIC_LIST)
        self.setLayout(self.ui.create_game_gridLayout)

        # Additional variables
        self.id_img = None
        self.path_to_img = None
        self.shuffle_indx = None

    def clicked_choose_image(self, event):
        self.choose_image_widget = QChooseImageWidget(self.signal_choose_img)
        self.choose_image_widget.show()

    def clicked_shuffle_button(self, event):
        print('shuffle')

    def update_source_image(self, id_img: int):
        print('id: ', id_img)
        path_to_img = DatabaseController.get_img(id_img)
        self.id_img = id_img
        self.path_to_img = path_to_img
        # Source
        pixmap = QPixmap(path_to_img)
        pixmap.scaledToWidth(self.SIZE_LABEL[1])
        pixmap.scaledToHeight(self.SIZE_LABEL[0])
        self.ui.source_image_label_placeholder.setPixmap(pixmap)
        # Shuffle
        pixmap = QPixmap(path_to_img)
        pixmap.scaledToWidth(self.SIZE_LABEL[1])
        pixmap.scaledToHeight(self.SIZE_LABEL[0])
        self.ui.shuffle_image_label_placeholder.setPixmap(pixmap)

