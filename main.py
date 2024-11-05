from Logics.voice_reading import Logic, ReadingIntoVariable
from Logics.command_analysis import Analysis
from time import sleep

if __name__ == "__main__":
    while True:
        start = Logic()
        conclusion = ReadingIntoVariable()
        command = Analysis()
    
        start.sample()
        start.end()
        start.WAV()
    
        result = conclusion.pulling_out()
        start.frames.clear()
        
        if str(result).lower() == "пока":
            break
    
        command.analyze(str(result).lower())
    
        sleep(2)
