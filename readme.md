# СУБД — Лабораторная работа №1

**Выполнил:** Челядинов Дмитрий  
**Группа:** ИВТ-363

---

## Описание

REST API сервер для управления базой данных MongoDB по тематике игры **War Thunder**. Система хранит данные об экипажах и военной технике трёх видов: наземной, морской и воздушной.

## Технологии

| Технология | Назначение |
|---|---|
| Python | Основной язык |
| FastAPI | REST API сервер |
| MongoDB | База данных |
| PyMongo | Драйвер для MongoDB |
| Pydantic | Валидация данных |
| Uvicorn | ASGI-сервер |

## Структура проекта

```
SUBD_Lab01/
├── main.py                          # Точка входа, запуск FastAPI
├── database.py                      # Функции работы с MongoDB
├── types_collection.py              # Enum типов коллекций
├── types_technic.py                 # Enum типов техники
├── generator/
│   ├── generator.py                 # Генерация тестовых документов
│   ├── support_functions.py         # Вспомогательные функции генератора
│   └── generator_constants/
│       ├── crew.py                  # Константы для экипажей
│       ├── air_tech.py              # Константы для авиатехники
│       ├── ground_tech.py           # Константы для наземной техники
│       ├── marine_tech.py           # Константы для морской техники
│       └── export_constatnts.py     # Экспорт констант
└── server/
    ├── collection_validator.py      # Pydantic-схемы запросов
    ├── convertor.py                 # Конвертация документов MongoDB ↔ JSON
    ├── documents/
    │   ├── crew_doc.py              # Модель документа экипажа
    │   └── technic_doc.py           # Модель документа техники
    └── routers/
        ├── routers.py               # Подключение всех роутеров
        ├── crew.py                  # Роутер /crew
        └── tech.py                  # Роутеры /air_tech, /ground_tech, /marine_tech
```

## База данных

**Название БД:** `war_thunder`  
**Подключение:** `mongodb://localhost:27017`

### Коллекции

**`crew`** — экипажи:
| Поле | Тип | Описание |
|---|---|---|
| `id` | int | Уникальный идентификатор |
| `count_people` | int | Количество человек (2–6) |
| `experience` | int | Опыт экипажа (1–99) |

**`ground_tech` / `marine_tech` / `air_tech`** — техника:
| Поле | Тип | Описание |
|---|---|---|
| `id` | int | Уникальный идентификатор |
| `name` | str | Название техники |
| `battle_rating` | float | Боевой рейтинг |
| `rank` | int | Ранг техники |
| `id_crew` | int | Ссылка на экипаж |

## API

Сервер запускается на `http://127.0.0.1:8000`. Документация доступна по адресу `http://127.0.0.1:8000/docs`.

### Экипаж (`/crew`)

| Метод | Endpoint | Описание |
|---|---|---|
| GET | `/crew` | Получить все записи экипажей |
| POST | `/crew` | Добавить экипаж |
| PUT | `/crew` | Обновить экипаж |
| DELETE | `/crew?id_doc={id}` | Удалить экипаж по ID |

**Тело POST-запроса:**
```json
{
  "count_people": 4,
  "experience": 75
}
```

**Тело PUT-запроса:**
```json
{
  "id": 1,
  "count_people": 4,
  "experience": 75
}
```

### Техника (`/air_tech`, `/ground_tech`, `/marine_tech`)

| Метод | Endpoint | Описание |
|---|---|---|
| GET | `/{type}_tech` | Получить всю технику данного типа |
| POST | `/{type}_tech` | Добавить единицу техники |
| PUT | `/{type}_tech` | Обновить запись о технике |
| DELETE | `/{type}_tech?id_doc={id}` | Удалить технику по ID |

**Тело POST-запроса:**
```json
{
  "name": "T-34",
  "battle_rating": 4.3,
  "rank": 3,
  "id_crew": 1
}
```

**Тело PUT-запроса:**
```json
{
  "id": 1,
  "name": "T-34",
  "battle_rating": 4.3,
  "rank": 3,
  "id_crew": 1
}
```

## Запуск

### Требования

- Python 3.10+
- MongoDB (запущенный на `localhost:27017`)

### Установка зависимостей

```bash
pip install fastapi uvicorn pymongo pydantic termcolor
```

### Запуск сервера

```bash
python main.py
```

Сервер запустится на `http://127.0.0.1:8000` в режиме автоперезагрузки (`reload=True`).

### Генерация тестовых данных

Для наполнения базы тестовыми документами использовать функцию из `generator/generator.py`:

```python
from database import get_database
from generator.generator import generate_documents

db = get_database()
generate_documents(db, count_documents=10)
```

Функция создаёт документы во всех четырёх коллекциях (`crew`, `ground_tech`, `marine_tech`, `air_tech`).
