-- script that lists all genres in the database hbtn_0d_tvshows_rate by their rating
SELECT tv_genres.name AS name, SUM(tv_show_ratings) AS rating
FROM tv_show_ratings
JOIN tv_shows ON tv_shows.id = tv_show_ratings.show_id
JOIN tv_genres ON tv_genres.name = 
