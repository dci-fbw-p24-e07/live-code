SELECT * FROM musician
WHERE
  last_name NOT LIKE 'Y%' AND
  last_name NOT LIKE 'M%' AND
  last_name NOT LIKE 'C%' AND
  last_name NOT LIKE 'A%'
ORDER BY last_name, first_name
LIMIT 5 OFFSET 5;
