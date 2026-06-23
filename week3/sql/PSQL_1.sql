CREATE TABLE users(
id SERIAL PRIMARY KEY,
name TEXT  NOT NULL,
email TEXT UNIQUE
);
INSERT INTO users(name,email)
VALUES
('sheela','sheela123@gmail.com'),
('ravi','ravi123@gmail,com'),
('mani','mani123@gmail.com'),
('rishi','rishi123@gmail.com'),
('shiva','shiva123@gmail.com');
SELECT * FROM users ORDER BY name DESC;
SELECT * FROM users ORDER BY name ASC;
SELECT * FROM users WHERE id = 4 ;
SELECT * FROM users WHERE name LIKE '%i';
SELECT * FROM users WHERE name LIKE 'r%';
