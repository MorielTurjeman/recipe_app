
import pymysql

connection = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    db="recipes_app",
    charset="utf8",
    cursorclass=pymysql.cursors.DictCursor
)


def get_dairy_ing():
    try:
        with connection.cursor() as cursor:
            dairy_query = f"select * from dairy_ing"
            cursor.execute(dairy_query)
            result = cursor.fetchall()
            return ([item["name"] for item in result])

    except Exception as e:
        return e


def get_gluten_ing():
    try:
        with connection.cursor() as cursor:
            gluten_query = f"select * from gluten_ing"
            cursor.execute(gluten_query)
            result = cursor.fetchall()
            return ([item["name"] for item in result])

    except Exception as e:
        return e
