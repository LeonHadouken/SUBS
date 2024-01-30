import speech_recognition as sr
from mtranslate import translate

def speech_to_text():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Скажи что-нибудь:")
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio, language="ru-RU")
        print("Ты сказал(а):", text)
        return text
    except sr.UnknownValueError:
        print("Извини, не могу распознать речь")
        return None
    except sr.RequestError as e:
        print(f"Ошибка при запросе к сервису распознавания: {e}")
        return None

def translate_to_english(text):
    try:
        translation = translate(text, "en")
        print(f"Переведенный текст на английский: {translation}")
        return translation
    except Exception as e:
        print(f"Ошибка при переводе текста: {e}")
        return None

if __name__ == "__main__":
    while True:
        text = speech_to_text()
        if text:
            translated_text = translate_to_english(text)
            if translated_text:
                print("Субтитры (en):", translated_text)
