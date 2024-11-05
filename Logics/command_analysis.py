import os

class Analysis:
    def analyze(self, text : str):
        command = {"привет": self.greet, "ладонь" : self.five, "интернет" : self.open_google}
        
        if text in command:
            command[text]()
        
    def greet(self):
        print("Привет") 
        
    def five(self):
        print("Даю пять")
        
    def open_google(self):
        os.startfile(r"C:\Program Files\Google\Chrome\Application\chrome.exe")