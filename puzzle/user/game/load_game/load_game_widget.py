import traceback

from PIL import Image, ImageQt
from PySide6.QtGui import Qt, QImage, QPixmap
from PySide6.QtWidgets import QWidget, QTableWidgetItem, QMessageBox, QHeaderView

from puzzle.common.error_box_widget import check_game_exist, check_img_exist
from puzzle.common.qmess_boxes import return_qmess_box_connect_db_error
from .load_game import Ui_LoadGame
from puzzle.database import DatabaseController
from puzzle.common.signals import SignalSenderBackToMenu
from puzzle.common.back_to_menu import BackToMenu

from puzzle.user.game.new_game.puzzle_game.build_game_widget_controller import BuildGameWidgetController


class QLoadGameWidget(QWidget, BackToMenu):

    SIZE_WINDOW_W = 600
    SIZE_WINDOW_H = 400

    def __init__(self, user_login: str, signal_back_to_menu: SignalSenderBackToMenu):
        super().__init__()
        self.ui = Ui_LoadGame()
        self.ui.setupUi(self)
        self.__user_login = user_login
        self.__selected_row = -1
        self.__qmess_box: QMessageBox = None
        self.__game_widget = None
        self.__data_about_game = []
        self.setup_back_to_menu_signal(signal_back_to_menu=signal_back_to_menu)

        # Buttons
        self.ui.back_to_menu_pushButton.clicked.connect(self.emit_signal_back_to_menu)
        self.ui.delete_game_pushButton.clicked.connect(self.clicked_delete_selected)
        self.ui.load_game_pushButton.clicked.connect(self.clicked_load_selected)
        self.setLayout(self.ui.gridLayout)

        # Table view
        # Headers
        self.ui.saved_games_tableWidget.setColumnCount(3)
        self.ui.saved_games_tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        qtwi = QTableWidgetItem("Изображение", QTableWidgetItem.Type)
        qtwi.setFlags(qtwi.flags() ^ Qt.ItemIsEditable)
        self.ui.saved_games_tableWidget.setHorizontalHeaderItem(0, qtwi)
        self.ui.saved_games_tableWidget.setColumnWidth(0, 150)

        qtwi = QTableWidgetItem("Сложность", QTableWidgetItem.Type)
        qtwi.setFlags(qtwi.flags() ^ Qt.ItemIsEditable)
        self.ui.saved_games_tableWidget.setHorizontalHeaderItem(1, qtwi)

        qtwi = QTableWidgetItem("Тип подсчета результатов", QTableWidgetItem.Type)
        qtwi.setFlags(qtwi.flags() ^ Qt.ItemIsEditable)
        self.ui.saved_games_tableWidget.setHorizontalHeaderItem(2, qtwi)
        self.ui.saved_games_tableWidget.setColumnWidth(2, 200)

        # Signals
        self.ui.saved_games_tableWidget.cellClicked.connect(self.signal_cell_selected)
        self.update_table_content()

    def update_table_content(self):
        self.ui.saved_games_tableWidget.setRowCount(0)
        saved_games_info = DatabaseController.get_all_saved_games_by_user(self.__user_login)

        if saved_games_info is None:
            self.__qmess_box = return_qmess_box_connect_db_error()
            self.__qmess_box.show()
            return

        for row_i, single_data in enumerate(saved_games_info):
            self.ui.saved_games_tableWidget.setRowCount(
                self.ui.saved_games_tableWidget.rowCount()+1
            )
            self.ui.saved_games_tableWidget.setRowHeight(
                self.ui.saved_games_tableWidget.rowCount()-1,
                150
            )

            img_path = DatabaseController.get_img(single_data['id_img'])

            if img_path is None:
                self.__qmess_box = return_qmess_box_connect_db_error()
                self.__qmess_box.show()
                return

            image = Image.open(img_path)
            image = image.resize((150, 150))
            qpixmap = QPixmap(QImage(ImageQt.ImageQt(image)))

            img_item = QTableWidgetItem()
            img_item.setData(Qt.DecorationRole, qpixmap)
            img_item.setTextAlignment(Qt.AlignCenter)
            img_item.setFlags(img_item.flags() ^ Qt.ItemIsEditable)

            self.ui.saved_games_tableWidget.setItem(row_i, 0, img_item)
            diff_item = QTableWidgetItem(single_data['diff'], QTableWidgetItem.Type)
            diff_item.setTextAlignment(Qt.AlignCenter)
            diff_item.setFlags(diff_item.flags() ^ Qt.ItemIsEditable)
            self.ui.saved_games_tableWidget.setItem(row_i, 1, diff_item)
            score_type = QTableWidgetItem(single_data["score_type"], QTableWidgetItem.Type)
            score_type.setTextAlignment(Qt.AlignCenter)
            score_type.setFlags(score_type.flags() ^ Qt.ItemIsEditable)
            self.ui.saved_games_tableWidget.setItem(row_i, 2, score_type)
            self.__data_about_game.append(
                {'id_img': single_data['id_img'], 'diff': single_data['diff'], 'score_type': single_data["score_type"],
                 "saved_game_id": single_data['saved_game_id']}
            )

    def signal_cell_selected(self, row: int, column: int):
        print(self.__selected_row)
        self.__selected_row = row

    def clicked_delete_selected(self):
        if self.__selected_row != -1:
            self.ui.saved_games_tableWidget.removeRow(self.__selected_row)
            # Send info to DataBase to remove saved game
            result = DatabaseController.remove_saved_game_by_user(
                saved_game_id=self.__data_about_game[self.__selected_row]['saved_game_id']
            )

            if not result:
                self.__qmess_box = return_qmess_box_connect_db_error()
                self.__qmess_box.show()
                return

            del self.__data_about_game[self.__selected_row]
        else:
            self._show_box_game_not_choosen()

    def clicked_load_selected(self):
        if self.__selected_row != -1:
            selected_dict = self.__data_about_game[self.__selected_row]
            diff, score_type, id_img, saved_game_id = (
                selected_dict['diff'], selected_dict['score_type'],
                selected_dict['id_img'], selected_dict['saved_game_id']
            )
            user_login = self.__user_login

            result_box = check_game_exist(int(saved_game_id))

            if result_box is not None:
                result_box.show()
                self.__qmess_box = result_box
                return # Error while load

            result_box = check_img_exist(int(id_img))

            if result_box is not None:
                result_box.show()
                self.__qmess_box = result_box
                return # Error while load
            # Create widget game...
            try:
                game_widget = BuildGameWidgetController.build_widget(
                    diff=diff, score_type=score_type, user_login=user_login,
                    id_img=id_img, saved_game_id=saved_game_id
                )
            except Exception:
                qmess_box = QMessageBox()
                qmess_box.setText("Ошибка создания игры. Возможно файл игры поврежден.")
                qmess_box.setWindowTitle("Ошибка")
                qmess_box.setIcon(QMessageBox.Icon.Critical)
                qmess_box.show()
                self.__qmess_box = qmess_box
                print(traceback.print_exc())
                return

            if game_widget is None:
                self.__qmess_box = return_qmess_box_connect_db_error()
                self.__qmess_box.show()
                return

            game_widget.show()
            self.__game_widget = game_widget
        else:
            self._show_box_game_not_choosen()

    def _show_box_game_not_choosen(self):
        qmes_box = QMessageBox()
        qmes_box.setWindowTitle("Ошибка")
        qmes_box.setText("Игра не выбрана.")
        qmes_box.setIcon(QMessageBox.Icon.Warning)
        qmes_box.show()
        self.__qmess_box = qmes_box

    def reset_state(self):
        self.__selected_row = -1
        self.__qmess_box: QMessageBox = None
        self.__game_widget = None
        self.__data_about_game = []

    def update(self) -> None:
        self.reset_state()
        self.update_table_content()
        super().update()
