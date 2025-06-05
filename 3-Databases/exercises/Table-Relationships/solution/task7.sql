SELECT city.name, country.name, country.population
  FROM city, country
  WHERE city.country_id = country.id
  AND city.is_capital = true
  ORDER BY country.population DESC
  LIMIT 3;
