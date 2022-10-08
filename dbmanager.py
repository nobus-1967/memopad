"""Set path, check if database exists, backup and restore database."""
from pathlib import Path
from shutil import copy as db_copy

from mdprinter import print_md
from prompter import check_confirmation


def set_db_path() -> Path:
    """Create (in not exists) a directory and set path to store database."""
    home = Path.home()

    working_dir = home.joinpath('.memopad')
    working_dir.mkdir(parents=True, exist_ok=True)

    db = 'memos.db'
    path = working_dir.joinpath(db)

    return path


def set_backup_path(path: Path) -> Path:
    """Set path of database's backup."""
    working_dir = path.parent
    db = path.name
    path_backup = working_dir.joinpath(f'{db}.backup')

    return path_backup


def check_db(path: Path) -> bool:
    """Check if database of memos exists."""
    return path.exists() and path.is_file()


def check_backup(path: Path) -> bool:
    """Check if database of memos exists."""
    path_backup = set_backup_path(path)

    return path_backup.exists() and path_backup.is_file()


def backup_db(path: Path) -> None:
    """Backup database of memos."""
    path_backup = set_backup_path(path)

    print_md('Создать резервную копию базы заметок?')
    confirmation = check_confirmation()

    if confirmation == 'yes':
        db_backup = db_copy(path, path_backup)
        print_md(f'Резервная копия базы заметок создана: `{db_backup}`.')


def restore_db(path: Path) -> None:
    """Restore database from backup."""
    is_db = check_db(path)
    is_backup = check_backup(path)
    path_backup = set_backup_path(path)

    if is_backup:

        if is_db:
            print_md('Восстановить базу заметок c перезаписью файла?')
            confirmation: str = check_confirmation()

            if confirmation == 'yes':
                db_replaced_from_backup: Path = db_copy(path_backup, path)
                print_md(
                    f'База заметок `{db_replaced_from_backup}` '
                    + 'перезаписана из резервной копии.'
                )
        else:
            db_restored_from_backup: Path = db_copy(path_backup, path)
            print_md(
                f'База заметок `{db_restored_from_backup}` '
                + 'восстановлена из резервной копии.'
            )
    else:
        print_md('Резервная копия базы заметок не найдена!')


def remove_db(path: Path) -> None:
    """Delete old database and create new database."""
    is_db = check_db(path)

    if is_db:
        print_md('Удалить базу заметок?')
        confirmation = check_confirmation()

        if confirmation == 'yes':
            path.unlink()


def clear_data(path: Path) -> None:
    """Clear all data and remove working directory."""
    working_dir = path.parent
    backup_path = set_backup_path(path)
    is_db = check_db(path)
    is_backup = check_backup(path)

    print_md('Очистить все данные и удалить папку приложения?')
    confirmation = check_confirmation()

    if confirmation == 'yes':
        if is_db:
            path.unlink()
        if is_backup:
            backup_path.unlink()
        Path.rmdir(working_dir)
