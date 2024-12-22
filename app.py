import database.connection as conn
import pandas as pd
from flask import Flask, render_template, g
import sqlite3

app = Flask(__name__)


def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect('./database/gifts.db')
        g.db.row_factory = sqlite3.Row
    return g.db


@app.route('/')
def index():
    return '''
    <a href="http://localhost:5000/list">Список подарков</a><br>
    <a href="http://localhost:5000/describe">Описание таблицы</a>
    '''


@app.route('/list')
def test():
    try:
        db = get_db()
        sql = 'select * from list'
        df = pd.read_sql(sql, db)
        table_html = df.to_html(columns=df.columns.tolist(), index=False)
        return render_template('index.html', table=table_html)
    except Exception as e:
        return '<font color="red"><h1> Ошибка: '+str(e)+'</h1></font>'
    finally:
        db.close


@app.route('/describe')
def query():
    try:
        db = get_db()
        sql = 'SELECT * FROM sqlite_master'
        df = pd.read_sql(sql, db)
        table_html = df.to_html(columns=df.columns.tolist(), index=False)
        return render_template('index.html', table=table_html)
    except Exception as e:
        return '<font color="red"><h1> Ошибка: '+str(e)+'</h1></font>'
    finally:
        db.close


if __name__ == '__main__':
    connection = conn.init_connection()
    app.run(host='0.0.0.0')
