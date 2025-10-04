-- Table 1: Sales
CREATE TABLE IF NOT EXISTS sales (
    sale_id SERIAL PRIMARY KEY,
    sale_date DATE NOT NULL,
    city VARCHAR(100) NOT NULL,
    product VARCHAR(100),
    amount INT,
    price NUMERIC(10,2)
);

-- Table 2: Weather
CREATE TABLE IF NOT EXISTS weather (
    weather_id SERIAL PRIMARY KEY,
    weather_date DATE NOT NULL,
    city VARCHAR(100) NOT NULL,
    temp_c NUMERIC(5,2),
    humidity INT,
    description VARCHAR(255)
);

INSERT INTO sales (sale_date, city, product, amount, price)
VALUES
('2025-06-27', 'London', 'Umbrella', 5, 12.99),
('2025-06-27', 'London', 'Raincoat', 2, 39.99),
('2025-06-28', 'Paris', 'Sunscreen', 10, 7.50),
('2025-06-28', 'Paris', 'Hat', 3, 15.00);
