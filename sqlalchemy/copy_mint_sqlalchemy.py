from sqlalchemy import create_engine

db = create_engine('postgresql+psycopg2:///', echo = True)

query = """

CREATE PROCEDURE copyMint()
LANGUAGE SQL
AS $$
COPY mint(date, description, originaldescription, amount, transactiontype, category, accountname, labels ,notes) FROM 'transactions.csv' DELIMITER ',' CSV HEADER;
$$;

"""

# Execute query
result_set = db.execute(query)

#for r in result_set:  
#    print(r)
