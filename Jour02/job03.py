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

sql = "INSERT INTO etage (nom, numero, superficie) VALUES (%s, %s, %s)"
val = [
    ('RDC', 0, 500),
    ('R+1', 1, 500)
]
mycursor.executemany(sql, val)
mydb.commit()
print(mycursor.rowcount, "was inserted.")

sql = "INSERT INTO salles (nom, id_etage, capacite) VALUES (%s, %s, %s)"
val = [
    ('Lounge', 1, 100),
    ('Studio Son', 1 ,5),
    ('Broadcasting', 2, 50),
    ('Bocal Peda', 2 ,4),
    ('Coworking', 2, 80),
    ('Studio Video', 2, 5)
]

mycursor.executemany(sql, val)
mydb.commit()
print(mycursor.rowcount, "was inserted.")