CREATE DATABASE vehicles;

\c vehicles;

CREATE TABLE car_model (
  name varchar(100),
  make varchar(100),
  year_of_checkin varchar(4),
  stock int
);
