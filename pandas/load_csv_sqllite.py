from pandas import read_csv
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String

meta = MetaData()
# print(sqlalchemy.__version__)
engine = create_engine('sqlite:///finance.db', echo=True)
sqlite_connection = engine.connect()
df = read_csv("hcac.csv")
# save_df = df["bankozktransactions"]
sqlite_table = "hcac"
df.to_sql(sqlite_table, sqlite_connection)
print(df.count())
sqlite_connection.close()
