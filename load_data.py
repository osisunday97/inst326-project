#NOTES: removed index numbers and possibly will remove hispanic column

import csv
import sqlite3

connect = sqlite3.connect('guns.sqlite')   #create database file
cursor = connect.cursor()                  #connect to database
#print(cursor)                             #make sure it works


#create table gun_deaths
gun_deaths = """
        CREATE TABLE IF NOT EXISTS gun_deaths (
            year        INTEGER,
            month       INTEGER,
            intent      TEXT,
            police      TINYINT,
            sex         TEXT,
            age         INTEGER,
            race        TEXT,
            hispanic    INTEGER,
            place       TEXT,
            education   INTEGER
        )
    """
cursor.execute(gun_deaths)

for row in csv.reader(open('guns.csv')):

    insert_gun_death =  'INSERT INTO gun_deaths VALUES (?,?,?,?,?,?,?,?,?,?)'
    cursor.execute(insert_gun_death, row)

connect.commit()

