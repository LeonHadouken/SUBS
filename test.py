from flask import Flask, render_template
from speech_recognition import Recognizer, UnknownValueError, RequestError, Microphone
from mtranslate import translate
from threading import Thread
import time
from flask_ngrok import run_with_ngrok

app = Flask(__name__)
run_with_ngrok(app)  # Используем ngrok для проброса порта

translated_text = ""

def speech_to_text():
    recognizer = Recognizer()

    with Microphone() as source:
        print("Скажи что-нибудь:")
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio, language="ru-RU")
        print("Ты сказал(а):", text)
        return text
    except UnknownValueError:
        print("Извини, не могу распознать речь")
        return None
    except RequestError as e:
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

def update_subtitle():
    global translated_text
    while True:
        text = speech_to_text()
        if text:
            translated_text = translate_to_english(text)
            time.sleep(0.1)  # обновляем каждые 100 миллисекунд

@app.route('/')
def index():
    return render_template('index.html', translated_text=translated_text)

if __name__ == '__main__':
    update_subtitle_thread = Thread(target=update_subtitle)
    update_subtitle_thread.daemon = True
    update_subtitle_thread.start()
    app.run(debug=True)
