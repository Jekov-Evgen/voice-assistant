import speech_recognition
import pyaudio
import wave

CHUNK = 1024    
FRT = pyaudio.paInt16
CHAN = 1
REC_SEC = 3
OUTPUT = "output.wav"
RT = 44100

class Logic:
    def __init__(self) -> None:
        self.__p = pyaudio.PyAudio()
        self.__strem = self.__p.open(format=FRT, channels=CHAN, rate=RT, input=True, frames_per_buffer=CHUNK)
        self.frames = []
    
    def sample(self):
        for i in range(0, int(RT / CHUNK * REC_SEC)):
            data = self.__strem.read(CHUNK)
            self.frames.append(data)
            
    def end(self):
        self.__strem.stop_stream()
        self.__strem.close()
        self.__p.terminate()
        
    def WAV(self):
        w = wave.open(OUTPUT, 'wb')
        w.setnchannels(CHAN)
        w.setsampwidth(self.__p.get_sample_size(FRT))
        w.setframerate(RT)
        w.writeframes(b''.join(self.frames))
        w.close()
    
    
        
class ReadingIntoVariable:
    def __init__(self) -> None:
        self.__s = speech_recognition.WavFile("output.wav")
        self.__r = speech_recognition.Recognizer()
        
    def pulling_out(self):
        with self.__s as audio:
            content = self.__r.record(audio)
            self.__r.adjust_for_ambient_noise(audio)
            try:
                text = self.__r.recognize_google(content, language="ru-RU") 
                return text
            except:
                print("Не удалось распознать речь")
                return