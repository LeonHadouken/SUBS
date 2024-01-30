-----------------------------------------------------------
Установка необходимого софта:
-----------------------------------------------------------

— Качаете Python 3.9 Для AMD или Intel.

— Качаете PyCharm Community Edition.

-----------------------------------------------------------
Подготовка и настройка среды:
-----------------------------------------------------------

Если вы используете GitHub — просто подключитесь к этому репозиторию и сделайте pull-request.

Если гитхаба нет:

        Запускаете PyCharm —> File —> New Project.

Установки:

        Location — Путь к проекту. 
        Сразу же копируем в буфер полный путь после его обозначения.
        
        Base Interpreter — Выбираем Python 3.9 (Может называться Python39)
        Нажимаем Create.

Заходим в проводник, копируем адрес проекта из location в адресную строку, и копируем туда содержимое этого архива.

-----------------------------------------------------------
Подготовка к запуску.
-----------------------------------------------------------
ВСЕ КОММАНДЫ ВВОДИТЬ ПО ОДНОЙ. ПОСЛЕ КАЖДОЙ ПРОЖИМАТЬ ENTER. 
-----------------------------------------------------------

Открываем наш проект.

Вызываем терминал с помощью сочетания Alt + F12

Устанавливаем необходимые библиотеки:

        pip install django

        pip install mtranslate

        pip install PyAudio

        pip install SpeechRecognition

Обновляем pip:

        python.exe -m pip install --upgrade pip

-----------------------------------------------------------
Запуск.
-----------------------------------------------------------

Переходим в папку с исполняемым файлом:

        cd SpeechRecognitionProject

Запускаем скрипт:

        python manage.py runserver

Чтобы прекратить работу скрипта нужно нажать Ctrl+C

-----------------------------------------------------------
Захват и отображение.
-----------------------------------------------------------

Открываем OBS

        Добавить источник —> Браузер

        Называйте источник как хотите.

        URL-адрес http://127.0.0.1:8000/

        ОКЕЙ

Щелкните по нему правой кнопкой мыши —> Фильтры —> Фильтры Эффектов —> Нажмите '+' —> Хромакей

-----------------------------------------------------------
Изменить шрифт 
-----------------------------------------------------------
меняем в файле SpeechRecognitionProject/subtitles/templates/subtitles/index.html 

14 строка:
        
        font-family: 'Cordana' — Просто введите туда любой шрифт из тех, что у вас есть.

-----------------------------------------------------------
Чтобы сменить язык, С КОТОРОГО нужно переводить:
-----------------------------------------------------------
меняем в файле manage.py

12 строка:
        
        text = recognizer.recognize_google(audio, language="ru-RU") — "ru-RU" меняем на нужный.

-----------------------------------------------------------
Чтобы сменить язык, НА КОТОРЫЙ нужно переводить:
-----------------------------------------------------------
меняем в файле manage.py

24 строка:
        
        translation = translate(text, "en") — "en" меняем на нужный.
-----------------------------------------------------------




