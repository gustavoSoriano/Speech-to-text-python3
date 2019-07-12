import speech_recognition as sr
from pydub import AudioSegment

r = sr.Recognizer()

def converFile():
    AudioSegment.from_file("./soriano.mp3").export("./soriano.flac", format="flac")

def recordAudio():
    with sr.Microphone() as s:
        r.adjust_for_ambient_noise(s)

        while True:
            audio  = r.listen(s)
            speech = r.recognize_google(audio, language='pt', show_all=True)
            print( speech )



def loadFile():
    r     = sr.Recognizer() 
    audio = sr.AudioFile("soriano.flac")

    with audio as source:
        print("Wait. Program Starting")
        audio   = r.record(source)
        message = r.recognize_google(audio, language='pt', show_all=True)

        for i in range( len(message["alternative"]) ):
            print( message["alternative"][i]["transcript"] )

converFile()
loadFile()





