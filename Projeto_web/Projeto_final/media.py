import webbrowser

class Movie():
    """This class provides a way to store movie related information"""
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        """This function constructs an instance of Movies class for each movie information
        The arguments are assigned to the corresponding intance variables and return the movie information
        Args:
            movie_tiles (str): holds the title of the movie that is a input
            movie_storyline (str): holds the information about the movie story
            poster_image (str): holds a url linked to the movie poster
            trailer_youtube (str): holds a url linked to the movie trailer
        returns:
            Returns a instance that hold the movie information to print them
        """
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """This function open the url link to movie trailer on a webbrowser""" 
        webbrowser.open (self.trailer_youtube_url)
