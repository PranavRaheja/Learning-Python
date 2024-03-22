import sqlite3
import pandas as pd
import time

try:
    # Connect to the SQLite database
    conn = sqlite3.connect('C:\\Users\\iampr\\Desktop\\history python\\hist_chrome')
    
    # if connected
    print("Connection to SQLite database successful!")
except sqlite3.Error as e:
    
    
    # if not connected
    print("Error connecting to SQLite database:", e)
 
#get table names   
def get_table_names(conn):
    cur = conn.cursor()
    query = """SELECT name FROM sqlite_master WHERE type='table';"""
    cur.execute(query)
    fetch = cur.fetchall()
#make a list of just the string(table name) and get rid of commas and other characters
    tables = [table[0] for table in fetch] 
#print them invidually
    print("All the table names are:\n")
    for i in range(0,18):
        print ("Table ",[i+1],":",tables[i])
    print("\033[34;5mCreating files...\033[0m")
    
#Creating csv files for all the tables
    for table in tables:
        cur.execute(f"""SELECT * FROM {table}""")
        data = cur.fetchall() 
        col_name = [desc[0]for desc in cur.description]
        df = pd.DataFrame(data, columns=col_name)
        df.to_csv(f'C:\\Users\\iampr\\Desktop\\python project\\CSV FILES\\{table}.csv',index=False)
    time.sleep(2)
    print("\033[32;5mCreated :)\033[0m")

get_table_names(conn)






