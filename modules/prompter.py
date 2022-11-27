#!/usr/bin/env python3
"""Uses custom editable prompt from module `prompt-toolkit`."""
from prompt_toolkit import prompt
from prompt_toolkit.clipboard.pyperclip import PyperclipClipboard
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.formatted_text import ANSI

from modules.mdprinter import print_md

COMMANDS: list[str] = [
    'help',
    '-h',
    'view',
    '-v',
    'view-recent',
    '-vr',
    'view-last',
    '-vl',
    'view-all',
    '-va',
    'count',
    '-c',
    'add',
    '-a',
    'edit',
    '-e',
    'edit-title',
    '-et',
    'edit-text',
    '-ex',
    'edit-tag',
    '-eg',
    'del',
    '-d',
    'del-memo',
    '-dm',
    'del-all',
    '-da',
    'search',
    '-s',
    'search-id',
    '-si',
    'search-date',
    '-sd',
    'search-title',
    '-st',
    'search-text',
    '-sx',
    'search-tag',
    '-sg',
    'howto',
    '-w',
    'howto-md',
    '-wm',
    'howto-hotkeys',
    '-wk',
    'backup',
    '-b',
    'backup-db',
    '-bd',
    'restore-db',
    '-od',
    'check-db',
    '-kd',
    'recreate-db',
    '-ed',
    'clear',
    '-r',
    'quit',
    '-q',
]
CONFIRMATIONS: list[str] = ['yes', '-y', 'no', '-n']


def get_command() -> str:
    """Enters user's command.

    Returns:
        str: command for command-line interpreter using autocomplete
        from module `prompt-toolkit`.

    """
    command_completer = WordCompleter(COMMANDS)

    command: str = prompt(
        ANSI('\033[34;1mmemopad\033[0m ' '\033[31;1m>>>\033[0m '),
        completer=command_completer,
    )

    return command


def check_command() -> str:
    """Checks user's command.

    Returns:
        str: command for command-line interpreter
        if command returned by function `get_command` is valid;
        otherwise user's input repeats in loop.

        Valid commands is listed in `COMMANDS`.

    """
    command = get_command().strip().lower()

    while command not in COMMANDS:
        print_md('Такой команды нет, обратитесь к `help`!')
        command = get_command().strip()

    return command


def confirm_command() -> str:
    """Confirms or cancel operations with database.

    Returns:
        str: confirmation command for command-line interpreter
        using autocomplete from module `prompt-toolkit`.

    """
    confirm_completer = WordCompleter(CONFIRMATIONS)

    command: str = prompt(
        ANSI(
            '\033[31;1m(\033[0m'
            '\033[34;1myes\033[0m'
            '\033[32;1m/\033[0m'
            '\033[34;1mno\033[0m'
            '\033[31;1m)\033[0m '
        ),
        completer=confirm_completer,
    )

    return command


def check_confirmation() -> str:
    """Checks user's confirmation command.

    Returns:
        str: confirmation command for command-line interpreter
        if confirmation command returned by function `get_command` is valid;
        otherwise user's input repeats in loop.

        Valid confirmation commands is listed in `CONFIRMATIONS`.

    """
    confirmation = confirm_command().strip().lower()

    while confirmation not in CONFIRMATIONS:
        print_md('Неправильный ввод, введите `yes` или `no`!')
        confirmation = confirm_command().strip().lower()

    return confirmation


def get_rowid() -> int:
    """Enters user's choice to choose memo's ROWID.

    Returns:
        int: memo's rowid entered by user.

    Raises:
        ValueError: If rowid is less than 0.

        In that case returns 0.

    """
    try:
        print_md('Введите `ID` заметки:')
        rowid = int(
            prompt(
                ANSI(
                    '\033[31;1m(\033[0m'
                    '\033[34;1mID\033[0m'
                    '\033[31;1m)\033[0m '
                )
            )
        )
        if rowid <= 0:
            raise ValueError

    except ValueError:
        rowid = 0

        return rowid
    else:
        return rowid


def get_new_title() -> str:
    """Prompts to enter title for new memo.

    Returns:
        str: user's input - title for creating memo.

    """
    new_title = prompt(ANSI('\033[32;1m##\033[0m '))

    return new_title


def get_new_text() -> str:
    """Prompts to enter text of body for new memo.

    Returns:
        str: user's input - multi-line text for creating memo.

    """
    new_text = prompt(ANSI('\033[32;1mТекст\033[0m '), multiline=True)

    return new_text


def get_new_tag() -> str:
    """Prompts to enter tag(s) for new memo.

    Returns:
        str: user's input - tag(s) for creating memo.

    """
    new_tag = prompt(ANSI('\033[32;1m#\033[0m'))

    return new_tag


def get_title_to_edit() -> str:
    """Prompts to enter title to edit or replace.

    Returns:
        str: user's input - new or corrected title for existing memo.

    """
    title_to_edit = prompt(
        ANSI('\033[32;1m##\033[0m '), clipboard=PyperclipClipboard()
    )

    return title_to_edit


def get_text_to_edit() -> str:
    """Prompts to enter text of body to edit or replace.

    Returns:
        str: user's input - new or corrected text for existing memo.

    """
    text_to_edit = prompt(
        ANSI('\033[32;1mТекст\033[0m '),
        multiline=True,
        clipboard=PyperclipClipboard(),
    )

    return text_to_edit


def get_tag_to_edit() -> str:
    """Prompts to enter tag(s) to edit or replace.

    Returns:
        str: user's input - new or corrected tag(s) for existing memo.

    """
    tag_to_edit = prompt(
        ANSI('\033[32;1m#\033[0m'), clipboard=PyperclipClipboard()
    )

    return tag_to_edit


def get_date_to_search() -> str:
    """Prompts to enter memo's date to search.

    Returns:
        str: user's input - date of existing memo.

    """
    date_to_search = prompt(
        ANSI(
            '\033[31;1m(\033[0m'
            '\033[34;1mГГГГ\033[0m'
            '\033[32;1m-\033[0m'
            '\033[34;1mММ\033[0m'
            '\033[32;1m-\033[0m'
            '\033[34;1mДД\033[0m'
            '\033[31;1m)\033[0m '
        )
    )

    return date_to_search


def get_title_to_search() -> str:
    """Prompts to enter memo's title to search.

    Returns:
        str: user's input - existing memo's title (part of title).

    """
    title_to_search = prompt(
        ANSI(
            '\033[31;1m(\033[0m'
            '\033[32;1m##\033[0m '
            '\033[34;1mЗаголовок\033[0m'
            '\033[31;1m)\033[0m '
        )
    )

    return title_to_search


def get_text_to_search() -> str:
    """Prompts to enter text in memo's body to search.

    Returns:
        str: user's input - part (keyword) of existing memo's body.

    """
    text_to_search = prompt(
        ANSI(
            '\033[31;1m(\033[0m' '\033[34;1mТекст\033[0m' '\033[31;1m)\033[0m '
        )
    )

    return text_to_search


def get_tag_to_search() -> str:
    """Prompts to enter memo's tag to search.

    Returns:
        str: user's input - existing memo's tag(s).

    """
    tag_to_search = prompt(
        ANSI(
            '\033[31;1m(\033[0m'
            '\033[32;1m#\033[0m'
            '\033[34;1mtag\033[0m'
            '\033[31;1m)\033[0m '
        )
    )

    return tag_to_search
