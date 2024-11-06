import os
import webbrowser
from time import sleep

class Analysis:
    def analyze(self, text : str):
        command = {"привет": self.greet, 
                   "ладонь" : self.five, 
                   "интернет" : self.open_google, 
                   "записать": self.create_notebook,
                   "проекты": self.open_my_git,
                   "алгоритмы" : self.open_my_codewars, 
                   "видео" : self.open_my_youtube,
                   "писать" : self.open_vs_cod,
                   "погода" : self.get_weather,
                   "таймер" : self.timer, 
                   "лиза" : self.her}
        
        if text in command:
            command[text]()
        
    def greet(self):
        print("Привет") 
        
    def five(self):
        print("Даю пять")
        
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
        print("введите время для таймера: ")
        tm = int(input())
        sleep(tm)
        print("время вышло")
        
    def her(self):
        os.startfile(r"C:\Users\Женя\source\repos\Liza\x64\Debug\Liza.exe")