"""Prints help and memos using Markdown markup language."""
from rich.console import Console
from rich.markdown import Markdown


def print_new_memo(memo: tuple[str, ...]) -> None:
    """Prints creating memo (process Markdown using module `rich`).

    Args:
        memo (tuple[str, ...]): tuple contains memo's elements
        (date_time, title, body and tag).

    """
    console = Console()

    date_time, title, body, tag = memo

    console.print('')
    console.print(f'{date_time} {tag}')
    console.print(Markdown(title))
    console.print(Markdown(body))
    console.print('')


def print_memo_from_db(memo: tuple[str, ...]) -> None:
    """Prints memo from DB (process Markdown using module `rich`).

    Args:
        memo (tuple[str, ...]): tuple contains memo's elements
        (rowid, date_time, title, body and tag).

    """
    console = Console()

    (
        rowid,
        date_time,
        title,
        body,
        tag,
    ) = memo

    console.print('')
    console.print(f'{date_time} {tag} (ID: {rowid})')
    console.print(Markdown(title))
    console.print(Markdown(body))
    console.print('')


def print_md(text: str) -> None:
    """Prints help and messages (process Markdown using module `rich`).

    Args:
        text (str): multi-line strings of help and messages.

    """
    console = Console()

    console.print(Markdown(text))


def print_total(total: int) -> None:
    """Prints total of memos in DB.

    Args:
        total (int): total of existing memos in database.
    """
    console = Console()

    console.print(f'Всего заметок в базе: {total}.')
