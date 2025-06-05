
-- Update Bernhard Schwarzenegger's instrument
UPDATE musician SET instrument = 'Piano'
  WHERE first_name = 'Bernhard' and last_name = 'Schwarzenegger';

-- Confirm it worked
SELECT instrument FROM musician
  WHERE first_name = 'Bernhard' and last_name = 'Schwarzenegger';
