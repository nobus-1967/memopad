"""Connects to SQLite-database and process data (memos)."""
from datetime import datetime
from pathlib import Path
from sqlite3 import connect, DatabaseError

from pyperclip import copy as copy_to_clipboard

from modules.dbmanager import check_db, check_backup, set_backup_path
from modules.dbmanager import restore_db
from modules.mdprinter import print_memo_from_db, print_md, print_total
from modules.memoeditor import input_corrected_body
from modules.memoeditor import input_corrected_title, input_corrected_tag
from modules.prompter import check_confirmation, get_rowid
from modules.prompter import get_date_to_search
from modules.prompter import get_title_to_search, get_text_to_search
from modules.prompter import get_tag_to_search


def check_db_path_and_table(path: Path) -> None:
    """Checks database's path and creates DB if not exists.

    Note:
        If database's backup exist, restores database from backup.

     Args:
         path (Path): PosixPath of program's working directory.

    """
    is_db = check_db(path)

    if is_db:
        print_md(f'Существующая база заметок: `{path}`.')
    else:
        is_backup = check_backup(path)

        if is_backup:
            path_backup = set_backup_path(path)

            print_md(f'База заметок `{path}` не найдена!')
            print_md(
                'Восстановить базу заметок из резервной копии '
                + f'`{path_backup}`?'
            )
            confirmation = check_confirmation()

            if confirmation == 'yes':
                restore_db(path)
        else:
            create_db(path)


def create_db(path: Path) -> None:
    """Creates empty DB of memos if not exists using SQL-query.

    Args:
        path (Path): PosixPath of program's working directory.

    Raises:
        DatabaseError: If operation failed.

    """
    connection = connect(path)
    cursor = connection.cursor()

    sql_create_table = """CREATE TABLE IF NOT EXISTS memos
                               (
                               date_time DATETIME NOT NULL,
                               titles TEXT NOT NULL,
                               bodies TEXT NOT NULL,
                               tags TEXT NOT NULL
                               );"""

    try:
        print_md(f'Будет создана новая база заметок: `{path}`.')
        cursor.execute(sql_create_table)
        connection.commit()

    except DatabaseError:
        print_md('Ошибка обращения к базе заметок.')
    finally:
        connection.close()


def show_recent(path: Path) -> None:
    """Shows the latest memo using SQL-query.

    Args:
        path (Path): PosixPath of program's working directory.

    Raises:
        DatabaseError: If operation failed.

    """
    connection = connect(path)
    cursor = connection.cursor()

    sql_select_latest = """SELECT ROWID, date_time, titles, bodies, tags
                                  FROM memos
                                  ORDER BY ROWID DESC;"""

    try:
        cursor.execute(sql_select_latest)
        memo = cursor.fetchone()

        if memo:
            print_md('Последняя заметка:')
            print_memo_from_db(memo)
        else:
            print_md('Заметка в базе не найдена.')

    except DatabaseError:
        print_md('Ошибка обращения к базе заметок.')
    finally:
        connection.close()


def show_last(path: Path) -> None:
    """Shows last 5 memos using SQL-query.

    Args:
        path (Path): PosixPath of program's working directory.

    Raises:
        DatabaseError: If operation failed.

    """
    connection = connect(path)
    cursor = connection.cursor()

    sql_select_last = """SELECT ROWID, date_time, titles, bodies, tags
                             FROM memos
                             ORDER BY ROWID DESC;"""
    try:
        cursor.execute(sql_select_last)
        memos = cursor.fetchmany(5)

        if memos:
            print_md('Последние заметки:')
            for memo in memos:
                print_memo_from_db(memo)
        else:
            print_md('Заметки в базе не найдены.')

    except DatabaseError:
        print_md('Ошибка обращения к базе заметок.')
    finally:
        connection.close()


