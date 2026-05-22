class Song:
    """
    Class to represent Song
    Attributes:
        title (str): The title of the song.
        artist (Nameof Artist): The artist who performed the song.
        duration (int): The duration of the song in seconds.
    """
    def __init__(self, title, artist, duration):
        # """
        # Initializes a Song instance.
        # Args:
        #     title (str): The title of the song.
        #     artist (Nameof Artist): The artist who performed the song.
        #     duration (int): The duration of the song in seconds.
        # """
        self.title = title
        self.artist = artist
        self.duration = duration

help(Song)
help(Song.__init__)
Song.__init__.__doc__ = """
        Initializes a Song instance.
        Args:
            title (str): The title of the song.
            artist (Nameof Artist): The artist who performed the song.
            duration (int): The duration of the song in seconds.
        """

help(Song.__init__)
# help(Song.__doc__)




