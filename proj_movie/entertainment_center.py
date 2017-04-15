import media
import fresh_tomatoes

toystory=media.Movie("Toy Story","This is a story abut a boy",
          "http://ecx.images-amazon.com/images/I/51NpxQ0ma8L.jpg",
          "https://www.youtube.com/watch?v=KYz2wyBy3kc")

print toystory.title
hungergames=media.Movie("The Hunger Games","Story about a fight",
             "http://cdn.collider.com/wp-content/uploads/the-hunger-games-poster.jpg",
             "https://www.youtube.com/watch?v=4S9a5V9ODuY")

sultan=media.Movie("Sultan","Story of a wrestler",
        "https://upload.wikimedia.org/wikipedia/en/3/31/Sultan%27s_logo.jpg",
        "https://www.youtube.com/watch?v=wPxqcq6Byq0")

shareek=media.Movie("Shareek"," About fight amongst brothers",
         "https://upload.wikimedia.org/wikipedia/en/2/2f/Shareek_movie_poster.jpg",
         "https://www.youtube.com/watch?v=GP2w3ekng90")

findingdory= media.Movie("Finding Dory"," A story of a fish",
                         "https://upload.wikimedia.org/wikipedia/en/3/3e/Finding_Dory.jpg",
                         "https://www.youtube.com/watch?v=3JNLwlcPBPI")
                         

#shareek.show_trailer()

movies=[toystory, hungergames, sultan, shareek, findingdory]



fresh_tomatoes.open_movies_page(movies)
