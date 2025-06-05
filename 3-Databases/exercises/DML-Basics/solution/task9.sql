SELECT * FROM musician
  WHERE first_name = 'Araceli' and (
    instrument = 'Piano' or instrument = 'Guitar'
  )
  ORDER BY date_of_birth DESC
  LIMIT 3;
