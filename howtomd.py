"""How-to for MemoPad (using Markdown in memos)."""
MARKDOWN: str = """
## Markdown

При написании заметок можно использовать элементы языка разметки Markdown,
такие как **полужирный шрифт** (слово выделяется с обеих сторон 
символами `**`) и *курсив* (выделяется с обеих сторон символом `*`).

Чтобы создать новый абзац, дважды нажмите `ENTER`.

Чтобы создать подзаголовок на новой строке, поставьте перед ним `###`:

### Подзаголовок

Цитата выделяется символом `>` перед ней:

> Цитата.

Нумерованный список создаётся цифрами (`1`, `2`, `3`...):
1. Один
2. Два
3. Три

Маркированный список создаётся символами (`*` или `+` или `-`):

* Утро
* День
* Вечер
* Ночь

Гиперссылка выделяется скобками `[` и `]`: [http://example.com/]

Горизонтальная линия-разделитель создаётся тремя символами (`***` или `---`):

---

Также в разметке Markdown можно использовать HTML-мнемоники, такие как:

* `&mdash;` (тире &mdash;),
* `&copy;` (знак охраны авторского права &copy;),
* `&laquo;` (левую, или открывающую двойную угловую кавычку &laquo;),
* `&raquo;` (правую, или закрывающую двойную угловую кавычку &raquo;),
* `&degree;` (знак градуса &deg;),
* `&pm;` (плюс-минус &pm;),
* `&euro;` (символ Евро &euro;),

неразрывный пробел `&nbsp;` и другие.

"""
