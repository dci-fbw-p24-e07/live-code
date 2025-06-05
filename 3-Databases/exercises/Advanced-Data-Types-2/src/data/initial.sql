CREATE TYPE role_type AS ENUM (
  'Anonymous',
  'Guest',
  'User',
  'Moderator',
  'Admin'
);

CREATE TABLE site_user (
  id serial PRIMARY KEY,
  name varchar(100),
  uuid uuid,
  avatar bytea,
  role role_type DEFAULT 'Anonymous',
  birthdate date,
  siblings varchar[],
  availability time[][],
  site_settings jsonb,
  created_on timestamp,
  active_for interval day
);

INSERT INTO site_user(name, uuid, role, birthdate, siblings, availability, site_settings, created_on)
VALUES (
      	'Miriam Valira',
      	'e41e1291-33b8-4316-8a86-28a618d5c338',
      	'Admin',
      	'1995-08-29',
      	ARRAY['Dani', 'Louis'],
      	ARRAY[[time '12:00:00', time '15:00:00']],
      	'{"background": "red", "notifications": false}',
      	'2015-09-23 08:56:00'
  	),
  	(
      	'Johann Müller',
      	'd81331bf-a4f6-4ecd-8883-51dee509309e',
      	'User',
      	'2002-05-09',
      	null,
      	ARRAY[[time '09:00:00', time '14:00:00'], [time '18:00:00', time '20:00:00']],
      	'{"notifications": true}',
      	'2017-05-01 13:03:00'
  	),
  	(
      	'Louise Clark',
      	'e6168ec9-7306-44a5-9875-2c659e15740e',
      	'Moderator',
      	'1992-05-03',
      	ARRAY['Monique'],
      	ARRAY[[time '09:00:00', time '12:00:00'], [time '13:00:00', time '17:00:00']],
      	'{"notifications": true}',
      	'2007-03-21 10:31:00'
  	);

UPDATE site_user SET active_for = CURRENT_TIMESTAMP - created_on;
