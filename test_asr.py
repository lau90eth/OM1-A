import speech_recognition as sr

r = sr.Recognizer()
mic = sr.Microphone()

def test(lang, phrase):
    print(f"\n[{lang}] Dì: {phrase}")
    with mic as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio, language=lang)
        print(f"Riconosciuto: {text}")
        return "pass" if phrase.lower() in text.lower() else "fail"
    except:
        return "error"

# Test
print(test("en-US", "hello how are you"))
print(test("it-IT", "ciao come stai"))