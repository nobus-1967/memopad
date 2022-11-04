"""Creates new memo with date_time, title, body and tag."""
from datetime import datetime

from mdprinter import print_md
from prompter import get_new_title, get_new_text, get_new_tag
from prompter import get_title_to_edit, get_text_to_edit, get_tag_to_edit


def create_new_memo() -> tuple[str, ...]:
    """Creates new memo (as tuple) with date_time, title, body and tag.

    Returns:
        tuple[str, ...]: tuple contains memo's elements
        (date_time, title, body and tag).

    """
    memo = (set_datetime(), input_title(), input_body(), input_tag())

    return memo


def set_datetime() -> str:
    """Sets date_time of new memo.

    Returns:
        str: date_time of memo generated by module `datetime`.

    """
    now = datetime.now()

    return now.strftime('%Y-%m-%d %H:%M:%S')


def input_title() -> str:
    """Enters and returns title of new memo.

    Returns:
        str: title of memo using function `get_new_title`.

        If user does not enter any own title,
        then default title from variable `no_title` is returned.

    """
    no_title = '## [Без заголовка]'

    print_md('Введите заголовок или просто нажмите `ENTER`:')
    title = get_new_title().strip()

    if title:
        title = f'## {title}'
    else:
        title = no_title

    return title


def input_body() -> str:
    """Enters and returns text of new memo.

    Returns:
        str: text of memo using function `get_new_text`.

        If user does not enter any own text,
        then default text from variable `no_text` is returned.

    """
    no_text = '[Пустая заметка]'

    print_md('Напишите заметку, для выхода нажмите `ESC` и затем `ENTER`:')
    text = get_new_text().strip()

    if not text:
        text = no_text

    return text


def input_tag() -> str:
    """Enters and returns tag(s) of new memo.

    Returns:
        str: tag(s) of memo using function `get_new_tag`.

        User can enter several tags divided by spaces.

        If user does not enter any own tag,
        then default tag from variable `no_tag` is returned.

    """
    no_tag = '#no_tag'

    print_md(
        'Введите тег (теги, разделённые пробелами) или просто нажмите '
        '`ENTER`:'
    )
    tags = get_new_tag().strip()

    if tags:
        tags = ' '.join([f'#{tag.strip()}' for tag in tags.split(' ') if tag])
    else:
        tags = no_tag

    return tags


def input_corrected_title() -> tuple[str, str]:
    """Pastes (from clipboard) and corrects title of existing memo.

    Returns:
        str: new or corrected title of memo using function `get_title_to_edit`.

        Title's text can be inserted from clipboard (`CTRL+Y`) and then
        edited by user.

        If user does not enter any own title,
        then default title from variable `no_title` is returned.

    """
    no_title = '## [Без заголовка]'

    print_md(
        'Вставьте прежний текст из буфера (`CTRL+Y`) и внесите в него '
        + 'исправления, затем нажмите `ENTER`:'
    )
    corrected_title = get_title_to_edit().strip()

    if corrected_title:
        corrected_title = f'## {corrected_title}'
    else:
        corrected_title = no_title

    updated_date_time = set_datetime()

    return updated_date_time, corrected_title


def input_corrected_body() -> tuple[str, str]:
    """Pastes (from clipboard) and corrects text of existing memo.

    Returns:
        str: new or corrected text of memo using function `get_text_to_edit`.

        Text of memo's body can be inserted from clipboard (`CTRL+Y`) and then
        edited by user.

        If user does not enter any own text,
        then default text from variable `no_text` is returned.

    """
    no_text = '[Пустая заметка]'

    print_md(
        'Вставьте прежний текст из буфера (`CTRL+Y`) и внесите в него '
        + 'исправления, для выхода нажмите `ESCAPE` и затем `ENTER`:'
    )
    corrected_text = get_text_to_edit().strip()

    if not corrected_text:
        corrected_text = no_text

    updated_date_time = set_datetime()

    return updated_date_time, corrected_text


def input_corrected_tag() -> tuple[str, str]:
    """Pastes (from clipboard) and corrects tag of existing memo.

    Returns:
        str: new or corrected tag(s) of memo using function `get_tag_to_edit`.

        User can enter several tags divided by spaces.

        Tag(s) can be inserted from clipboard (`CTRL+Y`) and then
        edited by user.

        If user does not enter any own tag,
        then default tag from variable `no_tag` is returned.
    """
    no_tag = '#no_tag'

    print_md(
        'Вставьте прежний тег или теги из буфера (`CTRL+Y`) и внесите '
        + 'исправления, затем нажмите `ENTER`:'
    )
    corrected_tags = get_tag_to_edit().strip()

    if corrected_tags:
        corrected_tags = ' '.join(
            [f'#{tag.strip()}' for tag in corrected_tags.split(' ') if tag]
        )
    else:
        corrected_tags = no_tag

    updated_date_time = set_datetime()

    return updated_date_time, corrected_tags
