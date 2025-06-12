-- Drop schema if it exists
DROP SCHEMA IF EXISTS bank CASCADE;
CREATE SCHEMA bank;
SET search_path TO bank;

-- Customers table
CREATE TABLE customers (
    customer_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    email VARCHAR(100) UNIQUE,
    phone VARCHAR(20),
    address TEXT,
    date_of_birth DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Branches table
CREATE TABLE branches (
    branch_id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    address TEXT,
    city VARCHAR(50),
    state VARCHAR(50),
    zip_code VARCHAR(10),
    phone VARCHAR(20)
);

-- Employees table
CREATE TABLE employees (
    employee_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    email VARCHAR(100) UNIQUE,
    phone VARCHAR(20),
    position VARCHAR(50),
    branch_id INT REFERENCES branches(branch_id),
    hired_date DATE
);

-- Accounts table
CREATE TABLE accounts (
    account_id SERIAL PRIMARY KEY,
    customer_id INT REFERENCES customers(customer_id),
    branch_id INT REFERENCES branches(branch_id),
    account_type VARCHAR(20) CHECK (account_type IN ('Checking', 'Savings')),
    balance NUMERIC(15,2) DEFAULT 0.00,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Transactions table
CREATE TABLE transactions (
    transaction_id SERIAL PRIMARY KEY,
    account_id INT REFERENCES accounts(account_id),
    transaction_type VARCHAR(20) CHECK (transaction_type IN ('Deposit', 'Withdrawal', 'Transfer')),
    amount NUMERIC(15,2) CHECK (amount > 0),
    transaction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    description TEXT
);

-- Loans table
CREATE TABLE loans (
    loan_id SERIAL PRIMARY KEY,
    customer_id INT REFERENCES customers(customer_id),
    branch_id INT REFERENCES branches(branch_id),
    loan_type VARCHAR(50),
    amount NUMERIC(15,2),
    interest_rate NUMERIC(5,2),
    issued_date DATE,
    due_date DATE,
    status VARCHAR(20) CHECK (status IN ('Active', 'Closed', 'Defaulted'))
);

-- -----------------------
-- Mock Data
-- -----------------------

-- Branches
INSERT INTO branches (name, address, city, state, zip_code, phone) VALUES
('Downtown Branch', '123 Main St', 'Metropolis', 'NY', '10001', '212-555-0101'),
('Uptown Branch', '456 Broadway Ave', 'Metropolis', 'NY', '10002', '212-555-0102');

-- Customers
INSERT INTO customers (first_name, last_name, email, phone, address, date_of_birth) VALUES
('Alice', 'Johnson', 'alice@example.com', '555-1234', '10 Elm St', '1985-04-12'),
('Bob', 'Smith', 'bob@example.com', '555-5678', '22 Oak St', '1990-08-19'),
('Carol', 'Taylor', 'carol@example.com', '555-8765', '35 Maple Rd', '1978-11-03');

-- Employees
INSERT INTO employees (first_name, last_name, email, phone, position, branch_id, hired_date) VALUES
('David', 'Brown', 'david@bank.com', '555-1111', 'Manager', 1, '2015-06-01'),
('Emily', 'White', 'emily@bank.com', '555-2222', 'Teller', 2, '2018-09-15');

-- Accounts
INSERT INTO accounts (customer_id, branch_id, account_type, balance) VALUES
(1, 1, 'Checking', 2500.00),
(1, 1, 'Savings', 10000.00),
(2, 2, 'Checking', 3200.50),
(3, 1, 'Savings', 500.00);

-- Transactions
INSERT INTO transactions (account_id, transaction_type, amount, description) VALUES
(1, 'Deposit', 500.00, 'Initial deposit'),
(1, 'Withdrawal', 200.00, 'ATM withdrawal'),
(2, 'Deposit', 1000.00, 'Monthly saving'),
(3, 'Deposit', 300.00, 'Paycheck'),
(4, 'Deposit', 500.00, 'Opening balance');

-- Loans
INSERT INTO loans (customer_id, branch_id, loan_type, amount, interest_rate, issued_date, due_date, status) VALUES
(1, 1, 'Home Loan', 250000.00, 3.5, '2021-01-10', '2031-01-10', 'Active'),
(2, 2, 'Car Loan', 15000.00, 5.0, '2022-05-15', '2027-05-15', 'Active'),
(3, 1, 'Personal Loan', 5000.00, 7.5, '2020-09-01', '2023-09-01', 'Closed');