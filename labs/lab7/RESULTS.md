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

##### files 1.1 - 1.8 from folder 'src/oil-prices':

- CSV: [brent-daily.csv](labs/lab7/src/oil-prices/brent-daily.csv)
- JSON: [brent-daily.json](labs/lab7/src/oil-prices/brent-daily.json)
- XLSX [brent-daily.xlsx](labs/lab7/src/oil-prices/brent-daily_pandas.xlsx)

Крім brent-daily.csv, також були розпаковані та сконвертовані у формати .csv, .json, .xlsx інші файли, такі як: 
- brent-monthly.csv, brent-weekly.csv, brent-year.csv, 
- wti-daily.csv, wti-monthly.csv, wti-weekly.csv, wti-year.csv.

##### file 2 from folder 'src/population':

- CSV: [population.csv](labs/lab7/src/population/population.csv)
- JSON: [population.json](labs/lab7/src/population/population.json)
- XLSX [population_pandas.xlsx](labs/lab7/src/population/population_pandas.xlsx)

##### file 3 from folder 'src/ppp':

- CSV: [ppp-gdp.csv](labs/lab7/src/ppp/ppp-gdp.csv)
- JSON: [ppp-gdp.json](labs/lab7/src/ppp/ppp-gdp.json)
- XLSX [ppp-gdp_pandas.xlsx](labs/lab7/src/ppp/ppp-gdp_pandas.xlsx)

#### Сгенеровані нові дані

##### table 1 

- [data_population_1960_2020.csv](labs/lab7/samples/tables and graphs/data_population_1960_2020.csv)
- [table 1](data/file1link1.xlsx)
- [table 1](data/file1link1.json)

##### table 2

- [table 1](data/file1link1.csv)
- [table 1](data/file1link1.xlsx)
- [table 1](data/file1link1.json)

#### Графіки
- [line1_population.png](labs/lab7/samples/tables and graphs/line1_population.png)
- [line2_population.png](labs/lab7/samples/tables and graphs/line2_population.png)
- [pie_population.png](labs/lab7/samples/tables and graphs/pie_population.png)
- [bar_population.png](labs/lab7/samples/tables and graphs/bar_population.png)

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
