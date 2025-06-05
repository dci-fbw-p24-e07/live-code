-- Add 5 musicians
--
-- If we want to insert values in all fields of the table,
-- and in the VALUES() we use the same order as they are defined,
-- we don't need to indicate the fields after the table name.

INSERT INTO musician
  VALUES('Justin', 'Bieber', '1994-03-01', 'Voice');

INSERT INTO musician
  VALUES('Lady', 'Gaga', '1986-03-28', 'Voice');

INSERT INTO musician
  VALUES('Alejandro', 'Sanz', '1968-12-18', 'Voice');

INSERT INTO musician
  VALUES('Jimmy', 'Hendrix', '1942-11-27', 'Guitar');

INSERT INTO musician
  VALUES('Charlie', 'Parker', '1920-08-29', 'Saxophone');


-- Show all columns for all musicians in the table
SELECT * FROM musician;
