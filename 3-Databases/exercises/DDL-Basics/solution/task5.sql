ALTER TABLE car_model
    ALTER COLUMN year_of_manufacture TYPE int
    USING year_of_manufacture::integer;
