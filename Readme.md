# MemoPad

## Информация о программе

**MemoPad** - CLI-программа для создания, редактирования и просмотра заметок в терминале, использующая [`SQLite`](https://www.sqlite.org) как базу заметок.

Программа позволяет использовать в заметках форматирование (элементы языка 
разметки [`Markdown`](https://www.markdownguide.org/basic-syntax)).

Для многострочного ввода текста применяются возможности модуля [`Prompt Toolkit`](https://github.com/prompt-toolkit/python-prompt-toolkit).

Для копирования и вставки текста применяется модуль [`Pyperclip`](https://pyperclip.readthedocs.io/en/latest). В **GNU/Linux** использование данного модуля может потребовать установку одного из механизмов работы с буфером обмена: `xsel`, `xclip`, `gtk` или `PyQt4`.

Список внешних заимствований содержится в файле `requirements.txt`.

Для своей работы программа создаёт папку `~/.memopad/`в домашнем каталоге пользователя, где хранится база данных (`memos.db`) и резервная копия базы данных (`memos.db.backup`).

О программе подробнее: [*MemoPad* — консольный редактор и SQLite-база  заметок](https://avshcherbina.ru/#memopad)

## Автор, текущая версия программы и лицензия

Автор программы: **Анатолий Щербина** (https://github.com/nobus-1967).

Версия программы: `1.2.0`

Лицензия: [GNU General Public License v3.0](LICENSE.md).

## Установка и удаление программы

### Установка программы (GNU/Linux):

1) клонировать на свой компьютер: `git clone https://github.com/nobus-1967/memopad.git` или скачать архив проекта и распаковать его: `wget https://github.com/nobus-1967/memopad/archive/refs/heads/main.zip && unzip main.zip`; 

2) перейти в папку проекта (для клона репозитория &mdash; `cd memopad`, для архива &mdash; `cd memopad-main`);

3) сделать исполняемым файл `install.sh` (`chmod u+x install.sh`) и запустить его (`./install.sh`);

4) при необходимости удалить репозиторий (`cd ~ && rm -rv memopad`) или архив и распакованную папку (`cd ~ && rm -rv memopad-main main.zip`);

5) перезапустить `Bash`: `source ~/.bashrc`; теперь программу можно запускать в терминале командой `memopad`.

### Удаление программы (GNU/Linux):

1) запустить `memopad`, командой `clear` удалить папку `~/.memopad/` в домашнем каталоге пользователя со всеми файлами; 

2) сделать исполняемым файл `uninstall.sh` из проекта (см. выше раздел об установке программы) и запустить его.
