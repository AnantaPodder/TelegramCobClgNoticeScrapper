import pymysql.cursors
from config import *


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
        connection.close()
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


### testing successful.


def dyno_usage_setter(time_to_add):
    a = 8  # temp variable for storing -1 or 0
    connection = pymysql.connect(
        host=host,
        user=user,
        password=password,
        database=database,
    )

    with connection.cursor() as cursor:
        a = 10
        cursor.execute(
            f"SELECT `dynosTime` from `dynoHourCounter` WHERE `DynoSL`='{DynoSL}';"
        )
        dynoSeconds = cursor.fetchone()[0]

        if dynoSeconds > 1944000:
            a = -1
            # more than 440 dyno hours used
        elif dynoSeconds > 1976400:
            a = -2
            # more than 449 dyno hours used
            # urget notice
        else:
            a = 0

        cmd = f"UPDATE `dynoHourCounter` SET `dynosTime`= (SELECT `dynosTime` from `dynoHourCounter` WHERE `DynoSL`='{DynoSL}')+{time_to_add} WHERE `DynoSL`='{DynoSL}';"
        cursor.execute(cmd)

    connection.commit()
    connection.close()
    return a


# put value of usage for opposite dyno zero
## successful test
def dyno_usage_reset():
    connection = pymysql.connect(
        host=host,
        user=user,
        password=password,
        database=database,
    )
    # cmd
    with connection.cursor() as cursor:

        if DynoSL == "1":
            cmd = f"UPDATE `dynoHourCounter` SET `dynosTime`= 0 WHERE `DynoSL`=2;"
            print("DynoSL=1")
        elif DynoSL == "2":
            cmd = f"UPDATE `dynoHourCounter` SET `dynosTime`= 0 WHERE `DynoSL`=1;"
            print("DynoSL=1")
        else:
            cmd = f"UPDATE `dynoHourCounter` SET `dynosTime`= '0' WHERE `DynoSL`='8';"
            print("error")
        cursor.execute(cmd)

    connection.commit()
    connection.close()
