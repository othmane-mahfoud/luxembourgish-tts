from tts import setupTTS, speak

def main():
    synthesizer = setupTTS()
    text = input("Enter the text you want to convert to speech: \n")
    speak(synthesizer=synthesizer, text=text)

if __name__ == "__main__":
    main()
    