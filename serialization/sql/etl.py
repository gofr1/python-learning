"""ETL from UFO data in XMLinto SQLite database"""
import sqlite3
from typing import Counter
import xml.etree.ElementTree as xml
from datetime import  datetime


def etl(xml_file, db_file):
    num_records = 0
    db = sqlite3.connect(db_file)

    with open('ufo.sql', 'r') as fp:
        schema_sql = fp.read()
    db.executescript(schema_sql)
    db.commit()

    cur = db.cursor()
    insert_sql = 'INSERT INTO ufo (date_occur, latitude, longitude, ufo_shape) VALUES (?, ?, ?, ?);'
    
    tree = xml.parse(xml_file)
    root = tree.getroot()

    for sighting in root.findall('./sighting'): 
        date_occur = sighting.find('time').text
        latitude = float(sighting.find('lat').text)
        longitude = float(sighting.find('lng').text)
        ufo_shape = sighting.find('shape').text
        
        if date_occur != None:
            date_occur = datetime.strptime(date_occur, '%m/%d/%Y').date()

        cur.execute(insert_sql, (date_occur, latitude, longitude, ufo_shape))
        num_records += 1
    db.commit()

    return num_records


if __name__ == '__main__':
    count = etl('ufo.xml', 'ufo.db')
    print(f'{count} records loaded') # 50856 based on ufo.csv

    db = sqlite3.connect('ufo.db')
    db.row_factory = sqlite3.Row # access column by name

    cur = db.cursor()
    query_sql = 'SELECT date_occur, latitude, longitude, ufo_shape FROM ufo LIMIT 10;'
    for row in cur.execute(query_sql):
        print(dict(row))

#* 50856 records loaded
#* {'date_occur': '2008-11-22', 'latitude': -95.78950112, 'longitude': 36.05084018, 'ufo_shape': 'Changing'}
#* {'date_occur': '2006-04-08', 'latitude': -118.2453206, 'longitude': 34.05349094, 'ufo_shape': 'Changing'}
#* {'date_occur': '2007-05-26', 'latitude': -106.6486413, 'longitude': 35.08418003, 'ufo_shape': 'Circle'}
#* {'date_occur': '2001-06-15', 'latitude': -71.53660023, 'longitude': 43.20725072, 'ufo_shape': 'Circle'}
#* {'date_occur': '2005-11-10', 'latitude': -76.51119034, 'longitude': 43.45646037, 'ufo_shape': 'Circle'}
#* {'date_occur': '2013-09-12', 'latitude': -118.4292502, 'longitude': 34.2608902, 'ufo_shape': 'Circle'}
#* {'date_occur': '2007-11-22', 'latitude': -82.30084031, 'longitude': 39.80629006, 'ufo_shape': 'Cylinder'}
#* {'date_occur': '2007-12-07', 'latitude': -70.15095032, 'longitude': 44.67026882, 'ufo_shape': 'Diamond'}
#* {'date_occur': '2012-09-08', 'latitude': -86.28880059, 'longitude': 36.20776105, 'ufo_shape': 'Flash'}
#* {'date_occur': '2012-08-27', 'latitude': -95.20141137, 'longitude': 42.64746138, 'ufo_shape': 'Formation'

# ufo.csv first 10 rows
# LATITUDE,LONGITUDE,CITY,DATE_OCCUR,STATE,UFO_SHAPE,DURATION
# -95.78950112,36.05084018,Broken Arrow,11/22/2008,OK,Changing,0
# -118.2453206,34.05349094,Los Angeles,04/08/2006,CA,Changing,0
# -106.6486413,35.08418003,Albuquerque,05/26/2007,NM,Circle,0
# -71.53660023,43.20725072,Concord,06/15/2001,NH,Circle,0
# -76.51119034,43.45646037,Oswego,11/10/2005,NY,Circle,0
# -118.4292502,34.2608902,Pacoima,09/12/2013,CA,Circle,0
# -82.30084031,39.80629006,Sommerset,11/22/2007,OH,Cylinder,0
# -70.15095032,44.67026882,Farmington,12/07/2007,ME,Diamond,0
# -86.28880059,36.20776105,Lebanon,09/08/2012,TN,Flash,0
# -95.20141137,42.64746138,Storm Lake,08/27/2012,IA,Formation,0
