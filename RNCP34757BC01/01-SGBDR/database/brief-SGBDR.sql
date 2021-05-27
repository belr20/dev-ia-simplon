-- Brief SGBDR 3.
CREATE DATABASE netflix;
USE netflix;

-- Brief SGBDR 4.
CREATE TABLE netflix_titles (
show_id INT NOT NULL,
type_ VARCHAR (10),
title VARCHAR (110),
director VARCHAR (210),
cast VARCHAR (780),
country VARCHAR (130),
date_added VARCHAR (20),
release_year INT NOT NULL,
rating VARCHAR (10),
duration VARCHAR (10),
listed_in VARCHAR (80),
description_ VARCHAR (280)
);
SET GLOBAL local_infile=1;
LOAD DATA LOCAL INFILE '/home/olivier/Documents/Briefes/20201109_Brief_SGBDR/Netflix_Titles.csv' INTO TABLE netflix_titles FIELDS TERMINATED BY ',' ENCLOSED BY '"' LINES TERMINATED BY '\n' IGNORE 1 ROWS;
SELECT * FROM netflix_titles;

-- Brief SGBDR 5.
CREATE TABLE netflix_shows (
title VARCHAR (64),
rating VARCHAR (9),
rating_level VARCHAR (126),
rating_description INT NOT NULL,
release_year INT NOT NULL,
user_rating_score VARCHAR (4),
user_rating_size INT NOT NULL);
LOAD DATA LOCAL INFILE '/home/olivier/Documents/Briefes/20201109_Brief_SGBDR/Netflix_Shows.csv' INTO TABLE netflix_shows CHARACTER SET latin1 FIELDS TERMINATED BY ',' ENCLOSED BY '"' LINES TERMINATED BY '\n' IGNORE 1 ROWS;
SELECT * FROM netflix_shows;

-- Brief SGBDR 6.
SELECT title FROM netflix_titles 
WHERE show_id < 80000000;

-- Brief SGBDR 7.
SELECT title, duration FROM netflix_titles 
WHERE type_ = 'TV Show'
ORDER BY duration;
SELECT title, duration FROM netflix_titles 
WHERE type_ = 'TV Show'
ORDER BY duration DESC;

-- Brief SGBDR 9.
SELECT netflix_titles.title FROM netflix_titles INNER JOIN netflix_shows 
ON netflix_titles.title = netflix_shows.title;

-- Brief SGBDR 10.
SELECT sum(duration) FROM netflix_titles 
WHERE type_ = 'TV Show';

-- Brief SGBDR 11.
SELECT count(*) FROM netflix_shows 
WHERE rating_level IS NOT NULL;

-- Brief SGBDR 12.
SELECT count(*) FROM netflix_titles INNER JOIN netflix_shows 
ON netflix_titles.title = netflix_shows.title AND netflix_shows.release_year >= 2016;
SELECT count(*) FROM netflix_titles INNER JOIN netflix_shows 
ON netflix_titles.title = netflix_shows.title AND netflix_titles.release_year >= 2016;
SELECT count(*) FROM netflix_shows INNER JOIN netflix_titles 
ON netflix_shows.title = netflix_titles.title AND netflix_shows.release_year >= 2016;
SELECT count(*) FROM netflix_shows INNER JOIN netflix_titles 
ON netflix_shows.title = netflix_titles.title AND netflix_titles.release_year >= 2016;

-- Brief SGBDR 13.
ALTER TABLE netflix_shows DROP COLUMN rating;

-- Brief SGBDR 15.
SELECT * FROM netflix_shows WHERE title = 'Marvel''s Iron Fist';
UPDATE netflix_shows SET rating_level = 'C VIDE !!!' WHERE title = 'Marvel''s Iron Fist';
SELECT * FROM netflix_shows WHERE title = 'Marvel''s Iron Fist';

-- Brief SGBDR 14.
ALTER TABLE netflix_shows ADD `id` INT NOT NULL AUTO_INCREMENT primary key first;
DELETE FROM netflix_shows ORDER BY 'id' DESC LIMIT 0, 100;