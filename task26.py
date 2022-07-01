#todo: Изучаем пакет pandas
#
# После установки библиотеки pandas выполните следующие действия:
#
# Изучите справку по модулю (для чего нужен модуль , какие возможности предоставляет)
# Найдите расположение директории модуля pandas и изучите его содержимое
# Получите список доступных атрибутов модуля pandas
# Импортируйте модуль pandas в исполняемый скрипт
# С помощью модуля pandas ознакомьтесь со структурой  DataFrame, фильтрации данных,
# загрузки данных из формата сsv (рассмотрите примеры статьи)
# Установите библиотеку matplotlib, создайте график на своем наборе данных.

#Опорная статья:  https://egorovegor.ru/pandas-obrabotka-i-analiz-dannyh-v-python/

# Изучаем пакет pandas
#
# После установки библиотеки pandas выполните следующие действия:
#
# Изучите справку по модулю (для чего нужен модуль , какие возможности предоставляет)
# Найдите расположение директории модуля pandas и изучите его содержимое
# Получите список доступных атрибутов модуля pandas
# Импортируйте модуль pandas в исполняемый скрипт
# С помощью модуля pandas ознакомьтесь со структурой  DataFrame, фильтрации данных,
# загрузки данных из формата сsv (рассмотрите примеры статьи)
# Установите библиотеку matplotlib, создайте график на своем наборе данных.

#Опорная статья:  https://egorovegor.ru/pandas-obrabotka-i-analiz-dannyh-v-python/

import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({
    'Страна': ['США', 'Китай', 'Япония', 'Великобритания', 'Россия'],
    '2017 год $': [20164.000, 10798.000, 9567.000, 2458.600, 513.478],
    '2018 год $': [21959.000, 11389.000, 10185.000, 2639.000, 49827.300],
    '2019 год $': [30000.000, 16250.630, 14259.517, 2681.230, 324.132],
}, index=['US', 'KIT', 'EA', 'UK', 'RU']
)

df.pivot(columns="Страна").plot(kind='barh')
plt.show()