from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String

meta = MetaData()


#print(sqlalchemy.__version__)

engine = create_engine('sqlite:///finance.db', echo = True)
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
