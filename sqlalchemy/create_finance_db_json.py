from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String

meta = MetaData()

# print(sqlalchemy.__version__)

engine = create_engine('sqlite:///finance_json.db', echo=True)

hcac_etl = Table(
    'pltr', meta,
    Column('data', String)
)
meta.create_all(engine)
