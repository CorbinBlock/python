from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String

meta = MetaData()

# print(sqlalchemy.__version__)

engine = create_engine('sqlite:///finance.db', echo=True)

hcac_etl = Table(
    'hcac_etl', meta,
    Column('data', String),
    Column('data_two', String),
    Column('data_three', String)
)
meta.create_all(engine)
