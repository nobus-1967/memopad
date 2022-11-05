"""Sets path, check if database exists, backup and restore database."""
from pathlib import Path
from shutil import copy as db_copy

from modules.mdprinter import print_md
from modules.prompter import check_confirmation


def set_db_path() -> Path:
    """Creates (in not exists) a directory and set path to store DB.

    Returns:
        Path: PosixPath of working directory.

    """
    home = Path.home()

    working_dir = home.joinpath('.memopad')
    working_dir.mkdir(parents=True, exist_ok=True)

    db = 'memos.db'
    path = working_dir.joinpath(db)

    return path


def set_backup_path(path: Path) -> Path:
    """Sets path of database's backup.

    Args:
        path (Path): PosixPath of program's working directory.

    Returns:
        Path: PosixPath of database's backup file.

    """
    working_dir = path.parent
    db = path.name
    path_backup = working_dir.joinpath(f'{db}.backup')

    return path_backup


def check_db(path: Path) -> bool:
    """Checks if DB of memos exists.

    Args:
        path (Path): PosixPath of program's working directory.

    Returns:
        bool: bool: True if path exists and backup is file, False otherwise.

    """
    return path.exists() and path.is_file()


def check_backup(path: Path) -> bool:
    """Checks if database's backup of memos exists.

    Args:
        path (Path): PosixPath of program's working directory.

    Returns:
        bool: True if path exists and backup is file, False otherwise.

    """
    path_backup = set_backup_path(path)

    return path_backup.exists() and path_backup.is_file()


def backup_db(path: Path) -> None:
    """Backups DB of memos.

    Args:
        path: PosixPath of program's working directory.

    """
    path_backup = set_backup_path(path)

    print_md('Создать резервную копию базы заметок?')
    confirmation = check_confirmation()

    if confirmation == 'yes':
        db_backup = db_copy(path, path_backup)
        print_md(f'Резервная копия базы заметок создана: `{db_backup}`.')


def restore_db(path: Path) -> None:
    """Restores DB from backup.

    Args:
        path (Path): PosixPath of program's working directory.

    """
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
    """Deletes existing DB and create new DB.

    Args:
        path (Path): PosixPath of program's working directory.

    """
    is_db = check_db(path)

    if is_db:
        print_md('Удалить базу заметок?')
        confirmation = check_confirmation()

        if confirmation == 'yes':
            path.unlink()


def clear_data(path: Path) -> None:
    """Clears all data and remove working directory.

    Args:
        path (Path): PosixPath of program's working directory.

    """
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
