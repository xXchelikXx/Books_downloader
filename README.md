# Парсер книг с сайта tululu.org

Этот проект нужен для того, чтобы скачивать книги и их обложки с сайта [tululu.org.](https://tululu.org)

### Как установить

Проект сделан на `Python`. Чтобы подготовить код нужно:

-Перенести код;

-В командной строке прописать `pip install requirements.txt`.

### Аргументы

В `--start_id` и `--end_id` хранятся `ID` книг с сайта [tululu.org](https://tululu.org). Чтобы запустить проект нужно прописать команду `python main.py` и аргументы с числами, например:

```
python main.py --start_id 10 --end_id 20
```

Скачаются книги с `ID` от 10 до 20(20 не входит).

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).