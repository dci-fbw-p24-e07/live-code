-- Connect to e07_store database
\c e07_store;

DROP TABLE IF EXISTS company;
DROP TABLE IF EXISTS company_bkp;

-- Create company table
CREATE TABLE company(
   id SERIAL PRIMARY KEY,
   name           TEXT    NOT NULL,
   age            INT     NOT NULL,
   address        CHAR(50),
   salary         REAL
);

-- Create company_bkp table
CREATE TABLE company_bkp(
   id SERIAL PRIMARY KEY,
   name           TEXT    NOT NULL,
   age            INT     NOT NULL,
   address        CHAR(50),
   salary         REAL
);

-- Insert company records
INSERT INTO company (id, name, age, address, salary)
VALUES (1, 'Paul', 32, 'California', 20000.00),
	(2, 'Allen', 25, 'Texas', 15000.00),
(3, 'Teddy', 23, 'Norway', 20000.00),
(4, 'Mark', 25, 'Rich-Mond ', 65000.00),
(5, 'David', 27, 'Texas', 85000.00),
(6, 'Kim', 22, 'South-Hall', 45000.00),
(7, 'James', 24, 'Houston', 10000.00);