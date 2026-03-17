# Speech Subtitles 🎤➡️📝

[![Python Version](https://img.shields.io/badge/python-3.9%2B-blue)](https://www.python.org/downloads/)
[![Django Version](https://img.shields.io/badge/django-4.x-brightgreen)](https://www.djangoproject.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**Speech Subtitles** — это веб-приложение на Django, которое распознает речь с микрофона в реальном времени, переводит её и отображает в виде субтитров. Идеально подходит для стримеров, видеоблогеров и всех, кому нужны живые субтитры в OBS Studio.

![Демонстрация работы приложения](link_to_your_screenshot_or_gif_here)

## ✨ Возможности

*   🎙️ **Распознавание речи в реальном времени** — использует Google Speech Recognition для высокой точности.
*   🌍 **Автоматический перевод** — встроенный переводчик mtranslate переводит текст на нужный язык.
*   🖥️ **Веб-интерфейс для OBS** — специально разработанная страница для встраивания в OBS через источник "Браузер".
*   🟢 **Хромакей-фон** — белый фон легко убирается в OBS для наложения на любой контент.
*   ⚙️ **Гибкая настройка** — легкое изменение языков распознавания и перевода, а также шрифтов.

## 🚀 Быстрый старт

### Предварительные требования

*   **Python** версии 3.9 или выше ([скачать](https://www.python.org/))
*   **Git** (для клонирования репозитория) ([скачать](https://git-scm.com/))
*   **OBS Studio** (опционально, для стримов) ([скачать](https://obsproject.com/))

### Пошаговая установка

#### 1. Клонирование репозитория
```bash
git clone https://github.com/LeonHadouken/speech_subtitles.git
cd speech_subtitles
```

#### 2. Создание виртуального окружения
Это изолирует зависимости проекта от системы.
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

#### 3. Установка зависимостей
```bash
pip install django mtranslate PyAudio SpeechRecognition
```

<details>
<summary>💡 Если возникнут проблемы с PyAudio</summary>

На **Windows** обычно устанавливается без проблем.

На **macOS**:
```bash
brew install portaudio
pip install PyAudio
```

На **Linux** (Debian/Ubuntu):
```bash
sudo apt-get install portaudio19-dev python3-pyaudio
pip install PyAudio
```
</details>

#### 4. Настройка и запуск сервера
```bash
cd SpeechRecognitionProject
python manage.py runserver
```

Если вы увидели сообщение `Starting development server at http://127.0.0.1:8000/` — всё работает! Оставьте терминал открытым.

## 🎮 Интеграция с OBS Studio

1. **Запустите OBS Studio**
2. **Добавьте источник "Браузер":**
   *   Нажмите `+` в панели "Источники"
   *   Выберите "Браузер"
   *   Назовите источник (например, "Субтитры")
3. **Настройте источник:**
   *   **URL:** `http://127.0.0.1:8000/`
   *   **Ширина:** `1920` (или ваша ширина сцены)
   *   **Высота:** `300` (или нужная высота)
4. **Настройка прозрачности:**
   *   Кликните правой кнопкой по источнику → **"Фильтры"**
   *   В разделе "Фильтры эффектов" нажмите `+` → **"Хромакей"**
   *   **Тип ключа:** "Custom"
   *   **Цвет:** `#FFFFFF` (белый)
   *   Настройте "Схожесть" и "Сглаживание" по вкусу

Готово! Теперь ваша речь будет появляться в виде субтитров на трансляции.

## ⚙️ Настройка под себя

### Изменение языка распознавания
Откройте файл `SpeechRecognitionProject/manage.py` и найдите строку:
```python
text = recognizer.recognize_google(audio, language="ru-RU")
```
Поменяйте `ru-RU` на нужный код языка, например:
*   `en-US` — английский (США)
*   `de-DE` — немецкий
*   `fr-FR` — французский
*   `es-ES` — испанский

### Изменение языка перевода
В том же файле `manage.py` найдите строку:
```python
translation = translate(text, "en")
```
Поменяйте `en` на нужный код, например:
*   `ru` — русский
*   `de` — немецкий
*   `fr` — французский
*   `es` — испанский

### Изменение шрифта
Откройте файл `SpeechRecognitionProject/subtitles/templates/subtitles/index.html` и найдите 14-ю строку:
```css
font-family: 'Cordana'; /* Замените Cordana на любой установленный у вас шрифт */
```

## 🛠️ Устранение неполадок

### Ошибка "No module named '...'"
Убедитесь, что виртуальное окружение активировано, и выполните:
```bash
pip install -r requirements.txt
```
(Создайте файл `requirements.txt` со списком зависимостей, если его нет)

### Не работает микрофон
*   Проверьте, подключен ли микрофон к компьютеру
*   В Windows проверьте настройки конфиденциальности: разрешите доступ приложений к микрофону
*   Попробуйте перезапустить сервер

### Субтитры не появляются в OBS
*   Убедитесь, что сервер запущен (`python manage.py runserver`)
*   Проверьте URL в источнике браузера — должен быть `http://127.0.0.1:8000/`
*   Обновите страницу в OBS (правый клик по источнику → "Обновить")

## 🤝 Участие в разработке

Ваш вклад сделает проект лучше! Вот как вы можете помочь:

1. **Форкните** репозиторий
2. Создайте ветку для фичи (`git checkout -b feature/amazing-feature`)
3. **Закоммитьте** изменения (`git commit -m 'Add amazing feature'`)
4. **Запушьте** ветку (`git push origin feature/amazing-feature`)
5. Откройте **Pull Request**

### Идеи для улучшения:
*   Рефакторинг кода (вынести логику из `manage.py` в отдельные модули)
*   Добавление выбора микрофона из веб-интерфейса
*   Сохранение истории субтитров в базу данных
*   Возможность использования разных API перевода (Google Translate, Yandex)
*   Темная тема для веб-интерфейса

## 📄 Лицензия

Проект распространяется под лицензией MIT. Смотрите файл [LICENSE](LICENSE) для получения дополнительной информации.

## 📬 Контакты и обратная связь

*   **Автор:** [LeonHadouken](https://github.com/LeonHadouken)
*   **Ссылка на проект:** [https://github.com/LeonHadouken/speech_subtitles](https://github.com/LeonHadouken/speech_subtitles)

---

⭐ Если проект оказался полезным, поставьте звезду на GitHub — это мотивирует развивать его дальше!
```
