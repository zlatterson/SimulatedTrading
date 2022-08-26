DROP TABLE call_put_options;
DROP TABLE call_put_contracts;
DROP TABLE buy_sell_actions;
DROP TABLE stocks;
DROP TABLE users;

CREATE TABLE users(
    id SERIAL PRIMARY KEY,
    username VARCHAR(255),
    name VARCHAR(255),
    currency VARCHAR(255),
    money_paid_in FLOAT,
    money FLOAT
);

CREATE TABLE stocks(
    id SERIAL PRIMARY KEY,
    ticker VARCHAR(255),
    summary VARCHAR(255),
    currency VARCHAR(255)
);

CREATE TABLE buy_sell_actions (
    id SERIAL PRIMARY KEY,
    user_id SERIAL REFERENCES users(id) ON DELETE CASCADE,
    stock_id SERIAL REFERENCES stocks(id) ON DELETE CASCADE,
    buy_sell_type VARCHAR(255),
    quantity INT,
    average_price FLOAT,
    history VARCHAR(255)
);

CREATE TABLE call_put_contracts (
    id SERIAL PRIMARY KEY,
    stock_id SERIAL REFERENCES stocks(id) ON DELETE CASCADE,
    contract_name VARCHAR(255),
    call_put_type VARCHAR(255),
    k FLOAT,
    expires VARCHAR(255)
);

CREATE TABLE call_put_options (
    id SERIAL PRIMARY KEY,
    user_id SERIAL REFERENCES users(id) ON DELETE CASCADE,
    call_put_contract_id SERIAL REFERENCES call_put_contracts(id) ON DELETE CASCADE,
    n_contracts INT,
    bought_c_price FLOAT,
    bought_contracts_value FLOAT,
    timestamp VARCHAR(255)
);
