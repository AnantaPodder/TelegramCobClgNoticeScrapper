import pymysql.cursors


def getter():
    connection = pymysql.connect(
        host="sql348.main-hosting.eu",
        user="u841345258_anantapodder",
        password="Ananta08@@",
        database="u841345258_cobClgNotice",
    )

    with connection.cursor() as cursor:
        cmd = "SELECT * FROM `noticeId`;"
        cursor.execute(cmd)

        temp = [item[0] for item in cursor.fetchall()]
        return temp

    connection.close()


def setter(id):
    connection = pymysql.connect(
        host="sql348.main-hosting.eu",
        user="u841345258_anantapodder",
        password="Ananta08@@",
        database="u841345258_cobClgNotice",
    )

    with connection.cursor() as cursor:
        cmd = f"INSERT INTO `noticeId` (`id`) VALUES ('{id}');"
        cursor.execute(cmd)

    connection.commit()
    connection.close()
