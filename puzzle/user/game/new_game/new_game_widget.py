from PySide6.QtWidgets import QWidget

from puzzle.common.choose_image import QChooseImageWidget
from puzzle.database import DatabaseController
from puzzle.common.back_to_menu import BackToMenu
from puzzle.common.signals import SignalSenderBackToMenu, SignalSenderChooseImage
from puzzle.utils import DIFFIC_LIST, TYPE_SCORE, BUILD_AREA, BUILD_LENTA, TRIANGLE_PUZZLES, RECTANGLE_PUZZLES
from .puzzle_game.on_field import GameOnFieldRectangleWidget, GameOnFieldTriangleWidget

from .new_game import Ui_Form


class QNewGameWidget(QWidget, BackToMenu):

    def __init__(self, signal_back_to_menu: SignalSenderBackToMenu):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
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
        self.choosen_id = img_id
        img_name = DatabaseController.get_img_name(img_id)
        self.ui.choosen_image_lineEdit.setText(img_name)

    def clicked_start_game(self):
        diff = self.ui.level_diff_comboBox.currentText()
        type_score = self.ui.type_res_comboBox.currentText()
        print(f"Diff:{diff} type score:{type_score}")

        # Create widget game...
        frag_h, frag_v, type_build, type_puzzle = DatabaseController.get_diff_params(diff)
        print(f"frag_h:{frag_h} frag_v:{frag_v} type_build:{type_build} type_puzzle:{type_puzzle}")
        self._widget_game = None
        if type_build == BUILD_AREA:
            if type_puzzle == RECTANGLE_PUZZLES:
                self._widget_game = GameOnFieldRectangleWidget(
                    id_img=self.choosen_id, diff=diff,
                    size_block_h=int(frag_h), size_block_w=int(frag_v)
                )
            elif type_puzzle == TRIANGLE_PUZZLES:
                self._widget_game = GameOnFieldTriangleWidget(
                    id_img=self.choosen_id, diff=diff,
                    size_block_h=int(frag_h), size_block_w=int(frag_v)
                )
            else:
                raise ValueError(f"Unknown type of puzzle: {type_build}, while type build: {type_build}")
        elif type_build == BUILD_LENTA:
            if type_puzzle == RECTANGLE_PUZZLES:
                pass
            elif type_puzzle == TRIANGLE_PUZZLES:
                pass
            else:
                raise ValueError(f"Unknown type of puzzle: {type_build}, while type build: {type_build}")
        else:
            raise ValueError(f"Unknown type build: {type_build}")

        self._widget_game.show()