def show_all(path: Path) -> None:
    """Show all memos using SQL-query.

    Args:
        path (Path): PosixPath of program's working directory.

    Raises:
        DatabaseError: If operation failed.

    """
    connection = connect(path)
    cursor = connection.cursor()

    sql_select_all = """SELECT ROWID, date_time, titles, bodies, tags
                             FROM memos
                             ORDER BY ROWID;"""

    try:
        cursor.execute(sql_select_all)
        memos = cursor.fetchall()

        if memos:
            print_md('Все заметки из базы (по порядку создания):')
            for memo in memos:
                print_memo_from_db(memo)
        else:
            print_md('Заметки в базе не найдены.')

    except DatabaseError:
        print_md('Ошибка обращения к базе заметок.')
    finally:
        connection.close()


def show_total_memos(path: Path) -> None:
    """Shows total of memos in DB using functions `count_memos`, `print-memos`.

    Args:
        path (Path): PosixPath of program's working directory.

    """
    total = count_memos(path)

    print_total(total)


def add_memo(path: Path, memo: tuple[str, ...]) -> None:
    """Adds new memo to DB using SQL-query.

    Args:
        path (Path): PosixPath of program's working directory.
        memo (tuple[str, ...]): tuple contains memo's elements
        (date_time, title, body and tag).

    Raises:
        DatabaseError: If operation failed.

    """
    connection = connect(path)
    cursor = connection.cursor()

    sql_add_memo = """INSERT INTO memos (date_time, titles, bodies, tags)
                           VALUES (?, ?, ?, ?);"""

    try:
        cursor.execute(sql_add_memo, memo)
        connection.commit()
        print_md('Заметка добавлена в базу.')

    except DatabaseError:
        print_md('Ошибка обращения к базе заметок.')
    finally:
        connection.close()


def edit_title(path: Path) -> None:
    """Edits title of existing memo using SQL-query.

    Note:
        User can paste previous title from clipboard
        (function `copy_to_clipboard` is an alias to `pyperclip.copy`)
        and then edit it; or may enter new title.

        User have to confirm changes.

    Args:
        path (Path): PosixPath of program's working directory.

    Raises:
        DatabaseError: If operation failed.

    """
    connection = connect(path)
    cursor = connection.cursor()

    sql_select_title = """SELECT titles
                               FROM memos
                               WHERE ROWID = ?;"""
    sql_update_title = """UPDATE memos
                               SET date_time = ?, titles = ?
                               WHERE ROWID = ?;"""
    rowid = search_memo_by_rowid(path)
    total = count_memos(path)

    try:
        if 0 < rowid <= total:
            cursor.execute(sql_select_title, (rowid,))

            memo = cursor.fetchone()
            copy_to_clipboard(memo[0].lstrip('## '))

            updated_date_time, corrected_title = input_corrected_title()

            print_md('Сохранить заметку с отредактированным заголовком?')
            confirmation = check_confirmation()

            if confirmation == 'yes':
                cursor.execute(
                    sql_update_title,
                    (updated_date_time, corrected_title, rowid),
                )
                connection.commit()
                print_md('Заметка обновлена.')

    except DatabaseError:
        print_md('Ошибка обращения к базе заметок.')
    finally:
        connection.close()


def edit_body(path: Path) -> None:
    """Edits body of existing memo using SQL-query.

    Note:
        User can paste previous text from clipboard
        (function `copy_to_clipboard` is an alias to `pyperclip.copy`)
        and then edit it; or may enter new text.

        User have to confirm changes.

    Args:
        path (Path): PosixPath of program's working directory.

    Raises:
        DatabaseError: If operation failed.

    """
    connection = connect(path)
    cursor = connection.cursor()

    sql_select_body = """SELECT bodies
                              FROM memos
                              WHERE ROWID = ?;"""
    sql_update_body = """UPDATE memos
                               SET date_time = ?, bodies = ?
                               WHERE ROWID = ?;"""
    rowid = search_memo_by_rowid(path)
    total = count_memos(path)

    try:
        if 0 < rowid <= total:
            cursor.execute(sql_select_body, (rowid,))

            memo = cursor.fetchone()
            copy_to_clipboard(memo[0])

            updated_date_time, corrected_text = input_corrected_body()

            print_md('Сохранить заметку с отредактированным текстом?')
            confirmation = check_confirmation()

            if confirmation == 'yes':
                cursor.execute(
                    sql_update_body, (updated_date_time, corrected_text, rowid)
                )
                connection.commit()
                print_md('Заметка обновлена.')

    except DatabaseError:
        print_md('Ошибка обращения к базе заметок.')
    finally:
        connection.close()


