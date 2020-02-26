import psycopg2, configparser

# Pandas and numpy for data wrangling and analysis
import pandas as pd
import numpy as np

# Connect to the dvdrental database on your computer.
# Please use whatever password you created for Postgres.
section_name = 'postgre_local'
config = configparser.ConfigParser()
c = config.read("./.env/db.conf")
db_opts = config.options(section_name)
con_param = dict()

for db_opt in db_opts:
    con_param[db_opt] = config.get(section_name, db_opt)

connect_string = 'dbname={database} user={user} password={password} port={port} host={host}'.format(**con_param)

try:
    conn = psycopg2.connect(connect_string)
except (Exception, psycopg2.Error) as error :
    print ("Error: ", error)
else:
    # Open a cursor to perform database operations
    cur = conn.cursor()
    
    # The "sql = " is the first part that allows us to store the SQL query as a dataframe
    # SELECT is selecting the variables we want to keep from each SQL tables. FROM lists the original table for the join.
    # The first INNER JOIN matches on "film_id" in both the film and inventory tables. This is stored as a temporary table.
    # The second INNER JOIN matches on "inventory_id" in both the temporary table and the rental table.
    # Note: INNER JOIN only keeps observations that match.
    
    sql = """
    SELECT f.title,
           i.inventory_id,
           f.film_id,
           r.rental_id
    FROM film f
    INNER JOIN inventory i ON f.film_id = i.film_id
    INNER JOIN rental r ON i.inventory_id = r.inventory_id
    ORDER BY i.inventory_id;
    """
    
    # This creates a dataframe from the SQL query. We do this so we can work with it in Pandas.
    rentalData = pd.read_sql_query(sql, conn)
    
    # Close the connection and cursor to the Postgres database.
    conn.close()
    cur.close()
    
    # Total number of rows (rentals)
    print(len(rentalData.index))
    
    # To answer the main question of this analyis, we will do a simple count and relative percentage
    # Let's first get a count of how many times each movie was rented. We do this with Panda's crosstab
    titleCount = pd.crosstab(index=rentalData['title'], columns="value")
    titleCount = titleCount.sort_values(by='value', ascending=False)
    
    # Now we will get the relative frequency of how many times each movie was rented as a share of all movie rentals
    rentalFreq = pd.DataFrame((titleCount / titleCount.sum() * 100))
    
    # Sort the results
    rentalFreq = rentalFreq.sort_values(by='value', ascending=False)
    
    rentalFreq.head(3)