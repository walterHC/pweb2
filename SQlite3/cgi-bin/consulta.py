#!/usr/bin/python3.8
# -*- coding: UTF-8 -*-

import sqlite3
import json
import cgi,cgitb

form = cgi.FieldStorage()
nameDB = form.getValue('nameDB')
consulta = form.getValue('consulta')

#nameDB = "Actor";
#consulta = "Tony Simotes"
db = sqlite3.connect("dataBase.db")
con = db.cursor()

if nameDB == "Actor":
    if len(consulta) <= 3:
        con.execute("SELECT Name FROM Actor WHERE Name Like '%"+consulta+"%' ")
        rows = con.fetchall()

    else:
        con.execute("SELECT Name, Title, Year, Score FROM Casting INNER JOIN Actor ON Casting.ActorId = Actor.ActorId INNER JOIN Movie ON Casting.MovieId = Movie.MovieId WHERE Name=?",(consulta,))
        rows = con.fetchall()
else:
    if len(consulta) <= 3:
        con.execute("SELECT Title FROM Movie WHERE Title Like '%"+consulta+"%' ")
        rows = con.fetchall()

    else:
        con.execute("SELECT Name, Title, Year, Score FROM Casting INNER JOIN Actor ON Casting.ActorId = Actor.ActorId INNER JOIN Movie ON Casting.MovieId = Movie.MovieId WHERE Name=?",(consulta,))
        rows = con.fetchall()

data = []
for row in rows:  
    data.append(row)
con.close()

print("Content-Type: application/json\n\n")
print(json.dumps(data)) 
