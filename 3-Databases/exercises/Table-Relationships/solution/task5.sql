SELECT country.name, city.name, city.area
  FROM country, city
  WHERE country.id = city.country_id
  ORDER BY city.area
  LIMIT 1;
