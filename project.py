import sqlite3 
database = 'basketball.sqlite' 
conn = sqlite3.connect(database) 
import pandas as pd 
tables = pd.read_sql("""SELECT * 
                        FROM sqlite_master 
                        WHERE type='table';""", conn)
tables.info()