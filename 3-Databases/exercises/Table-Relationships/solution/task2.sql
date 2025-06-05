DROP TABLE IF EXISTS city;
CREATE TABLE city (
  id SERIAL PRIMARY KEY,
  name VARCHAR(100),
  area NUMERIC,
  is_capital BOOLEAN,
  country_id INT REFERENCES country ON DELETE SET NULL
);


INSERT INTO city(name, area, is_capital, country_id)
  VALUES('Nur-Sultan', 810.2, true, 5);
INSERT INTO city(name, area, is_capital, country_id)
  VALUES('Montevideo', 201, true, 4);
INSERT INTO city(name, area, is_capital, country_id)
  VALUES('Florida', 8.2, false, 4);
INSERT INTO city(name, area, is_capital, country_id)
  VALUES('Windhoek', 5133, true, 3);
INSERT INTO city(name, area, is_capital, country_id)
  VALUES('Swakopmund', 196.3, false, 3);
INSERT INTO city(name, area, is_capital, country_id)
  VALUES('Marseille', 240.62, false, 2);
INSERT INTO city(name, area, is_capital, country_id)
  VALUES('Berlin', 891.7, true, 1);
