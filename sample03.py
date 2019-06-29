"""
目標; usersのusersテーブルからうまいことデータをとってきて

Bobさんは15歳です
Kenさんは27歳です
Tomさんは77歳です

って出力する
"""
import sqlite3


def main():
    conn = sqlite3.connect("users.sqlite")
    cursor = conn.cursor()

    sql = "SELECT * FROM users"

    users = cursor.execute(sql)

    results = users.fetchall()

    for result in results:
        print(f"{result[0]}さんは{result[1]}歳です。")

    conn.commit()

    conn.close()


if __name__ == "__main__":
    main()
