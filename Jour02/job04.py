import mysql.connector

# Connexion à la base de données
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="21601218",
  database="laplateforme"
)

if mydb.is_connected():
  print("Connection established")


mycursor = mydb.cursor()

mycursor.execute("SELECT nom, capacite FROM salles")
myresult = mycursor.fetchall()

for x in myresult:
  print(x)