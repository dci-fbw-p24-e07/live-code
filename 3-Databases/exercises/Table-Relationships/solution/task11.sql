CREATE TABLE locale (
  name varchar(100),
  language_code char(2) REFERENCES language,
  country_code char(2) REFERENCES country(code),
  PRIMARY KEY(language_code, country_code)
);

\i locale.sql

SELECT * FROM locale;

\i locale_test.sql
