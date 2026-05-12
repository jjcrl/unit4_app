CREATE TABLE IF NOT EXISTS films (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    release_year VARCHAR(255)
);

TRUNCATE table films;

INSERT INTO films (title, release_year) VALUES ('Akira', '1988');
INSERT INTO films (title, release_year) VALUES ('The Beach', '2000');