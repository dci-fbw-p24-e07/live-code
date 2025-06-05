DROP DATABASE IF EXISTS map;
CREATE DATABASE map;


\c map;


CREATE TABLE country (
  id SERIAL PRIMARY KEY,
  name VARCHAR(50),
  population INT,
  last_status_change DATE
);


INSERT INTO country(name, population, last_status_change)
  VALUES('Germany', 83190556, '1990-10-03');
INSERT INTO country(name, population, last_status_change)
  VALUES('France', 67413000, '1958-10-04');
INSERT INTO country(name, population, last_status_change)
  VALUES('Namibia', 2550226, '1990-03-21');
INSERT INTO country(name, population, last_status_change)
  VALUES('Uruguay', 3518552, '1830-07-18');
INSERT INTO country(name, population, last_status_change)
  VALUES('Kazakhstan', 18711560, '1995-08-30');


SELECT * FROM country;
