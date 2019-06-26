import sqlite3

"""
目標:PytonでSQLを使ってテーブルをつくる
"""


def main():
    # DB接続
    conn = sqlite3.connect("users.sqlite")
    cursor = conn.cursor()

    # SQLの準備
    sql = """CREATE TABLE users (
                name TEXT,
                age INTEGER
                )"""

    # SQLの実行
    cursor.execute(sql)

    # コミット
    conn.commit()

    # 接続を切る
    conn.close()


if __name__ == "__main__":
    main()
