import os
import sys
import logging
import pymysql


rds_host  = os.environ['rds_mysql_endpoint']
name = os.environ['rds_mysql_username']
password = os.environ['rds_mysql_password']
db_name = os.environ['db_name_lambda']

logger = logging.getLogger()
logger.setLevel(logging.INFO)

try:
    conn = pymysql.connect(host=rds_host, user=name, passwd=password, db=db_name, connect_timeout=5)
except pymysql.MySQLError as e:
    logger.error("ERROR: Unexpected error: Could not connect to MySQL instance.")
    logger.error(e)
    sys.exit()

logger.info("SUCCESS: Connection to RDS MySQL instance succeeded")
def lambda_handler(event, context):
    """
    This function fetches content from MySQL RDS instance
    """

    item_count = 0

    with conn.cursor() as cur:
    #   cur.execute("drop table IF EXISTS lambda.Employee")
    #   cur.execute("create table Employee (EmpID  int NOT NULL AUTO_INCREMENT, Name varchar(255) NOT NULL, PRIMARY KEY (EmpID))")
         cur.execute('insert into Employee (Name) values("Joe")')
    #    cur.execute('insert into Employee (Name) values("Bob")')
    #    cur.execute('insert into Employee (Name) values("Mary")')
       
         conn.commit()
         cur.execute("select EmpID, Name from lambda.Employee LIMIT 1;")
    for row in cur:
        item_count += 1
        
        
        logger.info(row)
        #print(row)
        conn.commit()
     
    
    return "Added %d items from RDS MySQL table" %(item_count)