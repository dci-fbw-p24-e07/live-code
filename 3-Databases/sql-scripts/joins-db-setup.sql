-- Check if database exists and create it
CREATE DATABASE food;

-- Change path to food DB 
\c food;

-- Create the schema
CREATE SCHEMA food_tables;

-- Set our search path
SET search_path TO food_tables;

-- Create a table if it does not exist
CREATE TABLE IF NOT EXISTS menu_a (
    a_id SERIAL PRIMARY KEY,
    food_a VARCHAR (100) NOT NULL
);

-- Create a table if it does not exist
CREATE TABLE IF NOT EXISTS menu_b (
    b_id SERIAL PRIMARY KEY,
    food_b VARCHAR (100) NOT NULL
);

INSERT INTO menu_a (food_a) 
VALUES ('Apple'),
        ('Mangoes'),
        ('Grapes'),
        ('Oranges');

INSERT INTO menu_b (food_b)
VALUES ('Watermelon'),
        ('Apple'),
        ('Oranges'),
        ('Pear');