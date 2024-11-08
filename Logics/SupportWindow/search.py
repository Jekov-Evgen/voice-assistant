from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton
from Logics.SupportWindow.Style.support_style import CONST_WINDOW
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class SearchWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setFixedSize(250, 250)
        self.setWindowTitle("Поисковик")
        self.setStyleSheet(CONST_WINDOW)
        
        control_UI = QVBoxLayout()
        central_widget = QWidget()
        
        instructions = QLabel(text="Введите запрос")
        self.inp = QLineEdit()
        go = QPushButton(text="Найти")
        go.clicked.connect(self.start)
        
        control_UI.addWidget(instructions, alignment=Qt.AlignmentFlag.AlignCenter)
        control_UI.addWidget(self.inp)
        control_UI.addWidget(go)
        
        central_widget.setLayout(control_UI)
        
        self.setCentralWidget(central_widget)
        
        self.show()
        
    def start(self):
        text = self.inp.text()
        
        go = webdriver.Chrome()
        go.get("https://www.google.com")
        s = go.find_element(By.NAME, "q")
        
        s.send_keys(text)
        s.send_keys(Keys.RETURN)
        
        input("")
        
    