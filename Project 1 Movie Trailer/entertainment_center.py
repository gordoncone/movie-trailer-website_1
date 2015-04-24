import fresh_tomatoes
import media

#Instances of class Movie
The_300 = media.Movie("The 300","300 Spartan Soldiers standup against an army to protect Greece ",
                        "http://a5.mzstatic.com/us/r30/Video/v4/73/f9/07/73f9071b-c857-9d23-b4c4-b89a93b73d3e/poster212x312.jpeg",
                        "https://www.youtube.com/watch?v=wDiUG52ZyHQ")


avatar = media.Movie("Avatar", "A marine on a alien planet",
                     "http://ia.media-imdb.com/images/M/MV5BMTYwOTEwNjAzMl5BMl5BanBnXkFtZTcwODc5MTUwMw@@._V1_SX640_SY720_.jpg",
                     "https://www.youtube.com/watch?v=d1_JBMrrYw8")


the_notebook = media.Movie("The Notebook", "Boy & Girl Falls in love",
                           "http://uk.nicholassparks.com/wp-content/uploads/sites/3/1996/07/notebook-680x1020.jpg",
                           "https://www.youtube.com/watch?v=4M7LIcH8C9U")



lion_king = media.Movie("Lion King", "Young Lion Grows up to Become King",
                           "http://ia.media-imdb.com/images/M/MV5BMjEyMzgwNTUzMl5BMl5BanBnXkFtZTcwNTMxMzM3Ng@@._V1_SX640_SY720_.jpg",
                           "https://www.youtube.com/watch?v=4sj1MT05lAA")


bad_boys = media.Movie("Bad Boys", "Two cops lead a major drug bust that saved the police department",
                           "http://ia.media-imdb.com/images/M/MV5BMTY4NDk1NTU5NF5BMl5BanBnXkFtZTcwMjE2NDU2MQ@@._V1_SX640_SY720_.jpg",
                           "hhttps://www.youtube.com/watch?v=ty8eBdHaf1c")

rush_hour = media.Movie("Rush Hour", " LAPD and Chinese cop team up to save a little girl and bust a major gang ring",
                           "http://ia.media-imdb.com/images/M/MV5BMjAyMzAyNzY5N15BMl5BanBnXkFtZTcwNjU3MTc0MQ@@._V1_SX640_SY720_.jpg",
                           "https://www.youtube.com/results?search_query=rush+hour+trailer")

#Enable Movie Trailer to Open
movies = [The_300, avatar, the_notebook, lion_king, bad_boys, rush_hour,]
fresh_tomatoes.open_movies_page(movies)
