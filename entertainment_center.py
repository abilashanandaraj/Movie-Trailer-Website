"""Stores the details of the movie and displays them on website."""
import fresh_tomatoes
import media

"""Declare favorite movies with 4 args each with movie title,
    movie storyline, movie poster image and movie youtube trailer."""
toy_story = media.Movie(
            "Toy Story",
            "A story of a boy and his toys that comes to life",
            "http://www.gstatic.com/tv/thumb/movieposters/17420/p17420_p_v8_ab.jpg",  # NOQA
            "https://www.youtube.com/watch?v=KYz2wyBy3kc")


avatar = media.Movie(
            "Avatar",
            "A marine on an alien planet",
            "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",  # NOQA
            "https://www.youtube.com/watch?v=5PSNL1qE6VY")

black_panther = media.Movie(
            "Black Panther",
            "the King of Wakanda, rises to the throne in the isolated,"
            "technologically advanced African nation, but his claim is"
            "challenged by a vengeful outsider who was a childhood"
            "victim of T'Challa's father's mistake.",
            "https://vignette.wikia.nocookie.net/marvelcinematicuniverse/images/6/60/Black_Panther_Textless_Character_Poster_01.jpg/revision/latest/scale-to-width-down/350?cb=20171201051945",  # NOQA
            "https://www.youtube.com/watch?v=xjDjIWPwcPU")


spider_man_homecoming = media.Movie(
            "Spiderman: Homecoming",
            "Peter Parker balances his life as an ordinary high school student"
            "in Queens with his superhero alter-ego Spider-Man,"
            "and finds himself on the trail of a new menace prowling"
            "the skies of New York City.",
            "http://t1.gstatic.com/images?q=tbn:ANd9GcQkBgGCS74dHRSe3i0fkEsdaC1jJPU4px6Pyv9-TOipm13gOprI",  # NOQA
            "https://www.youtube.com/watch?v=U0D3AOldjMU")

the_shape_of_water = media.Movie(
            "The Shape of Water",
            "At a top secret research facility in the 1960s,"
            "a lonely janitor forms a unique relationship with"
            "an amphibious creature that is being held in captivity.",
            "http://t1.gstatic.com/images?q=tbn:ANd9GcQmGqEyb3hsJDLbBH_mjF8jT-30QUY6KgQhVvsJCr86QFnO4NFu",  # NOQA
            "https://www.youtube.com/watch?v=XFYWazblaUA")

maze_runner_the_death_cure = media.Movie(
            "Maze Runner: The Death Cure",
            "Young hero Thomas embarks on a mission to find a cure"
            "for a deadly disease known as the Flare.",
            "https://upload.wikimedia.org/wikipedia/en/e/eb/MazeRunnerDeathCureFinalPoster.jpeg",  # NOQA
            "https://www.youtube.com/watch?v=4-BTxXm8KSg")

# Assign all movies to movies array
movies = [
            toy_story,
            avatar,
            black_panther,
            spider_man_homecoming,
            the_shape_of_water,
            maze_runner_the_death_cure
         ]

# Opens the movie website with all movies featuring above
fresh_tomatoes.open_movies_page(movies)
