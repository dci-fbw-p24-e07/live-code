SELECT
  first_name AS "Name",
  last_name AS "Family name",
  date_of_birth AS "Date of birth"
FROM musician
WHERE
  instrument = 'Harp' AND
  last_name LIKE 'M%'
ORDER BY date_of_birth DESC
LIMIT 1 OFFSET 3;
