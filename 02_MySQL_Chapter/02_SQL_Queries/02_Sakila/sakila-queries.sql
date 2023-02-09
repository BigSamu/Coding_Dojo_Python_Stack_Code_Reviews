-- MySQL Countries

-- Querie 1
-- What query would you run to get all the customers inside city_id = 312? Your query should return customer first name, last name, email, and address.


-- SOLUTION 1 
SELECT customer.first_name, customer.last_name, customer.email, address.address
FROM customer 
JOIN address ON customer.address_id = address.address_id
WHERE address.city_id = 312;

-- SOLUTION 2 
SELECT joint.first_name, joint.last_name, joint.email, joint.address
FROM (
	SELECT first_name, last_name, email, address, city_id
	FROM customer 
	JOIN address 
    ON customer.address_id = address.address_id
) AS joint
WHERE joint.city_id = 312;


-- Querie 2
-- What query would you run to get all comedy films? Your query should return film title, description, release year, rating, special features, and genre (category).

SELECT film.title, film.description AS 'Description', film.release_year AS 'Release Year', film.rating, film.special_features, category.name AS 'Genre'
FROM film
JOIN film_category ON film.film_id = film_category.film_id
JOIN category ON film_category.category_id = category.category_id
WHERE category.name = 'Comedy';
