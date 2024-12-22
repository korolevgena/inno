import sqlite3
import pandas as pd
import random


def create_db():
    names = [
        'Иван Иванов', 'Петр Петров', 'Сергей Сергеев', 'Алексей Алексеев',
        'Дмитрий Дмитриев', 'Светлана Светланова', 'Анна Аннан', 'Екатерина Екатерина',
        'Ольга Ольгова', 'Мария Мариева', 'Николай Николаев', 'Виктория Викторова',
        'Андрей Андреев', 'Татьяна Татянова', 'Анастасия Анастасиева', 'Евгений Евгеньев',
        'Станислав Станиславов', 'Ирина Ирищук', 'Георгий Георгиев', 'Яна Янкина'
    ]

    gifts = [
        'Книга', 'Часы', 'Игрушка', 'Набор для рисования',
        'Сертификат', 'Букет цветов', 'Парфюм', 'Курс обучения',
        'Смарт-часы', 'Наушники', 'Подарочная карта', 'Флешка',
        'Курс по кулинарии', 'Плед', 'Подарочный набор', 'Беспроводная колонка',
        'Сумка', 'Одежда', 'Подарок на выбор', 'Билеты на концерт'
    ]

    data = {
        'ФИО': random.choices(names, k=20),
        'Название подарка': random.choices(gifts, k=20),
        'Стоимость': [random.randint(500, 10000) for _ in range(20)],
        'Статус': random.choices(['Куплен', 'Не куплен'], k=20)
    }

    df = pd.DataFrame(data)

    return df


def init_connection():
    df = create_db()

    conn = sqlite3.connect(
        './database/gifts.db')
    df.to_sql('list', conn, if_exists='replace', index=False)

    return conn


def close_connection(connection):
    connection.close()
