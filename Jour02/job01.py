import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="21601218",
    database="laplateforme"
)

if mydb.is_connected():
  print("Connection established")


mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM etudiants")

myresult = mycursor.fetchall()

for x in myresult:
    print(x)
