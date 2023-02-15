-- MySQL Countries

-- Querie 1
-- What query would you run to get all the countries that speak Slovene? Your query should return the name of the country, language and language percentage. Your query should arrange the result by language percentage in descending order.

SELECT countries.name AS country, languages.language, languages.percentage
FROM countries
JOIN languages ON countries.id = languages.country_id
WHERE languages.language = 'Slovene'
ORDER BY languages.percentage DESC;

-- Querie 2
-- What query would you run to display the total number of cities for each country? Your query should return the name of the country and the total number of cities. Your query should arrange the result by the number of cities in descending order.

-- SOLUTION 1 (Without languages)
SELECT countries.name AS Country, COUNT(cities.country_id) AS Number_of_Cities
FROM countries
JOIN cities ON countries.id = cities.country_id
GROUP BY countries.id
ORDER BY Number_of_Cities DESC;

-- SOLUTION 1 (With languages)
SELECT countries.name AS Country, COUNT(cities.country_id) AS Number_of_Cities, countries_and_languages.languages AS Languages
FROM countries
JOIN cities ON countries.id = cities.country_id
JOIN (
		SELECT languages.country_id AS 'country_id', GROUP_CONCAT(DISTINCT language SEPARATOR ', ') AS 'Languages'
		FROM languages
		GROUP BY languages.country_id
    ) AS countries_and_languages
ON countries_and_languages.country_id = countries.id
GROUP BY countries.id
ORDER BY Number_of_Cities DESC;

-- Querie 3
-- What query would you run to get all the cities in Mexico with a population of greater than 500,000? Your query should arrange the result by population in descending order.

SELECT cities.name AS city, cities.population
FROM countries
JOIN cities ON countries.id = cities.country_id
WHERE countries.name = 'MEXICO' AND cities.population> 500000
ORDER BY cities.population DESC;

-- Querie 4
-- What query would you run to get all languages in each country with a percentage greater than 89%? Your query should arrange the result by percentage in descending order. 

SELECT countries.name, languages.language, languages.percentage
FROM countries
JOIN languages ON countries.id = languages.country_id
WHERE languages.percentage > 0.89
ORDER BY languages.percentage DESC;

-- Querie 5
-- What query would you run to get all the countries with Surface Area below 501 and Population greater than 100,000?

SELECT countries.name AS country, countries.surface_area, countries.population
FROM countries
WHERE countries.surface_area <  501 AND countries.population > 100000;

-- Querie 6
-- What query would you run to get countries with only Constitutional Monarchy with a capital greater than 200 and a life expectancy greater than 75 years?

SELECT countries.name AS country
FROM countries
WHERE countries.government_form = 'Constitutional Monarchy' AND countries.capital > 200 AND countries.life_expectancy > 75;

-- Querie 7
--  What query would you run to get all the cities of Argentina inside the Buenos Aires district and have the population greater than 500, 000? The query should return the Country Name, City Name, District and Population. 

SELECT cities.name AS city
FROM cities
WHERE cities.country_code = 'ARG' AND cities.district = 'Buenos Aires' AND cities.population > 500000;

-- Querie 8
--  What query would you run to get all the cities of Argentina inside the Buenos Aires district and have the population greater than 500, 000? The query should return the Country Name, City Name, District and Population. 

SELECT countries.region, COUNT(countries.id) AS number_of_countries
FROM countries
GROUP BY countries.region
ORDER BY COUNT(countries.id) DESC;