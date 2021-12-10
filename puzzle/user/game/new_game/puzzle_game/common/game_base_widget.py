from abc import abstractmethod

import PySide6
from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QWidget, QMessageBox

from puzzle.common.preview_widget import QPreviewWidget
from puzzle.common.qmess_boxes import return_qmess_box_connect_db_error
from puzzle.database import DatabaseController
from .score_calculators import ScoreCalculatorController


class GameBaseWidget(QWidget):

    def __init__(
            self, user_login: str, id_img: str, diff: str,
            size_block_w: int, size_block_h: int,
            score_type: str, saved_game_id: int = None):
        super().__init__()
        self._user_login = user_login
        self._id_img = id_img
        self._diff = diff
        self._score_type = score_type
        self._size_block_w = size_block_w
        self._size_block_h = size_block_h
        self._time_left: int = None
        self._current_score: int = None
        self._timer_score_update: QTimer = None
        self._timer_game_status: QTimer = None
        self._preview_widget: QPreviewWidget = None
        self._qmess_box: QMessageBox = None

        self._score_controller = ScoreCalculatorController(type_score=score_type)
        self._img_path = DatabaseController.get_img(id_img)

        if self._img_path is None:
            self._qmess_box = return_qmess_box_connect_db_error()
            self._qmess_box.show()
            return

        if saved_game_id is not None:
            game_config = DatabaseController.get_saved_game(saved_game_id)
        else:
            game_config = DatabaseController.get_game_config(diff=diff, id_img=id_img)

        if game_config is None:
            self._qmess_box = return_qmess_box_connect_db_error()
            self._qmess_box.show()
            return

        self._start_score = DatabaseController.parse_score_config(game_config)

        if self._start_score is None:
            self._qmess_box = return_qmess_box_connect_db_error()
            self._qmess_box.show()
            return

        self._game_config = game_config

    def reset_status(self):
        self._time_left = 0
        self._current_score = self._start_score

    def start_game(self):
        self.reset_status()
        self.start_score_timer()
        self.start_status_timer()

    def start_status_timer(self):
        self._timer_game_status = QTimer(self)
        self._timer_game_status.timeout.connect(self.game_end)
        self._timer_game_status.start(500)

    def stop_status_timer(self):
        if self._timer_game_status is not None:
            self._timer_game_status.stop()

    def start_score_timer(self):
        self._timer_score_update = QTimer(self)
        self._timer_score_update.timeout.connect(self.update_score)
        self._timer_score_update.start(1_000)

    def stop_score_timer(self):
        if self._timer_score_update is not None:
            self._timer_score_update.stop()

    def stop_game(self):
        self.stop_score_timer()
        self.stop_status_timer()

    def game_end(self):
        if not self.current_game_state():
            return

        self.stop_game()
        result = DatabaseController.add_record(
            user_login=self._user_login, diff=self._diff,
            score_value=self._current_score, score_type=self._score_type
        )

        if not result:
            self._qmess_box = return_qmess_box_connect_db_error()
            self._qmess_box.show()
            return

        # End of game
        # Show dialog window with message about end of game
        qmess_box = QMessageBox()
        qmess_box.setWindowTitle("Конец игры")
        qmess_box.setText(
            "Поздравляем! Вы собрали полный пазл.\n" +\
            f"Вам счет: {self._current_score}\n" +\
            f"Хотите начать заново или выйти?"
        )
        qmess_box.setIcon(QMessageBox.Icon.Question)
        retry_button = qmess_box.addButton(QMessageBox.Retry)
        close_button = qmess_box.addButton(QMessageBox.Close)

        close_button.clicked.connect(lambda x: self.close())
        retry_button.clicked.connect(self.build_game)
        self._qmess_box = qmess_box
        self._qmess_box.show()

    @abstractmethod
    def current_game_state(self) -> bool:
        """
        Return True if game is ended otherwise - False

        """
        pass

    @abstractmethod
    def update_score(self):
        pass

    @abstractmethod
    def build_game(self):
        pass

    def take_new_score(self, bad_placed: int, max_placed: int):
        self._time_left += 1
        self._current_score = self._score_controller.update_score(
            bad_placed=bad_placed, max_placed=max_placed,
            start_time=self._start_score, current_time=self._time_left
        )
        return self._current_score

    def preview_full_image(self):
        img_path = DatabaseController.get_img(self._id_img)

        if img_path is None:
            self._qmess_box = return_qmess_box_connect_db_error()
            self._qmess_box.show()
            return

        preview_widget = QPreviewWidget(img_path, "test")
        preview_widget.show()
        self._preview_widget = preview_widget

    def closeEvent(self, event:PySide6.QtGui.QCloseEvent) -> None:
        self.stop_score_timer()
