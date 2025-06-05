CREATE TABLE language (
  code char(2) PRIMARY KEY,
  name varchar(25)
);

\i language.sql

SELECT name, code FROM language;

\i language_test.sql
