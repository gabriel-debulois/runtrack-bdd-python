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

mycursor.execute("SELECT sum(superficie) AS superficie_total FROM etage")
myresult = mycursor.fetchone()


print("La superficie de La Plateforme est de", myresult[0], "m²")
