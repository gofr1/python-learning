#!/usr/bin/env python3

from bs4 import BeautifulSoup
from sqlalchemy import create_engine
import urllib, configparser, requests
import pandas as pd


URL = 'https://www.xe.com'
CUR = '/symbols.php'

def get_conn_str():
    section_name = 'azure_main'
    config = configparser.ConfigParser()
    _ = config.read("./.env/db.conf")
    db_opts = config.options(section_name)
    details = dict()
    
    for db_opt in db_opts:
        details[db_opt] = config.get(section_name, db_opt)
    
    return 'DRIVER={driver};SERVER={server};PORT={port};DATABASE={database};UID={uid};PWD={pwd}'.format(**details)

def write_in_azure(connect_string, data_frame, table_name):
    params = urllib.parse.quote_plus(connect_string)
    engine = create_engine("mssql+pyodbc:///?odbc_connect=%s" % params)
    data_frame.to_sql(table_name, con=engine, if_exists='replace', index=True)
    # engine.execute("SELECT COUNT(*) FROM currency").fetchall()

def parse_html(input_html, tag):
    result = []
    for block in input_html:
        res = []
        for row in block.find_all(tag):
            txt = row.text
            if not txt:
                for img in row.find_all('img'):
                    txt = get_image('{0}{1}'.format(URL, img.get('src')))
            res.append(txt)
        result.append(res)
    return result
            
def get_image(url):
    myfile = requests.get(url)
    # open('test.gif', 'wb').write(myfile.content) # use to write in file
    return myfile.content

def main():

    response = requests.get("{0}{1}".format(URL, CUR))
    soup = BeautifulSoup(response.text, 'lxml')

    header_html = soup.find_all('tr', class_='currencySymblTableSubTitle')
    part_one = soup.find_all('tr', class_='row1')
    part_two = soup.find_all('tr', class_='row2')

    header = parse_html(header_html, 'td')[0]
    all_cur = part_one + part_two
    
    df = pd.DataFrame(parse_html(all_cur, 'td'), columns = header)
    #print(df) # [109 rows x 8 columns]
    write_in_azure(get_conn_str(), df, 'currency')

if __name__ == '__main__':
    main()