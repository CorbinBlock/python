from sqlalchemy import create_engine

engine = create_engine('sqlite:///finance.db', echo = True)


query="""

SELECT * FROM transactions

"""
with engine.connect() as con:

    rs = con.execute(query)

    for row in rs:
        print(row)
