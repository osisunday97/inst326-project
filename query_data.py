import sqlite3

connect = sqlite3.connect('guns.sqlite')
cursor = connect.cursor()

''' The database includes data regarding the gun death victim. 
This database includes the age, sex, race, education, intent, month, year 
and place of death, and weather or not police was at the place of death.
'''


#QUERY 1: Count the number of deaths that the police was involved in and deaths they were not involved in.

gun_deaths = '''    SELECT police AS 'involved police', COUNT(police)
                    FROM gun_deaths
                    GROUP BY police; '''
cursor.execute(gun_deaths)
print('query 1: 0 = no police involved, 1 = police involvement')
for t in cursor.fetchall():
    print(t)


#QUERY 2: Count the number of deaths in each category of the intent column, order by intent ASC
gun_deaths = '''    SELECT intent, COUNT(*)
                    FROM gun_deaths
                    GROUP BY intent
                    ORDER BY intent ASC; '''
cursor.execute(gun_deaths)
print('query 2: cause of gun death')
for t in cursor.fetchall():
    print(t)


#QUERY 3: Find out the month where most suicides and homocides took place, respectively
gun_deaths = '''    SELECT month, COUNT(intent) AS 'num of suicides'
                    FROM gun_deaths
                    WHERE intent = 'Suicide'
                    GROUP BY month
                    ORDER BY COUNT(intent) ASC; '''
cursor.execute(gun_deaths)
print('query 3: months and num of suicides')
for t in cursor.fetchall():
    print(t)

gun_deaths =  '''   SELECT month, COUNT(intent) AS 'num of homicides'
                    FROM gun_deaths
                    WHERE intent = 'Homicide' 
                    GROUP BY month
                    ORDER BY COUNT(intent) ASC; '''
cursor.execute(gun_deaths)
print('query 3: months and num of homicides')
for t in cursor.fetchall():
    print(t)


#QUERY 4: Count the number of victims of suicide who had less than a HS educaton and  those who graudated from
#college, respectively. And similary, count the number victims of homicides 
# 1: Less than High School 
# 2: Graduated from High School or equivalent 
# 3: Some College 
# 4: At least graduated from College 
# 5: Not available

gun_deaths = '''    SELECT intent, COUNT(intent) AS num_victims
                    FROM gun_deaths
                    WHERE education = 1 AND intent = 'Suicide'; '''
cursor.execute(gun_deaths)
print('query 4: less than HS & suicide')
for t in cursor.fetchall():
    print(t)

gun_deaths = '''    SELECT intent, COUNT(intent) AS num_victims
                    FROM gun_deaths
                    WHERE education = 4 AND intent = 'Suicide'; '''
cursor.execute(gun_deaths)
print('query 4: college & suicide')
for t in cursor.fetchall():
    print(t)

gun_deaths = '''    SELECT intent, COUNT(intent) AS num_victims
                    FROM gun_deaths
                    WHERE education = 1 AND intent = 'Homicide'; '''
cursor.execute(gun_deaths)
print('query 4: less than HS & homicide')
for t in cursor.fetchall():
    print(t)

gun_deaths = '''    
                    SELECT intent, COUNT(intent) AS num_victims
                    FROM gun_deaths
                    WHERE education = 4 AND intent = 'Homicide'; '''
cursor.execute(gun_deaths)
print('query 4: college & homicide')
for t in cursor.fetchall():
    print(t)




