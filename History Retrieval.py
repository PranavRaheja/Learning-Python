import sqlite3
import pandas as pd
import time
import os
print("\n\033[31;5mCLOSE YOUR BROWSER WHILE YOU RETRIEVE THIS DATA\033[0m")
print("Which browser's history file would you like to choose?")
print("1. Mozilla Firefox")
print("2. Google Chrome")
print("3. Other")
i =1
browser =int(input("Select your browser (1/2/3): "))
print(f"Select the user:")
users = os.listdir("C:\\Users")
for user in users:
    print(f"User",i,":", user)
    i=i+1
    
sel_user = input()
path_chrome = f'C:\\Users\\{sel_user}\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\History'
path_firefox = f'C:\\Users\\{sel_user}\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\dtqlgeuz.default-release\\places.sqlite'

print("\n")
if (browser == 1):
    db_path = path_firefox
elif (browser == 2):
    db_path = path_chrome
elif (browser == 3):
    db_path = input("Please enter the path for the history file: ")

try:
    conn = sqlite3.connect(db_path)
    print("Connection to SQLite database successful!")
except sqlite3.Error as e:
    print("Error connecting to SQLite database:", e)
    exit()  # Exit if cannot connect

#get table names   
def get_table_names(conn):
    cur = conn.cursor()
    query = """SELECT name FROM sqlite_master WHERE type='table';"""
    cur.execute(query)
    fetch = cur.fetchall()
#make a list of just the string(table name) and get rid of characters
    tables = [table[0] for table in fetch] 
#print them invidually
    print("All the table names are:")
    
    for i in range(0,18):
        print ("Table ",[i+1],":",tables[i])
    print("\n\033[34;5mCreating files...\033[0m")
    
    #make directory to store csv files
    base_path ='C:\\Users\\iampr\\Desktop\\'
    dir_path ='CSV Files'
    full_path = os.path.join(base_path,dir_path)
    os.makedirs(full_path,exist_ok=True)

    time.sleep(2)
    print("\033[32;5mCreated :)\033[0m")
    for table in tables:
        cur.execute(f"""SELECT * FROM {table}""")
        data = cur.fetchall() 
        col_name = [desc[0]for desc in cur.description]
        df = pd.DataFrame(data, columns=col_name)
        df.to_csv(f'C:\\Users\\iampr\\Desktop\\CSV FILES\\{table}.csv',index=False)

get_table_names(conn)






