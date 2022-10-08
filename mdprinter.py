"""Print help and memos using Markdown markup language."""
from rich.console import Console
from rich.markdown import Markdown


def print_new_memo(memo: tuple) -> None:
    """Print memo using Markdown markup language."""
    console = Console()

    date_time, title, body, tag = memo

    console.print('')
    console.print(f'{date_time} {tag}')
    console.print(Markdown(title))
    console.print(Markdown(body))
    console.print('')


def print_memo_from_db(memo: tuple) -> None:
    """Print memo using Markdown markup language."""
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
    """Print help and messages using Markdown markup language."""
    console = Console()

    console.print(Markdown(text))


def print_total(total: int) -> None:
    """Print total of memos in DB."""
    console = Console()

    console.print(f'Всего заметок в базе: {total}.')
