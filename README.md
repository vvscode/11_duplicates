# Anti-Duplicator

Скрипт предназначен для рекурсивного поиска дубликатов файлов. 
Под понятие `дубликат` попадают файлы с одинаковым именем и одинаковым размером.

При запуске скрипта параметром ему нужно передать путь к папке для сканирования `python3 duplicates.py DIR_PATH`;

Примеры работы скрипта:

```
> python3 duplicates.py
Please pass directory as a param

> python3 duplicates.py 11234
Please pass correct directory name

> python3 duplicates.py 1
No dublicates detected

> python3 duplicates.py .
Next dublicates detected:
Group `test.1 with size 0`
./1/test.1
./3/test.1
./2/test.1
Group `HEAD with size 198`
./.git/logs/HEAD
./.git/logs/refs/remotes/origin/HEAD
```


# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
