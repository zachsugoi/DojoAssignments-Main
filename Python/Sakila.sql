USE sakila;

/*1*/
SELECT customer.first_name, customer.last_name, customer.email, address.address
FROM customer
INNER JOIN address
	ON customer.address_id = address.address_id
    AND address.city_id = '312'
;

/*2*/
SELECT film.title, film.description, film.release_year, film.rating, film.special_features, category.name AS genre
FROM film
INNER JOIN film_category
	ON film.film_id = film_category.film_id
INNER JOIN category
	ON category.category_id = film_category.category_id
    AND TRIM(category.name) = 'Comedy'
;

/*3*/
SELECT film.title, film.description, film.release_year
FROM film
INNER JOIN film_actor
	ON film.film_id = film_actor.film_id
INNER JOIN actor
	ON actor.actor_id = film_actor.actor_id
    AND actor.actor_id = '5'
;

/*4*/
SELECT customer.first_name, customer.last_name, customer.email, address.address
FROM customer
INNER JOIN address
	ON customer.address_id = address.address_id
    AND address.city_id IN ('1','42','312','459')
WHERE customer.store_id = '1'
;

/*5*/
SELECT  film.title, film.description, film.release_year, film.rating, film.special_features
FROM film
INNER JOIN film_actor
	ON film.film_id = film_actor.film_id
    AND film_actor.actor_id = '15'
WHERE TRIM(film.rating) = 'G'
	AND film.special_features LIKE '%Behind the Scenes%'
;

/*6*/
SELECT film.film_id, film.title, actor.actor_id, CONCAT(actor.first_name, ' ', actor.last_name) AS actor_name
FROM film
INNER JOIN film_actor
	ON film.film_id = film_actor.film_id
INNER JOIN actor
	ON actor.actor_id = film_actor.actor_id
WHERE film.film_id = '369'
;

/*7*/
SELECT film.title, film.description, film.release_year, film.rating, film.special_features, category.name as genre
FROM film
INNER JOIN film_category
	ON film_category.film_id = film.film_id
INNER JOIN category
	ON category.category_id = film_category.category_id
    AND TRIM(category.name) = 'Drama'
WHERE film.rental_rate = '2.99'
;

/*8*/
SELECT film.title, film.description, film.release_year, film.rating, film.special_features, category.name AS genre, actor.first_name, actor.last_name
FROM film
INNER JOIN film_category
	ON film.film_id = film_category.film_id
INNER JOIN category
	ON category.category_id = film_category.category_id
    AND TRIM(category.name) = 'Action'
INNER JOIN film_actor
	ON film.film_id = film_actor.film_id
INNER JOIN actor
	ON actor.actor_id = film_actor.actor_id
    AND actor.first_name = 'SANDRA'
    AND actor.last_name = 'KILMER'
;