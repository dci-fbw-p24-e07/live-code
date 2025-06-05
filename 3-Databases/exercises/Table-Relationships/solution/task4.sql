SELECT * FROM city, country
  WHERE city.country_id = country.id
  AND country.name = 'Germany';
