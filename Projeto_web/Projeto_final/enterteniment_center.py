import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story", "A story of boy and his toys that come to life", "https://upload.wikimedia.org/wikipedia/pt/d/dc/Movie_poster_toy_story.jpg", "https://www.youtube.com/watch?v=KYz2wyBy3kc")
avatar = media.Movie("Avatar", "A marine on a alien planet", "https://upload.wikimedia.org/wikipedia/pt/b/b0/Avatar-Teaser-Poster.jpg", "https://www.youtube.com/watch?v=5PSNL1qE6VY")
august_osage = media.Movie ("August osage: county", "A family drama with a mother who has mouth cancer", "https://upload.wikimedia.org/wikipedia/pt/4/42/Poster_august.jpg", "https://www.youtube.com/watch?v=9Hd_uO72h1s")
la_vie_en_rose = media.Movie ("Edith Piaf: La vie en rose", "Une chanteuse et leurs amours par les hommes et la musique.", "https://upload.wikimedia.org/wikipedia/pt/f/f6/La_Vie_en_Rose.png", "https://www.youtube.com/watch?v=uzEJ7NV_g98")
marguerite = media.Movie ("Marguerite", "A bad singer who believes that has a great voice.", "http://t1.gstatic.com/images?q=tbn:ANd9GcQJGMGHth44ve_8ma85D5eheBmBcy8VVYcqVHmpR0aU7V_MfVpF", "https://www.youtube.com/watch?v=AZsgWFITTu8")

movies = [toy_story, avatar, august_osage, la_vie_en_rose, marguerite]

#open the web page on webbrowser and display information about "movie"
fresh_tomatoes.open_movies_page(movies)
