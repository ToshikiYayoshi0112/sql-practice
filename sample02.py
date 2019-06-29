"""
目標:users.sqliteにINSERT文を発行する
"""

import sqlite3


def main():
    conn = sqlite3.connect("users.sqlite")
    cursor = conn.cursor()

    sql = "INSERT INTO users (name, age) VALUES ('Ken', 77)"

    cursor.execute(sql)

    conn.commit()

    conn.close()


if __name__ == "__main__":
    main()
