MemoPad
=======

**MemoPad** - CLI-программа для создания, редактирования и просмотра
заметок в терминале, использующая
`SQLite <https://www.sqlite.org>`__ как базу заметок.

Программа позволяет использовать в заметках форматирование (элементы
языка разметки
`Markdown <https://www.markdownguide.org/basic-syntax>`__).

Для многострочного ввода текста применяются возможности модуля
`Prompt Toolkit <https://github.com/prompt-toolkit/python-prompt-toolkit>`__.

Для копирования и вставки текста применяется модуль
`Pyperclip <https://pyperclip.readthedocs.io/en/latest>`__. В
**GNU/Linux** использование данного модуля может потребовать установку
одного из механизмов работы с буфером обмена: ``xsel``, ``xclip``,
``gtk`` или ``PyQt4``.

Список внешних заимствований содержится в файле ``requirements.txt``.

Для своей работы программа создаёт папку ``~/.memopad/``\ в домашнем
каталоге пользователя, где хранится база данных (``memos.db``) и
резервная копия базы данных (``memos.db.backup``).

О программе подробнее: `MemoPad — консольный редактор и SQLite-база
заметок <https://avshcherbina.ru/#memopad>`__

Автор программы: **Анатолий Щербина** (https://github.com/nobus-1967).

Версия программы: ``1.1.9``

Лицензия: `GNU General Public License
v3.0 <LICENSE.md>`__.
