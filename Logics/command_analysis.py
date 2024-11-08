import os
import webbrowser
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QLabel, QPushButton, QMainWindow, QWidget, QVBoxLayout
from Logics.SupportWindow.timer import TimerWindow
from Logics.SupportWindow.translate import TranslateWindow
from Logics.SupportWindow.search import SearchWindow
from Logics.SupportWindow.Style.support_style import CONST_ANSWER_BOX

class Answer(QMainWindow):
    def __init__(self, text) -> None:
        super().__init__()
        self.setFixedSize(150, 150)
        self.setWindowTitle("Ответ!!!!")
        self.setStyleSheet(CONST_ANSWER_BOX)
        
        control_UI = QVBoxLayout()
        central_widget = QWidget()
        
        ans = QLabel(text)
        ds = QPushButton()
        ds.clicked.connect(self.close)
        
        control_UI.addWidget(ans, alignment=Qt.AlignmentFlag.AlignCenter)
        control_UI.addWidget(ds)
        
        central_widget.setLayout(control_UI)
        
        self.setCentralWidget(central_widget)
        
        self.show()

class Analysis:
    def analyze(self, text : str):
        self.res = None
        
        command = {"привет": self.greet, 
                   "ладонь" : self.five, 
                   "интернет" : self.open_google, 
                   "записать": self.create_notebook,
                   "проекты": self.open_my_git,
                   "логика" : self.open_my_codewars, 
                   "видео" : self.open_my_youtube,
                   "писать" : self.open_vs_cod,
                   "погода" : self.get_weather,
                   "таймер" : self.timer, 
                   "лиза" : self.her, 
                   "слово" : self.translate,
                   "поиск" : self.search}
        
        if text in command:
            command[text]()
        
    def greet(self):
        app = QApplication([])
        
        answer = Answer("Привет!!")
        
        app.exec()
        
    def five(self):
        app = QApplication([])
        
        answer = Answer("Даю краба")
        
        app.exec()
        
    def open_google(self):
        os.startfile(r"C:\Program Files\Google\Chrome\Application\chrome.exe")
        
    def create_notebook(self):
        fl = open("test.txt", 'w')
        os.startfile(r"C:\Users\Женя\OneDrive\Desktop\programming\ML\my ml\test.txt")
        
    def open_my_git(self):
        webbrowser.open("https://github.com/Jekov-Evgen")
        
    def open_my_codewars(self):
        webbrowser.open("https://www.codewars.com/users/jeeeek")
        
    def open_my_youtube(self):
        webbrowser.open("https://www.youtube.com/")
        
    def open_vs_cod(self):
        os.startfile(r"C:\Users\Женя\AppData\Local\Programs\Microsoft VS Code\Code.exe")
        
    def get_weather(self):
        webbrowser.open(r"https://ua.sinoptik.ua/%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0-%D0%BE%D0%B4%D0%B5%D1%81%D0%B0")
        
    def timer(self):
        app = QApplication([])
        start = TimerWindow()
        app.exec()
        
    def her(self):
        os.startfile(r"C:\Users\Женя\source\repos\Liza\x64\Debug\Liza.exe")
        
    def translate(self):
        app = QApplication([])
        start = TranslateWindow()
        app.exec()
        
    def search(self):
        app = QApplication([])
        start = SearchWindow()
        app.exec()