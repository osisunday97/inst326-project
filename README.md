# Project Idea

I want to do my project using SQLite to analysis a csv file that contains information about victims of gun deaths in the US from 2012 to 2014. I would be able to import the csv file in python and query the database to form conclusions from the data.

The database includes data regarding the gun death victim. 
This database includes the age, sex, race, education, intent, month, year 
and place of death, and weather or not police was at the place of death.

# Details 
 ** load_data.py: I created a database file name gun_deaths and connected to it using a cursor. I then created a table that reflects the columns in the csv file. Then, I inserted the data from the csv file into the table.

 ** query_data.py: I queried the populate database to anakyze and form conclusion based on the data. I wrote and excecuted four different kinds a queries.
    * Query 1:  From the 100,799 gun deaths, police were involved in 1,402 of them. 
                However, they were not invloved in the remaining 99,396 gun deaths.
    * Query 2:  The highest intent/cause of death was suidice with ~63,000 deaths. 
                The second highest was homicide with ~35,000 deaths.
    * Query 3:  Most suicides took place between the months of April and August.
                While most homicides took place in June, July, August and Decemember.
    * Query 4:  For suicide victims, those who had a college education committed suicide more than those with less                than a HS education. 
                However, for homicide victims, about 11,000 people with less than a HS education were killed compared to about 1,500 victims with college education.

# For Use
** This database was intended to display my findings from the csv I uploaded. However, if you choose to query the database yourselve, please follow the directions and methods I used in the 'load_data.py' and 'query_data.py' files.

