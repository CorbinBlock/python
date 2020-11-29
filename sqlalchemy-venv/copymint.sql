CREATE PROCEDURE copyMint()
LANGUAGE SQL
AS $$
COPY mint(date, description, originaldescription, amount, transactiontype, category, accountname, labels ,notes) FROM '/home/ec2-user/sql/transactions.csv' DELIMITER ',' CSV HEADER;
$$;