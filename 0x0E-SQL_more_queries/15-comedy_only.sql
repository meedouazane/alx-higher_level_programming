-- lists all Comedy shows in the database hbtn_0d_tvshows
SELECT tv_shows.title AS title
FROM tv_shows INNER JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id
WHERE tv_show_genres.genre_id = 5
ORDER BY title;
