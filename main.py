#!/usr/bin/env python3
"""MemoPad - CLI program using SQLite to store memos (version 1.2.0)."""
import sys

from prompt_toolkit.shortcuts import set_title

from help.commandshelp import COMMANDS
from modules.dbmanager import set_db_path
from modules.dbmanager import backup_db, remove_db, restore_db, clear_data
from help.howtokeys import HOTKEYS
from help.howtomd import MARKDOWN
from modules.mdprinter import print_new_memo, print_md
from modules.memoeditor import create_new_memo
from help.messages import HOWTO, VIEW, EDIT, DEL, SEARCH, BACKUP
from help.messages import TITLE, INFO, COPYRIGHT, CLEAR
from modules.prompter import check_command
from modules.sqlconnector import add_memo, delete_memo, delete_all
from modules.sqlconnector import check_db_integrity, check_db_path_and_table
from modules.sqlconnector import create_db
from modules.sqlconnector import edit_title, edit_body, edit_tag
from modules.sqlconnector import search_memo_by_rowid, search_memo_by_date
from modules.sqlconnector import search_memo_by_tag
from modules.sqlconnector import search_memo_by_title, search_memo_by_text
from modules.sqlconnector import show_recent, show_last, show_all
from modules.sqlconnector import show_total_memos


def main() -> None:
    """Memopad - CLI program using SQLite to store memos: main module.

    Runs commands in a command-line interpreter.

    Note:
        Function `main` prompts user to create database's backup before exit.

    Example:
        memopad >>> help

    """
    set_title('MemoPad')

    print_md(TITLE)
    print_md(INFO)

    path = set_db_path()
    check_db_path_and_table(path)

    command = check_command()

    while command not in ['quit', '-q']:
        if command in ['help', '-h']:
            print_md(COMMANDS)
        elif command in ['howto', '-w']:
            print_md(HOWTO)
        elif command in ['howto-md', '-wm']:
            print_md(MARKDOWN)
        elif command in ['howto-hotkeys', '-wk']:
            print_md(HOTKEYS)

        elif command in ['view', '-v']:
            print_md(VIEW)
        elif command in ['view-recent', '-vr']:
            show_recent(path)
        elif command in ['view-last', '-vl']:
            show_last(path)
        elif command in ['view-all', '-va']:
            show_all(path)
        elif command in ['count', '-c']:
            show_total_memos(path)

        elif command in ['add', '-a']:
            memo = create_new_memo()
            print_new_memo(memo)
            add_memo(path, memo)

        elif command in ['edit', '-e']:
            print_md(EDIT)
        elif command in ['edit-title', '-et']:
            edit_title(path)
        elif command in ['edit-text', '-ex']:
            edit_body(path)
        elif command in ['edit-tag', '-eg']:
            edit_tag(path)

        elif command in ['del', '-d']:
            print_md(DEL)
        elif command in ['del-memo', '-dm']:
            delete_memo(path)
        elif command in ['del-all', '-da']:
            delete_all(path)

        elif command in ['search', '-s']:
            print_md(SEARCH)
        elif command in ['search-id', '-si']:
            search_memo_by_rowid(path)
        elif command in ['search-date', '-sd']:
            search_memo_by_date(path)
        elif command in ['search-title', '-st']:
            search_memo_by_title(path)
        elif command in ['search-text', '-sx']:
            search_memo_by_text(path)
        elif command in ['search-tag', '-sg']:
            search_memo_by_tag(path)

        elif command in ['backup', '-b']:
            print_md(BACKUP)
        elif command in ['backup-db', '-bd']:
            backup_db(path)
        elif command in ['restore-db', '-od']:
            restore_db(path)
        elif command in ['check-db', '-kd']:
            check_db_integrity(path)
        elif command in ['recreate-db', '-ed']:
            remove_db(path)
            create_db(path)

        elif command in ['clear', '-r']:
            clear_data(path)
            print_md(CLEAR)
            sys.exit()

        command = check_command()

    backup_db(path)
    print_md(COPYRIGHT)


if __name__ == '__main__':
    main()
