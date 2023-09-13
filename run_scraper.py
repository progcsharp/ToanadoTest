import getopt

import requests
import sys
from bs4 import BeautifulSoup
from prettytable import PrettyTable


def parse() -> list:
    request = requests.get("https://en.wikipedia.org/wiki/Python_(programming_language)#Typing")
    site = request.text
    soup = BeautifulSoup(site, "html.parser")
    table = soup.find("table", attrs={"class": "wikitable"})
    table_body = table.find('tbody')
    rows = table_body.find_all('tr')
    return rows


def table():
    rows = parse()
    th = ["Type", "Mutability", "Description" ,"Syntax examples"]
    table_out = PrettyTable(th)
    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        if cols:
            table_out.add_row(cols)
    print(table_out)


def database():
    from app.db.hendlers.create import create_collect_data
    from app.db.hendlers.delete import delete_collect_data

    delete_collect_data()

    rows = parse()

    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        if cols:
            create_collect_data(cols)


def main(argv: list):
    opts, args = getopt.getopt(argv, "dry_run:", ["dry_run="])

    opt, arg = opts[0]
    if opt == "--dry_run" and arg == "True":
        table()
    elif opt == "--dry_run" and arg == "False":
        database()
    else:
        print("error")


main(sys.argv[1:])
