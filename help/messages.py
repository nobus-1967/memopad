"""Program messages and contex help for MemoPad."""
TITLE: str = """
# MEMOPAD (SQLite-версия 1.2.0)

"""
INFO: str = """
**`MemoPad`** - консольный редактор и база заметок.
Чтобы получить информацию о командах приложения, наберите в командной строке
`help`.

"""
COPYRIGHT: str = """
---
### &copy; Nobus, 2022

"""
HOWTO: str = """
Инструкции по редактированию текста:

- `howto-md`(`-wm`) - использование в тексте элементов разметки Markdown
- `howto-hotkeys`(`-wk`) - комбинации клавиш для редактирования текста

"""
VIEW: str = """
`view` используется для показа команд просмотра заметок:

- `view-recent`(`-vr`) - просмотр последней (по времени создания) заметки
- `view-last`(`-vl`) - просмотр последних 5 заметок
- `view-all`(`-va`) - просмотр всех заметок
- `count`(`-c`) - количество заметок в базе

"""
EDIT: str = """
`edit` показывает команды по редактированию существующих заметок:

- `edit-title`(`-et`) - редактирование заголовка
- `edit-text`(`-ex`) - редактирование основного текста (тела) заметки
- `edit-tag`(`-eg`) - редактирование тега заметки

"""
DEL: str = """
`del` показывает команды по удалению заметок из базы:

- `del-memo`(`-dm`) - удаление заметки из базы (по ID)
- `del-all`(`-da`) - удаление всех заметок из базы

"""
SEARCH: str = """
`search` показывает команды поиска заметок в базе:

- `search-id`(`-si`) - поиск заметки по ID
- `search-date`(`-sd`) - поиск заметки по дате создания (редактирования)
- `search-title`(`-st`) - поиск заметки по заголовку
- `search-text`(`-sx`) - поиск заметки по основному тексту (телу)
- `search-tag`(`-sg`) - поиск заметки по тегу

"""
BACKUP: str = """
`backup` показывает команды резервного копирования и восстановления:

- `backup-db`(`-bd`) - создание резервной копии базы заметок
- `restore-db`(`-od`) - восстановление базы заметок из резервной копии
- `check-db`(`-kd`) - проверка целостности базы заметок
- `recreate-db`(`-ed`) - пересоздание базы заметок
- `clear`(`-r`) - удаление всех данных (включая папку программы)

"""
CLEAR: str = (
    """
Все данные очищены, работа приложения **`MemoPad`** завершена.
"""
    + COPYRIGHT
)
