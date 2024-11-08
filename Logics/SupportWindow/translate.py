from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QApplication
import translate
from Logics.SupportWindow.Style.support_style import CONST_TRANSLATE_WINDOW

class TranslateWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setFixedSize(250, 250)
        self.setWindowTitle("Переводчик")
        self.setStyleSheet(CONST_TRANSLATE_WINDOW)
        
        self.res = None
        
        control_UI = QVBoxLayout()
        central_widget = QWidget()
        
        ins = QLabel(text="Введите слово для перевода на английский")
        self.enter = QLineEdit()
        trn = QPushButton(text="Перевести")
        trn.clicked.connect(self.transl)
        
        control_UI.addWidget(ins, alignment=Qt.AlignmentFlag.AlignCenter)
        control_UI.addWidget(self.enter)
        control_UI.addWidget(trn)
        
        central_widget.setLayout(control_UI)
        
        self.setCentralWidget(central_widget)
        
        self.show()
        
    def transl(self):
        gen = translate.Translator(from_lang="ru", to_lang="en")
        
        text = self.enter.text()
        
        translation = gen.translate(text)
        
        self.res = QMessageBox()
        self.res.setWindowTitle("Перевод")
        self.res.setText(translation)
        
        self.res.show()