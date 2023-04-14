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
mycursor.execute("CREATE TABLE etage(id INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY, "
                 "nom VARCHAR(255) NOT NULL, "
                 "numero INT NOT NULL, "
                 "superficie INT NOT NULL);")
mycursor.execute("CREATE TABLE salles(id INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY, "
                 "nom VARCHAR(255) NOT NULL, "
                 "id_etage INT NOT NULL,"
                 "capacite INT NOT NULL);")
