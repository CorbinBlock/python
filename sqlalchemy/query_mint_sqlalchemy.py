from sqlalchemy import create_engine

db = create_engine('postgresql+psycopg2:///', echo = True)

query = """


SELECT * FROM mint ORDER BY date DESC

"""

# Execute query
result_set = db.execute("SELECT * FROM mint ORDER BY date DESC")

for r in result_set:  
    print(r)
