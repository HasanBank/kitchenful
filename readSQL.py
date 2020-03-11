import sqlite3
import connectSQL

def readAllProducts(sqliteConnection,cursor):

	sqlite_select_query = """SELECT * from products"""
	printResult(cursor,sqlite_select_query)

def getAmount(sqliteConnection,cursor,productName):
	#Todo Regex
	sqlite_select_query = " SELECT Amount, Amount_Unit from products where Name =  '%s'" %productName
	print(sqlite_select_query)
	printResult(cursor,sqlite_select_query)


def printResult(cursor,sqlite_select_query):
	cursor.execute(sqlite_select_query)
	result = cursor.fetchall()
	print("Result:  ", result)
	cursor.close()


def main():
	print('# Press enter the key #')
	print('To read all prodcuts: 1')
	print('To get amount of the product: 2')
	key = int(input())

	if key != 1 and key != 2:
		print('Please enter an acceptable key ')
		main()
	else:
		sqliteConnection,cursor = connectSQL.readSqliteTable()

		if key == 1:
			readAllProducts(sqliteConnection,cursor)
		if key == 2:
			productName = input('Please enter the product name: ')
			getAmount(sqliteConnection,cursor,productName)

		connectSQL.closeConnection(sqliteConnection)



if __name__ == '__main__':
	main()

