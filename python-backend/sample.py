from EMConnectionManager import connection


def showTables():
    cursor= connection.cursor()
    cursor.execute("show tables")

    for x in cursor:
        print(x)