def edit_tag(path: Path) -> None:
    """Edit tag(s) of existing memo using SQL-query.

    Note:
        User can paste previous tag(s) from clipboard
        (function `copy_to_clipboard` is an alias to `pyperclip.copy`)
        and then edit them; or may enter new tag(s).

        User have to confirm changes.

    Args:
        path (Path): PosixPath of program's working directory.

    Raises:
        DatabaseError: If operation failed.

    """
    connection = connect(path)
    cursor = connection.cursor()

    sql_select_tag = """SELECT tags
                              FROM memos
                              WHERE ROWID = ?;"""
    sql_update_tag = """UPDATE memos
                               SET date_time = ?, tags = ?
                               WHERE ROWID = ?;"""
    rowid = search_memo_by_rowid(path)
    total = count_memos(path)

    try:
        if 0 < rowid <= total:
            cursor.execute(sql_select_tag, (rowid,))

            memo = cursor.fetchone()
            copy_to_clipboard(
                ' '.join([tag.lstrip('#') for tag in memo[0].split()])
            )

            updated_date_time, corrected_tag = input_corrected_tag()

            print_md('Сохранить заметку с отредактированным тегом?')
            confirmation = check_confirmation()

            if confirmation == 'yes':
                cursor.execute(
                    sql_update_tag, (updated_date_time, corrected_tag, rowid)
                )
                connection.commit()
                print_md('Заметка обновлена.')

    except DatabaseError:
        print_md('Ошибка обращения к базе заметок.')
    finally:
        connection.close()


def delete_memo(path: Path) -> None:
    """Delete memo from database (by ROWID)."""
    connection = connect(path)
    cursor = connection.cursor()

    sql_delete_memo = """DELETE FROM memos
                              WHERE ROWID == ?;"""
    rowid = search_memo_by_rowid(path)
    total = count_memos(path)

    try:
        if 0 < rowid <= total:
            print_md(f'Удалить заметку с ID `{rowid}`?')
            confirmation = check_confirmation()

            if confirmation == 'yes':
                cursor.execute(sql_delete_memo, (rowid,))
                connection.commit()
                print_md('Заметка удалена из базы.')

    except DatabaseError:
        print_md('Ошибка обращения к базе заметок.')
    finally:
        connection.close()


def delete_all(path: Path) -> None:
    """Delete all memos from database using SQL-query.

    Note:
        User have to confirm operation.

    Args:
        path (Path): PosixPath of program's working directory.

    Raises:
        DatabaseError: If operation failed.

    """
    connection = connect(path)
    cursor = connection.cursor()

    sql_delete_all = """DELETE FROM memos;"""

    try:
        print_md('Удалить все заметки из базы?')
        confirmation = check_confirmation()

        if confirmation == 'yes':
            cursor.execute(sql_delete_all)
            connection.commit()
            print_md('Все заметки удалены из базы.')

    except DatabaseError:
        print_md('Ошибка обращения к базе заметок.')
    finally:
        connection.close()


def search_memo_by_date(path: Path) -> None:
    """Search memo in database (by date) using SQL-query.

    Args:
        path (Path): PosixPath of program's working directory.

    Raises:
        DatabaseError: If operation failed.

    """
    connection = connect(path)
    cursor = connection.cursor()

    sql_select_date = """SELECT ROWID, date_time, titles, bodies, tags
                              FROM memos
                              WHERE DATE(date_time) = ?;"""
    print_md(
        'Введите дату создания (редактирования) заметки '
        + 'в формате `ГГГГ-ММ-ДД`:'
    )
    date = get_date_to_search().strip()
    date_is_valid = check_date(date)

    while not date_is_valid:
        print_md(
            'Введите правильную дату создания (редактирования) заметки '
            + 'в формате `ГГГГ-ММ-ДД`:'
        )
        date = get_date_to_search().strip()
        date_is_valid = check_date(date)

    try:
        cursor.execute(sql_select_date, (date,))
        memos = cursor.fetchall()

        if memos:
            for memo in memos:
                print_memo_from_db(memo)
        else:
            if date == '':
                print_md('Дата не задана, заметка не найдена.')
            else:
                print_md(f'Заметка от `{date}` не найдена.')

    except DatabaseError:
        print_md('Ошибка обращения к базе заметок.')
    finally:
        connection.close()


