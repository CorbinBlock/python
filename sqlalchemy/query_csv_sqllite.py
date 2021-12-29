from sqlalchemy import create_engine

engine = create_engine('sqlite:///finance.db', echo=True)

query = """

--INSERT INTO hcac_etl
--SELECT * FROM hcac


SELECT SUBSTR(data_three,3,85) FROM hcac_etl

SELECT SUBSTR(data_three,92,95) FROM hcac_etl LIMIT 1


--SELECT SUBSTR(data_three,3,800) FROM hcac_etl LIMIT 1    
 




"""

query_two = """

--SELECT "df_data" FROM hcac

--DROP TABLE hcac_etl

PRAGMA table_info(hcac);

--ALTER TABLE hcac
--RENAME COLUMN 'Unnamed: 0' TO df_data

"""

with engine.connect() as con:
    rs = con.execute(query_two)

    for row in rs:
        print(row)
