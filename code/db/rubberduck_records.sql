DROP TABLE IF EXISTS pre_orders;
DROP TABLE IF EXISTS customers;
DROP TABLE IF EXISTS items;
DROP TABLE IF EXISTS albums;
DROP TABLE IF EXISTS artists;

CREATE TABLE artists (
  id SERIAL PRIMARY KEY,
  name VARCHAR NOT NULL
);

CREATE TABLE albums (
  id SERIAL PRIMARY KEY,
  artist_id INT REFERENCES artists(id),
  title VARCHAR NOT NULL,
);

CREATE TABLE items (
  id SERIAL PRIMARY KEY,
  album_id INT REFERENCES album(id),
  support VARCHAR NOT NULL,
  cost FLOAT NOT NULL,
  selling_price FLOAT NOT NULL,
  in_stock INT,
  ordered INT,
  pre_booked INT
);

CREATE TABLE customers (
  id SERIAL PRIMARY KEY,
  name VARCHAR NOT NULL,
  contact VARCHAR NOT NULL
);

CREATE TABLE pre_orders (
  id SERIAL PRIMARY KEY,
  customer_id INT REFERENCES customer(id),
  item_id INT REFERENCES item(id)
);
