from pandas import read_csv
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String

meta = MetaData()
#print(sqlalchemy.__version__)

engine = create_engine('sqlite:///finance.db', echo = True)

"""

#defined table structure but returned table already exists error - perhaps we do not need

bankozktransactions = Table(
        'transactions', meta,
        Column('id', Integer, primary_key = True),
        Column('date', String),
        Column('description', String),
        Column('chkref', String),
        Column('amount', String),
        Column('balance', String)
)
meta.create_all(engine)

"""

sqlite_connection = engine.connect()
df = read_csv("export_20201127.csv")
#save_df = df["bankozktransactions"]
sqlite_table= "transactions"

df.to_sql(sqlite_table, sqlite_connection)
print(df.count())

sqlite_connection.close()
