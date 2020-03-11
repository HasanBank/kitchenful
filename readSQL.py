import sqlite3
import connectSQL

def readAllProducts(sqliteConnection,cursor):
	sqlite_select_query = """SELECT * from products"""
	printOrExecuteSQL(cursor,sqlite_select_query,True)

def getAmount(sqliteConnection,cursor,productName):
	keyword = "%" + productName + "%"
	sqlite_select_query = " SELECT name,amount, amount_Unit from products where Name LIKE '%s'" %keyword
	printOrExecuteSQL(cursor,sqlite_select_query,True)

def getAmountOfIngredientsOfRecipe(sqliteConnection,cursor,recipeName):
	keyword = "%" + recipeName + "%"
	amountOfIngredients = "Amount of Ingredients"

	sqlite_select_query = " SELECT id from recipes where Name LIKE '%s'" %keyword
	sqlite_merged_query = " Select Count(recipes_ingredients.ingredient_id) as '%s' , recipes.name FROM recipes_ingredients INNER JOIN recipes ON recipes_ingredients.recipe_id = recipes.id Where recipes.id In (%s) GROUP BY recipes_ingredients.recipe_id " %(amountOfIngredients, sqlite_select_query)  
	
	printOrExecuteSQL(cursor,sqlite_merged_query,True)


def printOrExecuteSQL(cursor,sqlite_select_query,printResult):
	cursor.execute(sqlite_select_query)
	result = cursor.fetchall()
	if(printResult):
		print('### Result ###')
		print( [i[0] for i in cursor.description])
		print('\n'.join(str(e) for e in result))
	else:
		return result
	cursor.close()






def main():
	print('# Press enter the key #')
	print('To read all prodcuts: 1')
	print('To get amount of the product: 2')
	print('To get number of ingredients in the recipe: 3')
	key = int(input())

	if key != 1 and key != 2 and key != 3:
		print('Please enter an acceptable key ')
		main()
	else:
		sqliteConnection,cursor = connectSQL.readSqliteTable()

		if key == 1:
			readAllProducts(sqliteConnection,cursor)
		if key == 2:
			productName = input('Please enter the product name: ')
			getAmount(sqliteConnection,cursor,productName)
		if key == 3:
			recipeName = input('Please enter the recipe name: ')
			getAmountOfIngredientsOfRecipe(sqliteConnection,cursor,recipeName)

		connectSQL.closeConnection(sqliteConnection)



if __name__ == '__main__':
	main()

