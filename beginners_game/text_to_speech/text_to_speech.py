from gtts import gTTS
from playsound import playsound


class TextSpeechAdapter:
    def __init__(self, text, language):
        self.text = text
        self.language = language
        self.audioFile = "speech.mp3"

    def saveLyrics(self):
        tosay = gTTS(text=self.text, lang=self.language)
        tosay.save(self.audioFile)

    def speech(self):
        self.saveLyrics()
        playsound(self.audioFile)


if __name__ == "__main__":
    toSay = str(input("What do you wan to say : "))
    TTSAdapter = TextSpeechAdapter(toSay, 'en')
    TTSAdapter.speech()
