-- Lists all the cities of California
-- Query that lists all the cities of California that can be found in the database hbtn_0d_usa.
SELECT id, name
FROM cities
WHERE state_id = ( -- Query to get the California's id
	SELECT id
	FROM states
	WHERE name = "California"
)
ORDER BY id;
