DELETE FROM musician
  WHERE first_name = 'Justin' AND last_name = 'Bieber';

DELETE FROM musician
  WHERE first_name = 'Lady' AND last_name = 'Gaga';

DELETE FROM musician
  WHERE first_name = 'Alejandro' AND last_name = 'Sanz';

DELETE FROM musician
  WHERE first_name = 'Jimmy' AND last_name = 'Hendrix';

DELETE FROM musician
  WHERE first_name = 'Charlie' AND last_name = 'Parker';

SELECT * FROM musician ORDER BY date_of_bith ASC LIMIT 10;

-- OR:
DELETE FROM musician
  WHERE first_name = 'Justin' AND last_name = 'Bieber'
  OR first_name = 'Lady' AND last_name = 'Gaga'
  OR first_name = 'Alejandro' AND last_name = 'Sanz'
  OR first_name = 'Jimmy' AND last_name = 'Hendrix'
  OR first_name = 'Charlie' AND last_name = 'Parker';

SELECT * FROM musician ORDER BY date_of_bith ASC LIMIT 10;