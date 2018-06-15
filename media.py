"""The Movie class that contains the details of a movie."""
import webbrowser


class Movie():
    """This class stores movie related information.
    Args:
        title: A string to store title of the movie.
        storyline: A string to store the plot of the movie.
        poster_image_url: A string to store the URL of movie poster.
        trailer_youtube_url: A string to store the URL of movie trailer."""

    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        """Initialises Movie class instance variables."""
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """ Opens trailer in a web browser """
        webbrowser.open(self.trailer_youtube_url)
