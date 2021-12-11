from PySide6.QtWidgets import QMessageBox

def return_qmess_box_regist_info(title: str, text: str) -> QMessageBox:
    qmess_box = QMessageBox()
    qmess_box.setIcon(QMessageBox.Icon.Information)
    qmess_box.setText(text)
    qmess_box.setWindowTitle(title)
    return qmess_box