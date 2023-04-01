# Пояснювальна записка та висновок до лабораторного практикуму

Результатом лабораторного практикуму для 3 країн (згідно з варіантом з файлу [tasks.csv](labs/lab7/tasks.csv))

1. Bermuda
2. France
3. Panama

є наступні матеріали.

## Кодова база

### Python code

- [script_convert](labs/lab7/samples/script_convert.py)


### Jupiter Notebooks

- [jnb hello world](src/hello_world.jnb)
- [jnb sample](labs/lab7/samples/sample.ipynb)


#### Scripts
Для запуску докера з Jupiter Notebook.
- [bash example_10_start_docker_compose_study_jupyter](labs/lab7/example_10_start_docker_compose_study_jupyter.sh)


### Файли

#### Вхідні дані (разархівовані та сконвертовані дані) з архівів:

- [oil-prices.zip](labs/lab7/datasets/oil-prices.zip)
- [population.zip](labs/lab7/datasets/population.zip)
- [ppp.zip](labs/lab7/datasets/ppp.zip)

Архіви були розпаковані в папку [data](labs/lab7/data/), з них були скопійовані файли csv-формату у папку [src](labs/lab7/src/).

##### file 1

- CSV: [file 1](labs/lab7/src/oil-prices/brent-daily.csv)
- JSON: [file 1](labs/lab7/src/oil-prices/brent-daily.json)
- XLSX [file 1](labs/lab7/src/oil-prices/brent-daily_pandas.xlsx)

Крім brent-daily.csv, також були розпаковані та сконвертовані у формати .csv, .json, .xlsx інші файли, такі як: 
- brent-monthly.csv, brent-weekly.csv, brent-year.csv, 
- wti-daily.csv, wti-monthly.csv, wti-weekly.csv, wti-year.csv.

##### file 2

- CSV: [file 1](data/file1link1.csv)
- JSON: [file 1](data/file1link1.json)
- XLSX [file 1](data/file1link1.xlsx)

##### file 3

- CSV: [file 1](data/file1link1.csv)
- JSON: [file 1](data/file1link1.json)
- XLSX [file 1](data/file1link1.xlsx)

#### Сгенеровані нові дані

##### table 1

- [table 1](data/file1link1.csv)
- [table 1](data/file1link1.xlsx)
- [table 1](data/file1link1.json)

##### table 2

- [table 1](data/file1link1.csv)
- [table 1](data/file1link1.xlsx)
- [table 1](data/file1link1.json)

#### Графіки

- [img 1](src/file1link1.jnb)
- [img 2](img/file1link2.png)
- [img 2](img/file1link2.jpg)

---

## Інструкція до роботи

1. Запускаемо [программу 1](src/hello_world.py).
2. Результат программи 1:
    1. ...
    2. ...
    3. ...
3. Виконуємо код програми 2 в ноутбук ...
4. Результат программи 2
    1. ...
    2. ...
    3. ...
       ...
