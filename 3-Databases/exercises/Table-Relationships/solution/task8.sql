DELETE FROM country WHERE name = 'Germany';

SELECT * FROM city;

-- Briefly explain what happened.
-- ******************************************************
-- The foreign key in the `city` table was created with an `ON DELETE SET NULL` clause.
-- When a record in the referenced table (`country`) gets deleted, the records
-- in this table that were referencing to that object are set to
-- NULL.
