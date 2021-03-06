DROP TABLE transactions;
DROP TABLE limits;
DROP TABLE tags;
DROP TABLE merchants;


CREATE TABLE limits (
    id SERIAL PRIMARY KEY,
    spending_limit INT,
    notification_point INT
);

CREATE TABLE tags (
    id SERIAL PRIMARY KEY,
    spending_type VARCHAR(255),
    active BOOLEAN
);

CREATE TABLE merchants (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    active BOOLEAN
);

CREATE TABLE transactions (
    id SERIAL PRIMARY KEY,
    amount INT,
    tag_id INT REFERENCES tags(id) ON DELETE CASCADE,
    merchant_id INT REFERENCES merchants(id) ON DELETE CASCADE,
    date DATE
);
