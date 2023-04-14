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

mycursor.execute("SELECT sum(capacite) AS superficie_total FROM salles")
myresult = mycursor.fetchone()


print("La capacité de toutes les salles est de", myresult[0])
