# Лабораторная работа №2

## Цель работы:
Спроектировать и разработать систему для анонимного общения в сети интернет. Интерфейс системы должен представлять собой веб-страницу с лентой заметок, отсортированных в обратном хронологическом порядке и форму добавления новой заметки.

## Возможности:
- добавление заметок
- реакция на заметки (лайк/дизлайк)
- добавление комментария
- удаление заметки
## Пользовательский интерфейс
![Интерфейс](https://github.com/AnnyMars/OPLab2/blob/main/ПользовательскийИнтерфейс.png)
## Описание API сервера и его хореографии
Запрос при создании записи

![](https://github.com/AnnyMars/OPLab2/blob/main/ЗапросПост.png)

Запрос при написании комментария

![](https://github.com/AnnyMars/OPLab2/blob/main/ЗапросКоммент.png)

Запрос для реакции

![](https://github.com/AnnyMars/OPLab2/blob/main/ЗапросЛайк.png)

Запрос для удаления записи

![](https://github.com/AnnyMars/OPLab2/blob/main/ЗапросУдаление.png)
## Описание структуры базы данных
Для хранения данных используется sqlite3. Используется 2 таблицы: в первой хранятся сами посты и лайки к ним, во второй таблицы отдельно хранятся комментарии к постам. Комментарии связаны с каждым постом с помощью id

## Блок-схема алгоритма
![](https://github.com/AnnyMars/OPLab2/blob/main/блок-схема.png)


