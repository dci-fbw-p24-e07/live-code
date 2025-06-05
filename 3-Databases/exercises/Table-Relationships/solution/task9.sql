ALTER TABLE country
ADD code char(2) UNIQUE;

\i country.sql

SELECT name, code FROM country;

\i country_test.sql
