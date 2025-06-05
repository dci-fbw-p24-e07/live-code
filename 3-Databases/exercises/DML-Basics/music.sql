DROP DATABASE IF EXISTS music;


CREATE DATABASE music;

\c music


CREATE TABLE musician (
    first_name VARCHAR(40),
    last_name VARCHAR(40),
    date_of_birth TIMESTAMP,
    instrument varchar(100)
);
