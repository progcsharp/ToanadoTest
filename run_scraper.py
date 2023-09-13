import getopt

import requests
import sys
from bs4 import BeautifulSoup
from prettytable import PrettyTable


def parse() -> list: # Функция для запроса на сайт и получения списка строк таблицы
    request = requests.get("https://en.wikipedia.org/wiki/Python_(programming_language)#Typing") # get запрос на сайт
    site = request.text # Получение html сайта в string формате
    soup = BeautifulSoup(site, "html.parser") # Создание экземпляра класса BeautifulSoup
    table = soup.find("table", attrs={"class": "wikitable"}) # Поиск нужной таблици на сайте
    table_body = table.find('tbody') # Поиск элемента tbody в нужной таблице
    rows = table_body.find_all('tr') # Получение списка строк таблицы
    return rows # Возвращение списка строк таблицы


def output_table(): # Фунцкия для вывода таблицу в консоль
    rows = parse() # Вызов функции parse для получения списка строк таблицы
    th = ["Type", "Mutability", "Description", "Syntax examples"] # Создание списка названия столбцов
    table_out = PrettyTable(th) # Экземпляр класса PrettyTable
    for row in rows: # Цикл по строкам таблицы
        cols = row.find_all('td') # Поиск всех элеметнов td с строке таблицы
        cols = [ele.text.strip() for ele in cols] # Создание массива с данными строки таблицы
        if cols: # Проверка на пустоту массива
            table_out.add_row(cols) # Добавление данных строки в таблицу для вывода
    print(table_out) # Вывод таблицы


def database(): # Функция для записи данных в бд
    # import нужных функций
    from app.db.hendlers.create import create_collect_data
    from app.db.hendlers.delete import delete_collect_data

    delete_collect_data() # Вызов функции для удаление всех записей таблицы collect_data в бд

    rows = parse() # Вызов функции parse для получения списка строк таблицы

    for row in rows: # Цикл по строкам таблицы
        cols = row.find_all('td') # Поиск всех элеметнов td с строке таблицы
        cols = [ele.text.strip() for ele in cols] # Создание массива с данными строки таблицы
        if cols: # Проверка на пустоту массива
            create_collect_data(cols) # Фызов функции для записи данных в бд


def main(argv: list): # Функция для запуска парсера
    opts, args = getopt.getopt(argv, "dry_run:", ["dry_run="]) # Поиск параметра dry_run

    opt, arg = opts[0] #  Получеие параметра и апгрумента

    # Проверка параметра dry_run
    if opt == "--dry_run" and arg == "True":
        output_table() # Вызов функции для вывода данных в консоль
    elif opt == "--dry_run" and arg == "False":
        database() # Вызов функции для записи данных в бд
    else:
        print("error: no parameter dry_run\n--dry_run True: output table to console\n--dry_run False: writing a table to a database") # Вывод ошибки

main(sys.argv[1:])
