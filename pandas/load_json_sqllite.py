from pandas import read_csv
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String

meta = MetaData()
# print(sqlalchemy.__version__)
engine = create_engine('sqlite:///finance_json.db', echo=True)
sqlite_connection = engine.connect()
df = read_csv("data_file.json")
# save_df = df["bankozktransactions"]
sqlite_table = "pltr"
df.to_sql(sqlite_table, sqlite_connection)
print(df.count())
sqlite_connection.close()
