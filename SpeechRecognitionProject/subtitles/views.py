from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from threading import Thread
import time
from speech_recognition import Recognizer, UnknownValueError, RequestError, Microphone
from mtranslate import translate

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
        else:
            # Если нет нового перевода, заменяем на пустую строку
            translated_text = ""

def index(request):
    return render(request, 'subtitles/index.html', {'translated_text': translated_text})

@csrf_exempt
def get_subtitle(request):
    global translated_text
    return JsonResponse({'subtitle': translated_text})

# Запускаем обновление субтитров в отдельном потоке
update_subtitle_thread = Thread(target=update_subtitle)
update_subtitle_thread.daemon = True
update_subtitle_thread.start()
