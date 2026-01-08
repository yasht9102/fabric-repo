-- Lakehouse Table: sales
-- Storage: Delta
-- Layer: Silver
-- Owner: Data Engineering

CREATE TABLE sales (
    sale_id INT,
    amount DECIMAL(10,2),
    sale_date DATE
);
