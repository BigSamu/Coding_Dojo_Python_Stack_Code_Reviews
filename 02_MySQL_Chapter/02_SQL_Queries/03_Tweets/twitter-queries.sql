-- Only 5 Users (Kobe, Vince, Alien, Tracy, Rajon)
SELECT id, first_name
FROM users;

-- Get tweets of all Users included Rajon that does not have tweets (NULL value)
SELECT users.id, users.first_name, tweets.tweet
FROM users
LEFT JOIN tweets
ON users.id = tweets.user_id;

-- Get tweets of all Users excluding Rajon that does not have tweets 
SELECT users.id, first_name, tweet
FROM users
JOIN tweets
ON users.id = tweets.user_id;