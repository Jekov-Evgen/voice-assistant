from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QApplication
from Logics.SupportWindow.Style.support_style import CONST_WINDOW_TIMER

class TimerWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setFixedSize(250, 250)
        self.setWindowTitle("Таймер")
        self.setStyleSheet(CONST_WINDOW_TIMER)
        
        self.error = None
        self.res = None
        
        control_UI = QVBoxLayout()
        central_widget = QWidget()
        
        instructions = QLabel(text="Введите время в секундах")
        self.inp = QLineEdit()
        go = QPushButton(text="Засечь таймер")
        go.clicked.connect(self.start)
        
        control_UI.addWidget(instructions, alignment=Qt.AlignmentFlag.AlignCenter)
        control_UI.addWidget(self.inp)
        control_UI.addWidget(go)
        
        central_widget.setLayout(control_UI)
        
        self.setCentralWidget(central_widget)
        
        self.show()
        
    def start(self):
        try:
            time = self.inp.text()
        except:
            self.error = QMessageBox()
            self.error.setWindowTitle("Ошибка")
            self.error.setText("Ошибка ввода времени")
            
            self.error.show()
            
        self.interval = QTimer()
        self.interval.setInterval(int(time) * 1000)
        self.interval.timeout.connect(self.time_is_up)
        self.interval.start()
        
    def time_is_up(self):
        self.res = QMessageBox()
        self.res.setWindowTitle("Время!!!")
        self.res.setText("Время вышло!")
        
        self.res.show()
        
        self.interval.stop()