def check_date(date: str) -> bool:
    """Checks user's date to search.

    Args:
        date (str): date to check (in format '%Y-%m-%d').

    Returns:
        bool: True if user's date is valid, False otherwise.

    """
    today = datetime.today().date()

    try:

        date_to_check = datetime.strptime(date, '%Y-%m-%d').date()
        delta = today - date_to_check

        if delta.total_seconds() < 0:
            print('Этот день ещё не наступил.', end=' ')
            raise ValueError

        return True

    except ValueError:
        print('Введена неверная дата!')

        return False


def search_memo_by_title(path: Path) -> None:
    """Searches memo in database (by title) using SQL-query.

    Note:
        To search, user have to input a string (title or keyword - part of it).

        The search is case-insensitive.

    Args:
        path (Path): PosixPath of program's working directory.

    Raises:
        DatabaseError: If operation failed.

    """
    connection = connect(path)
    connection.create_function('CASEFOLD', 1, lambda x: x.casefold())
    cursor = connection.cursor()

    sql_select_title = """SELECT ROWID, date_time, titles, bodies, tags
                               FROM memos
                               WHERE CASEFOLD(titles) LIKE ?;"""
    print_md('Введите фрагмент заголовка заметки:')
    title = get_title_to_search().strip()

    if title != '':
        title_to_search = f'%{title.casefold()}%'
    else:
        title_to_search = title

    try:
        cursor.execute(sql_select_title, (title_to_search,))
        memos = cursor.fetchall()

        if memos:
            for memo in memos:
                print_memo_from_db(memo)
        else:
            if title == '':
                print_md('Заголовок не задан, заметка не найдена.')
            else:
                print_md(f'Заметка с `{title}` в заголовке не найдена.')

    except DatabaseError:
        print_md('Ошибка обращения к базе заметок.')
    finally:
        connection.close()


def search_memo_by_text(path: Path) -> None:
    """Search memo in database (by text) using SQL-query.

    Note:
        To search, user have to input a string (word or phrase - part of text).

        The search is case-insensitive.

    Args:
        path (Path): PosixPath of program's working directory.

    Raises:
        DatabaseError: If operation failed.

    """
    connection = connect(path)
    connection.create_function('CASEFOLD', 1, lambda x: x.casefold())
    cursor = connection.cursor()

    sql_select_text = """SELECT ROWID, date_time, titles, bodies, tags
                              FROM memos
                              WHERE CASEFOLD(bodies) LIKE ?"""
    print_md('Введите фрагмент текста заметки:')
    text = get_text_to_search().strip()

    if text != '':
        text_to_search = f'%{text.casefold()}%'
    else:
        text_to_search = text

    try:
        cursor.execute(sql_select_text, (text_to_search,))
        memos = cursor.fetchall()

        if memos:
            for memo in memos:
                print_memo_from_db(memo)
        else:
            if text == '':
                print_md('Текст не задан, заметка не найдена.')
            else:
                print_md(f'Заметка с текстом `{text}` не найдена.')

    except DatabaseError:
        print_md('Ошибка обращения к базе заметок.')
    finally:
        connection.close()


