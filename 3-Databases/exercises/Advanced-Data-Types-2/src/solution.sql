-- Task 1

SELECT * FROM site_user WHERE array_length(siblings, 1) > 1

-- Task 2

UPDATE site_user
SET siblings = array_append(siblings, 'Jordi')
WHERE name = 'Louise Clark';

-- Task 3

UPDATE site_user
SET availability = ARRAY[[time '09:00', time '10:00']]
WHERE name = 'Louise Clark';

-- Task 4

UPDATE site_user
SET site_settings = site_settings || jsonb '{"notification": false}'
WHERE name = 'Louise Clark';

-- Task 5

SELECT * FROM site_user WHERE role < 'Moderator';

UPDATE site_user
SET role = 'Moderator'
WHERE name = 'Johan Müller';

-- Task 6

SELECT name, site_settings
FROM site_user
WHERE site_settings->>'notifications' = 'false';

-- Task 7

SELECT name, site_settings
FROM site_user
WHERE not site_settings?'background';
