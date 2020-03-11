import sqlite3

def readSqliteTable():
    try:
        sqliteConnection = sqlite3.connect('kitchenful-db.db', timeout=20)
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        return sqliteConnection,cursor

    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)

def closeConnection(sqliteConnection):
	if (sqliteConnection):
            sqliteConnection.close()
            print("The Sqlite connection is closed")

