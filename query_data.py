import sqlite3

connect = sqlite3.connect('guns.sqlite')
cursor = connect.cursor()

''' The data includes data regarding the victim's age, sex, race, education, intent, 
    time (month and year) and place of death, and weather or not police was at the place of death
'''


#QUERY 1: Count the number of deaths that the police was involved in and deaths they were not involved in.

gun_deaths = '''    SELECT police AS 'involved police', COUNT(police)
                    FROM gun_deaths
                    GROUP BY police; '''
cursor.execute(gun_deaths)
print('query 1:')
for t in cursor.fetchall():
    print(t)


#QUERY 2: Count the number of deaths in each category of the intent column, order by intent ASC
gun_deaths = '''    SELECT intent, COUNT(*)
                    FROM gun_deaths
                    GROUP BY intent
                    ORDER BY intent ASC; '''
cursor.execute(gun_deaths)
print('query 2:')
for t in cursor.fetchall():
    print(t)


#QUERY 3: Find out the month where most suicides and homocides took place, respectively
gun_deaths = '''    SELECT month, COUNT(intent) AS 'num of suicides'
                    FROM gun_deaths
                    WHERE intent = 'Suicide'
                    GROUP BY month
                    ORDER BY COUNT(intent) ASC; '''
cursor.execute(gun_deaths)
print('query 3:')
for t in cursor.fetchall():
    print(t)

gun_deaths =  '''   SELECT month, COUNT(intent) AS 'num of homicides'
                    FROM gun_deaths
                    WHERE intent = 'Homicide' 
                    GROUP BY month
                    ORDER BY COUNT(intent) ASC; '''
cursor.execute(gun_deaths)
print('query 3:')
for t in cursor.fetchall():
    print(t)


#QUERY 4: For homocides, count the number of people murdered in each education level
# 1: Less than High School 
# 2: Graduated from High School or equivalent 
# 3: Some College 
# 4: At least graduated from College 
# 5: Not available
gun_deaths = '''    SELECT education, COUNT(education) AS edu_count
                    FROM gun_deaths
                    WHERE intent = 'Homicide'
                    GROUP BY education; '''
cursor.execute(gun_deaths)
print('query 4:')
for t in cursor.fetchall():
    print(t)







