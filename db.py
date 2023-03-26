import sqlite3


def create_table():
    conn = sqlite3.connect('settings.db')
    cur = conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS settings(
       base_url TEXT,
       token TEXT,
       secret TEXT,
       language TEXT);
    """)
    conn.commit()
    conn.close()


def add_record(b_url: str, token: str, secret: str, language: str):
    conn = sqlite3.connect('settings.db')
    cur = conn.cursor()
    cur.execute("""INSERT INTO settings(base_url, token, secret, language)
        VALUES(?, ?, ?, ?)""", (b_url, token, secret, language))
    conn.commit()

    conn.close()
