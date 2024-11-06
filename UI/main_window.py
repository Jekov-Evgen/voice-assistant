from PyQt6.QtCore import Qt
from Style.style import CONST_WINDOW
from PyQt6.QtWidgets import QMainWindow, QWidget, QLabel, QPushButton, QVBoxLayout
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import QProcess

class MainWindow(QMainWindow):    
    def __init__(self) -> None:
        super().__init__()
        self.setFixedSize(350, 150)
        self.setWindowTitle("Голосовой помощник")
        self.setStyleSheet(CONST_WINDOW)
        self.setWindowIcon(QIcon(r"image\icon_scan.jpg"))
        
        conrol_UI = QVBoxLayout()
        central_widget = QWidget()
        self.process = QProcess()
        
        greet = QLabel(text="Приветствуем в голосовом помощнике")
        go_command = QPushButton(text="Начать выполнение")
        go_command.clicked.connect(self.run)
        
        conrol_UI.addWidget(greet, alignment=Qt.AlignmentFlag.AlignHCenter)
        conrol_UI.addWidget(go_command)
        
        central_widget.setLayout(conrol_UI)
        self.setCentralWidget(central_widget)
        
        self.show()
        
    def run(self):
        self.process.start("python", [r"C:\Users\Женя\OneDrive\Desktop\programming\ML\my ml\main.py"])