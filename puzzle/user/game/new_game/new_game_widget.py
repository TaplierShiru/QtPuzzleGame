import traceback

from PySide6.QtWidgets import QWidget, QMessageBox

from puzzle.common.choose_image import QChooseImageWidget
from puzzle.database import DatabaseController
from puzzle.common.back_to_menu import BackToMenu
from puzzle.common.signals import SignalSenderBackToMenu, SignalSenderChooseImage
from puzzle.utils import DIFFIC_LIST, TYPE_SCORE, BUILD_AREA, BUILD_LENTA, TRIANGLE_PUZZLES, RECTANGLE_PUZZLES
from puzzle.user.game.new_game.puzzle_game.build_game_widget_controller import BuildGameWidgetController
from .new_game import Ui_Form


class QNewGameWidget(QWidget, BackToMenu):

    SIZE_WINDOW_W = 200
    SIZE_WINDOW_H = 200

    def __init__(self, user_login: str, signal_back_to_menu: SignalSenderBackToMenu):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self._user_login = user_login
        self._qmess_box = None
        self.setup_back_to_menu_signal(signal_back_to_menu=signal_back_to_menu)

        # Buttons
        self.ui.back_to_menu_pushButton.clicked.connect(self.emit_signal_back_to_menu)
        self.ui.choose_image_pushButton.clicked.connect(self.clicked_choose_image)
        self.ui.start_game_pushButton.clicked.connect(self.clicked_start_game)
        # Combo boxes
        self.ui.level_diff_comboBox.addItems(DIFFIC_LIST)
        self.ui.type_res_comboBox.addItems(TYPE_SCORE)
        # Signals
        self.signal_choose_img = SignalSenderChooseImage()
        self.signal_choose_img.signal.connect(self.update_choosen_img)
        # Other...
        self.ui.choosen_image_lineEdit.setReadOnly(True)
        self.setLayout(self.ui.new_game_gridLayout)

    def clicked_choose_image(self, event):
        self.choose_image_widget = QChooseImageWidget(self.signal_choose_img, user_type=True, diff=self.ui.level_diff_comboBox.currentText())
        self.choose_image_widget.show()

    def update_choosen_img(self, img_id: str):
        self._choosen_id = img_id
        img_name = DatabaseController.get_img_name(img_id)
        self.ui.choosen_image_lineEdit.setText(img_name)

    def clicked_start_game(self):
        diff = self.ui.level_diff_comboBox.currentText()
        score_type = self.ui.type_res_comboBox.currentText()
        print(f"Diff:{diff} type score:{score_type}")
        # Create widget game...
        try:
            self._widget_game = BuildGameWidgetController.build_widget(
                diff=diff, score_type=score_type, user_login=self._user_login,
                id_img=self._choosen_id
            )
            self._widget_game.show()
        except Exception:
            qmess_box = QMessageBox()
            qmess_box.setText("Что-то пошло не так...")
            qmess_box.setWindowTitle("Ошибка")
            qmess_box.setIcon(QMessageBox.Icon.Warning)
            qmess_box.show()
            self._qmess_box = qmess_box
            print(traceback.print_exc())
