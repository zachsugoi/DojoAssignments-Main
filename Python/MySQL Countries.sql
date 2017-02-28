USE world;

/*1*/
SELECT countries.name, languages.language, languages.percentage
FROM countries
INNER JOIN languages
	ON countries.id = languages.country_id
WHERE languages.language = 'Slovene'
ORDER BY languages.percentage DESC
;

/*2*/
SELECT countries.name, COUNT(DISTINCT cities.name) AS city_count
FROM countries
LEFT JOIN cities
	ON countries.id = cities.country_id
GROUP BY countries.name
ORDER BY city_count DESC
;

/*3*/
SELECT cities.name, cities.population
FROM countries
INNER JOIN cities
	ON countries.id = cities.country_id
WHERE countries.name = 'Mexico'
	AND cities.population > 500000
ORDER BY cities.population DESC
;

/*4*/
SELECT languages.language, countries.name AS country, languages.percentage
FROM countries
INNER JOIN languages
	ON countries.id = languages.country_id
	AND languages.percentage > 89
ORDER BY languages.percentage DESC
;

/*5*/
SELECT countries.name, countries.surface_area, countries.population
FROM countries
WHERE countries.surface_area < 501
	AND countries.population > 100000
;

/*6*/
SELECT countries.name, countries.government_form, countries.capital, countries.life_expectancy
FROM countries
WHERE countries.government_form LIKE 'Constitutional Monarchy%'
	AND countries.capital > 200
    AND countries.life_expectancy > 75
;

/*7*/
SELECT countries.name AS country, cities.name AS city, cities.district, cities.population
FROM countries
INNER JOIN cities
	ON countries.id = cities.country_id
    AND cities.district = 'Buenos Aires'
    AND cities.population > 500000
WHERE countries.name = 'Argentina'
;

/*8*/
SELECT countries.region, COUNT(DISTINCT countries.name) as country_count
FROM countries
GROUP BY countries.region
ORDER BY country_count DESC
;