def search_memo_by_tag(path: Path) -> None:
    """Search memo in database (by tag) using SQL-query.

    Note:
        To search, user have to input a word.

        The search is case-insensitive.

    Args:
        path (Path): PosixPath of program's working directory.

    Raises:
        DatabaseError: If operation failed

    """
    connection = connect(path)
    connection.create_function('CASEFOLD', 1, lambda x: x.casefold())
    cursor = connection.cursor()

    sql_select_tag = """SELECT ROWID, date_time, titles, bodies, tags
                             FROM memos
                             WHERE CASEFOLD(tags) LIKE ?;"""
    print_md('Введите фрагмент тега заметки:')
    tag = get_tag_to_search().strip()

    if tag != '':
        tag_to_search = f'%{tag.casefold()}%'
    else:
        tag_to_search = tag

    try:
        cursor.execute(sql_select_tag, (tag_to_search,))
        memos = cursor.fetchall()

        if memos:
            for memo in memos:
                print_memo_from_db(memo)
        else:
            if tag == '':
                print_md('тег не задан, заметка не найдена.')
            else:
                print_md(f'Заметка с `{tag}` в теге не найдена.')

    except DatabaseError:
        print_md('Ошибка обращения к базе заметок.')
    finally:
        connection.close()


def search_memo_by_rowid(path: Path) -> int:
    """Search memo in database (by rowid) using SQL-query.

    Note:
        To search, user have to input a correct number (rowid).

    Args:
        path (Path): PosixPath of program's working directory.

    Returns:
        int: a number > 0 if database is not empty;
        -1 if user's input is not valid of raises DatabaseError.

    Raises:
        DatabaseError: If operation failed.

    """
    connection = connect(path)
    cursor = connection.cursor()

    sql_select_rowid = """SELECT ROWID, date_time, titles, bodies, tags
                               FROM memos
                               WHERE ROWID = ?;"""
    rowid = get_rowid()

    try:
        if rowid != 0:
            cursor.execute(sql_select_rowid, (rowid,))
            memo = cursor.fetchone()

            if memo:
                print_memo_from_db(memo)
            else:
                print_md(f'Заметка с `ID` {rowid} не найдена.')

                rowid = -1
        else:
            print_md('Неверный ввод `ID`.')

            rowid = -1

    except DatabaseError:
        print_md('Ошибка обращения к базе заметок.')

        rowid = -1
    finally:
        connection.close()

        return rowid


def count_memos(path: Path) -> int:
    """Show a number of memos in DB sing SQL-query.

    Args:
        path (Path): PosixPath of program's working directory.

    Returns:
        int: a number of existing memos in database.

    Raises:
        DatabaseError: If operation failed.

    """
    connection = connect(path)
    cursor = connection.cursor()

    sql_select = """SELECT * FROM memos;"""
    total = 0

    try:
        cursor.execute(sql_select)
        total = len(cursor.fetchall())

    except DatabaseError:
        print_md('Ошибка обращения к базе заметок.')

    finally:
        connection.close()

        return total


def check_db_integrity(path: Path) -> None:
    """Check integrity of database using SQL-query.

    Note:
        Uses SQLite's query `PRAGMA integrity_check`.

    Args:
        path (Path): PosixPath of program's working directory.

    Raises:
        DatabaseError: If operation failed.

    """
    connection = connect(path)
    cursor = connection.cursor()

    sql_integrity_check = """PRAGMA integrity_check;"""

    try:
        cursor.execute(sql_integrity_check)
        result = cursor.fetchone()[0]

        if result == 'ok':
            print_md(f'База заметок `{path}` в порядке!')
            print_md(
                'Если всё же обратиться к ней не удалось, '
                + 'попробуйте восстановить её из резервной копии '
                + '(`restore-db`) или пересоздать (`recreate-db`).'
            )
        else:
            print_md(f'База заметок `{path}` повреждена!')
            print_md(
                'Попробуйте восстановить её из резервной копии '
                + '(`restore-db`) или пересоздать (`recreate-db`).'
            )

    except DatabaseError:
        print_md('Ошибка обращения к базе заметок.')
        print_md(
            'Попробуйте восстановить её из резервной копии '
            + '(`restore-db`) или пересоздать (`recreate-db`).'
        )
    finally:
        connection.close()
