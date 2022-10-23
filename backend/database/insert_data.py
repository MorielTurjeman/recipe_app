import pymysql
from db_connection import connection

dairy_ingredients = ["Cream", "Cheese", "Milk", "Butter",
                     "Creme", "Ricotta", "Mozzarella", "Custard", "Cream Cheese"]
gluten_ingredients = ["Flour", "Bread", "spaghetti", "Biscuits", "Beer"]


def insert_dairy_ing(name):
    try:
        with connection.cursor() as cursor:
            dairy_query = f"INSERT IGNORE into dairy_ing(name) values('{name}')"
            cursor.execute(dairy_query)
            connection.commit()

    except Exception as e:
        print(e)


def insert_gluten_ing(name):
    try:
        with connection.cursor() as cursor:
            gluten_query = f"INSERT IGNORE into gluten_ing(name) values('{name}')"
            cursor.execute(gluten_query)
            connection.commit()

    except Exception as e:
        print(e)


def insert_all_data():
    for name in dairy_ingredients:
        insert_dairy_ing(name)
    for name in gluten_ingredients:
        insert_gluten_ing(name)


# insert_all_data()
