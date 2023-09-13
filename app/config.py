import yaml

with open('app/config.yml', 'r') as file:
    config = yaml.safe_load(file) # Парсинг yaml файла в переменную config

