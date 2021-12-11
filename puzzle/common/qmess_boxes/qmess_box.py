from PySide6.QtWidgets import QMessageBox

def return_qmess_box(title: str, text: str, icon) -> QMessageBox:
    qmess_box = QMessageBox()
    qmess_box.setIcon(icon)
    qmess_box.setText(text)
    qmess_box.setWindowTitle(title)
    return qmess_box