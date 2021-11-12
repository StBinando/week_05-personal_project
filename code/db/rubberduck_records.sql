DROP TABLE IF EXISTS customers_items;
DROP TABLE IF EXISTS customers;
DROP TABLE IF EXISTS items;
DROP TABLE IF EXISTS albums;
DROP TABLE IF EXISTS artists;

CREATE TABLE artists (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255) NOT NULL
);

CREATE TABLE albums (
  id SERIAL PRIMARY KEY,
  artist_id INT REFERENCES artists(id),
  title VARCHAR(255) NOT NULL
);

CREATE TABLE items (
  id SERIAL PRIMARY KEY,
  album_id INT REFERENCES albums(id),
  support VARCHAR(255) NOT NULL,
  cost FLOAT NOT NULL,
  selling_price FLOAT NOT NULL,
  in_stock INT,
  ordered INT
);

CREATE TABLE customers (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  contact VARCHAR(255) NOT NULL
);

CREATE TABLE customers_items (
  id SERIAL PRIMARY KEY,
  customer_id INT REFERENCES customers(id),
  item_id INT REFERENCES items(id)
);
