import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="PostGres123!",
    database="mydatabase"
)

mycursor = mydb.cursor()

sql = "DELETE FROM players WHERE completions = 'Tom Brady*'"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "records deleted.")