DROP TABLE IF EXISTS posts;
DROP TABLE IF EXISTS users;
CREATE TABLE users(
id SERIAL PRIMARY KEY,
name TEXT
);
CREATE TABLE posts(
id SERIAL PRIMARY KEY,
user_id INTEGER REFERENCES users(id),
posts TEXT
);
INSERT INTO users(name)
VALUES
('alice'),
('bob'),
('charlie'),
('david');
SELECT * FROM users;
INSERT INTO posts(user_id,posts)
VALUES
(1,'blog about mountain'),
(2,'blog about mountain'),
(3,'blog about mountain'),
(2,'vlog on travel'),
(3,'vlog on travel'),
(1,'upload a photo'),
(4,'blog about trecking');

#UPDATE
UPDATE posts
SET posts = 'blog about raining'
WHERE user_id =4;

#INNER-JOIN
SELECT * FROM posts;
SELECT users.name,posts.posts
FROM users
INNER JOIN posts
on users.id = posts.user_id;

#DELETE
DELETE FROM posts
WHERE user_id = 4;
SELECT * FROM posts;

#LEFT-JOIN
SELECT users.name,posts.posts
FROM users
LEFT JOIN posts
on users.id = posts.user_id

#COUNT POSTS PER USER
SELECT users.name,COUNT(posts.user_id) as Total_posts
FROM users
LEFT JOIN posts
on users.id = posts.user_id
GROUP BY users.name;