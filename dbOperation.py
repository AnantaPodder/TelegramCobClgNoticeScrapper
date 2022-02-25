import pymysql.cursors
from config import host, user, password, database


def getter():
    connection = pymysql.connect(
        host=host,
        user=user,
        password=password,
        database=database,
    )

    with connection.cursor() as cursor:
        cmd = "SELECT * FROM `noticeId`;"
        cursor.execute(cmd)

        temp = [item[0] for item in cursor.fetchall()]
        return temp

    connection.close()


def setter(id):
    connection = pymysql.connect(
        host=host,
        user=user,
        password=password,
        database=database,
    )

    with connection.cursor() as cursor:
        cmd = f"INSERT INTO `noticeId` (`id`) VALUES ('{id}');"
        cursor.execute(cmd)

    connection.commit()
    connection.close()
