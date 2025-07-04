# Неоновое TODO-приложение 🌌

Ахуенное TODO-приложение на русском с неоновым дизайном, автоматическим ID, поиском и календарем. Построено на FastAPI и React с Tailwind CSS, Flatpickr и glassmorphism. Разъёб в каждом пикселе! 😎

## ✨ Фичи

  - **Автоматический ID** 📝: Задачи создаются без ручного ввода ID — SQLite генерит уникальный ID.
  - **Поиск** 🔍: Фильтрация по названию, описанию, категории с кнопкой лупы.
    - Показывает "Ничего не найдено", если задач нет.
  - **Календарь** 📅: Выбор даты через Flatpickr, просмотр задач по дате (например, 4 июля 2025 = `2025-07-04`).
  - **Тёмная/светлая тема** 🌙: Переключение между неоновой тёмной и светлой темами с анимацией.
  - **Неоновый стиль** 🎨: Glassmorphism, неоновые градиенты, анимации (neon-pulse, tilt, shake).
  - **Категории** 🗂:
    - Работа (💼)
    - Личное (🏡)
    - Срочно (🔥)
  - **Фильтры и сортировка** 🔄:
    - Фильтры: Все задачи, Активные, Выполненные.
    - Сортировка: по ID, названию, статусу.
  - **Спиннер** 🌀: Показывает загрузку при добавлении/редактировании/удалении.
  - **Интерактивность** ✅:
    - Отметка задач как выполненных.
    - Редактирование (ID readonly).
    - Удаление с анимациями и уведомлениями.

## 🛠 Технологии

  - **Бэкенд**:
    - FastAPI
    - SQLite (авто-ID через `INTEGER PRIMARY KEY AUTOINCREMENT`)
  - **Фронтенд**:
    - React (CDN)
    - Tailwind CSS
    - Flatpickr (календарь)
    - Font Awesome (иконки)
    - Axios (запросы)
  - **Стили**:
    - Неоновый градиент
    - Glassmorphism
    - Анимации (neon-pulse, tilt, shake)

## 🚀 Установка

1. Клонируй репозиторий:
   ```bash
   git clone https://github.com/dgrmorty/todo.git
   cd todo


2. Установи Python 3.8+ и создай виртуальное окружение:
    ```bash
    python3 -m venv venv
    source venv/bin/activate


3. Установи зависимости:
    ```bash
    pip install fastapi uvicorn


4. Запусти FastAPI сервер:
    ```bash
    uvicorn main:app --reload


5. В другом терминале запусти HTTP-сервер для фронтенда:
    ```bash
    python3 -m http.server 8080


6. Открой в браузере:
    ```bash
    open http://127.0.0.1:8080



📋 Использование

Добавить задачу:
Введи название (обязательно).
Добавь описание, категорию, дату (опционально).
ID генерится автоматически.
Нажми "Добавить задачу".


Поиск:
Введи запрос (например, "молоко" или "Работа").
Нажми лупу.


Календарь:
Кликни на дату (например, 4 июля 2025).
Откроется модалка с задачами.


Редактирование:
Кликни "Редактировать".
ID показывается (readonly), остальные поля редактируются.


Выполнение/удаление:
Отметь задачу как выполненную ("Отметить выполненной" / "Отменить").
Удали задачу ("Удалить").


Тема:
Переключи тёмную/светлую тему через иконку солнца/луны.



📂 Файлы

main.py: FastAPI бэкенд с SQLite.
index.html: React фронтенд с Tailwind CSS, Flatpickr.
.gitignore: Игнорирует venv, tasks.db, .vscode, .DS_Store.
README.md: Этот файл с описанием.

🗂 Структура проекта
todo/
  ├── main.py          # FastAPI бэкенд
  ├── index.html       # React фронтенд
  ├── .gitignore       # Игнор ненужных файлов
  ├── README.md        # Документация
  ├── tasks.db        # SQLite база (игнорируется)
  └── venv/           # Виртуальное окружение (игнорируется)

🔮 Планы на будущее

Просроченные задачи 🔥:
Подсветка задач с истёкшим сроком (due_date < текущей даты).


Экспорт в CSV 📤:
Скачивание списка задач в CSV.


Drag-and-drop 🖱:
Перетаскивание задач для изменения порядка.


Деплой 🌐:
Размещение на Vercel или другом хостинге.



🛠 Проблемы и решения

Ошибка CORS:
Проверь в main.py:app.add_middleware(CORSMiddleware, allow_origins=["http://127.0.0.1:8080"])





Задачи не сохраняются:
Проверь логи FastAPI:uvicorn main:app --reload


Проверь консоль браузера:# Открой F12 → Console




Тёмная тема не читается:
Переключи на светлую тему.
Проверь стили в F12 → Elements:.dark-theme, .flatpickr-day





📬 Контакты
Разработано с любовью к разъёбу! 😎Связь: dgrmorty
🏷 Хэштеги
#todo #productivity #react #fastapi #sqlite #tailwindcss #flatpickr #fontawesome #axios #neon #glassmorphism```