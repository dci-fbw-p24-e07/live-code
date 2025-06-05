SELECT first_name, last_name, instrument FROM musician
WHERE instrument = 'Piano' OR instrument = 'Guitar'
ORDER BY instrument, last_name;

-- OR:
SELECT first_name, last_name, instrument FROM musician
WHERE instrument IN ('Piano', 'Guitar')
ORDER BY instrument, last_name;
