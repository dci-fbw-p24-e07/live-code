-- Create employees table
CREATE TABLE employees(
   id SERIAL PRIMARY KEY,
   name VARCHAR(15) NOT NULL,
   age INT NOT NULL,
   address CHAR(25),
   salary DECIMAL(18, 2)
);

-- Insert data into employees table
INSERT INTO employees(name, age, address, salary) 
VALUES('Ramesh', 32, 'Ahmedabad', 2000.00),
   ('khilan', 25, 'Delhi', 1500.00),
   ('Kaushik', 23, 'Kota', 2000.00),
   ('chaitali', 25, 'Mumbai', 6500.00),
   ('Hardhik', 27, 'Bhopal', 8500.00),
   ('komal', 22, 'MP', 4500.00),
   ('Muffy', 24, 'Indore', 10000.00 );
