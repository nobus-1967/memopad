"""How-to edit text (in prompt to enter parts of new memo)."""

HOTKEYS: str = """
## Как редактировать вводимый текст заметки

При вводе заголовка, основного текста (тела) и тега заметки поддерживаются
следующие `горячие клавиши`:

### Перемещение курсора

* `CTRL+A` - перемещает курсор в *начало строки*
* `CTRL+E` - перемещает курсор в *конец строки*
* `CTRL+F` - перемещает курсор на *один символ вперед* (как и клавиша `->`)
* `CTRL+B` - перемещает курсор на *один символ назад* (как и клавиша `->`)
* `ALT+F` - перемещает курсор на *одно слово вперед*
* `ALT+B` - перемещает курсор на *одно слово назад*

### Редактирование текста

* `CTRL+D` - удаляет символ в *позиции курсора*
* `CTRL+T` - меняет местами *два символа* (в позиции курсора и предшествующий)
* `ALT+T` - меняет местами *два слова* (в позиции курсора и предшествующее)
* `ALT+L` - переводит в *нижний регистр* символы от курсора и до конца слова
* `ALT+U` - переводит в *верхний регистр* символы от курсора и до конца слова

### Удаление текста

* `CTRL+K` - удаляет символы от курсора до *конца строки*
* `CTRL+U` - удаляет символы от курсора до *начала строки*
* `ALT+D` - удаляет символы от курсора до *конца текущего слова*
* `ALT+BACKSPACE` - удаляет символы от курсора до *начала текущего слова*;
 (если курсор находится в начале слова, удаляет *предшествующее слово*)
* `CTRL+L` - очищает *весь текст*

"""
