-- lists all shows without the genre Comedy in the database hbtn_0d_tvshows.
SELECT tv_shows.title AS title
FROM tv_shows
JOIN tv_show_genres ON tv_show_genres.show_id = tv_shows.id
WHERE tv_show_genres.genre_id != 5
GROUP BY title
ORDER BY title;
