import traceback

from PySide6.QtWidgets import QWidget, QMessageBox

from puzzle.common.choose_image import QChooseImageWidget
from puzzle.common.error_box_widget import check_img_exist
from puzzle.common.qmess_boxes import return_qmess_box_connect_db_error
from puzzle.database import DatabaseController
from puzzle.common.back_to_menu import BackToMenu
from puzzle.common.signals import SignalSenderBackToMenu, SignalSenderChooseImage
from puzzle.utils import DIFFIC_LIST, TYPE_SCORE, BUILD_AREA, BUILD_LENTA, TRIANGLE_PUZZLES, RECTANGLE_PUZZLES
from puzzle.user.game.new_game.puzzle_game.build_game_widget_controller import BuildGameWidgetController
from .new_game import Ui_NewGame


class QNewGameWidget(QWidget, BackToMenu):

    SIZE_WINDOW_W = 200
    SIZE_WINDOW_H = 200

    def __init__(self, user_login: str, signal_back_to_menu: SignalSenderBackToMenu):
        super().__init__()
        self.ui = Ui_NewGame()
        self.ui.setupUi(self)
        self.__user_login = user_login
        self.__qmess_box: QMessageBox = None
        self.__choose_image_widget: QChooseImageWidget = None
        self.__widget_game = None
        self.__choosen_id = -1
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
        self.__choose_image_widget = QChooseImageWidget(
            self.signal_choose_img, user_type=True,
            diff=self.ui.level_diff_comboBox.currentText())
        self.__choose_image_widget.show()

    def update_choosen_img(self, img_id: int):
        self.__choosen_id = img_id
        img_name = DatabaseController.get_img_name(img_id)

        if img_name is None:
            self.__qmess_box = return_qmess_box_connect_db_error()
            self.__qmess_box.show()
            return

        self.ui.choosen_image_lineEdit.setText(img_name)

    def clicked_start_game(self):
        if self.__choosen_id == -1:
            # Show box that user do not choose any image for game
            qmess_box = QMessageBox()
            qmess_box.setText("Изображение для игры не выбрано.")
            qmess_box.setWindowTitle("Ошибка начала игры")
            qmess_box.setIcon(QMessageBox.Icon.Warning)
            qmess_box.show()
            self.__qmess_box = qmess_box
            return

        res_box = check_img_exist(self.__choosen_id)
        if res_box is not None:
            self.__qmess_box = res_box
            res_box.show()
            return

        diff = self.ui.level_diff_comboBox.currentText()
        score_type = self.ui.type_res_comboBox.currentText()
        # Create widget game...
        try:
            self.__widget_game = BuildGameWidgetController.build_widget(
                diff=diff, score_type=score_type, user_login=self.__user_login,
                id_img=self.__choosen_id
            )

            if self.__widget_game is None:
                self.__qmess_box = return_qmess_box_connect_db_error(
                    title='Ошибка подключения к БД или \n' +\
                          'игра с данным изображенем не существует.'
                )
                self.__qmess_box.show()
                return

            self.__widget_game.show()
        except Exception:
            qmess_box = QMessageBox()
            qmess_box.setText("Ошибка создания игры. Возможно файл игры поврежден.")
            qmess_box.setWindowTitle("Ошибка")
            qmess_box.setIcon(QMessageBox.Icon.Critical)
            qmess_box.show()
            self.__qmess_box = qmess_box
            print(traceback.print_exc())
