DROP TABLE call_put_options;
DROP TABLE buy_sell_positions;
DROP TABLE stocks;
DROP TABLE users;

CREATE TYPE currency AS ENUM ('USD', 'GBP', 'CAD');
CREATE TYPE action AS ENUM ('buy', 'sell');
CREATE TYPE call_put_type AS ENUM ('call', 'put');


CREATE TABLE users(
    id SERIAL PRIMARY KEY,
    username VARCHAR(255),
    name VARCHAR(255),
    money INT
);

CREATE TABLE stocks(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    ticker VARCHAR(255),
    currency_used currency,
);

CREATE TABLE buy_sell_positions (
    id SERIAL PRIMARY KEY,
    user_id SERIAL REFERENCES users(id) ON DELETE CASCADE,
    stock_id SERIAL REFERENCES items(id) ON DELETE CASCADE,
    action_used action,
    price FLOAT,
    timestamp DATETIME
);

CREATE TABLE call_put_options (
    id SERIAL PRIMARY KEY,
    user_id SERIAL REFERENCES users(id) ON DELETE CASCADE,
    stock_id SERIAL REFERENCES items(id) ON DELETE CASCADE,
    action_used action,
    call_put_type call_put_type,
    price FLOAT,
    timestamp DATETIME,
    c FLOAT,
    n FLOAT,
    st FLOAT,
    k FLOAT,
    r FLOAT,
    t FLOAT,
    o FLOAT
);