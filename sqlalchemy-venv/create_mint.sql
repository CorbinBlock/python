CREATE PROCEDURE createMint()
LANGUAGE SQL
AS $$
CREATE TABLE mint(
recordid serial,
loaddate date default current_date,
date date,
description varchar(200),
originaldescription varchar(200),
amount money,
transactiontype varchar(50),
category varchar(50),
accountname varchar(50),
labels varchar(50),
notes varchar(50)
);

$$;