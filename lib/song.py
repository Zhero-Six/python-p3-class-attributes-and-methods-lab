# song.py

class Song:
    # Class attributes
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        # Instance attributes
        self.name = name
        self.artist = artist
        self.genre = genre
        
        # Update class attributes through class methods
        self.add_song_to_count()
        self.add_to_genres()
        self.add_to_artists()
        self.add_to_genre_count()
        self.add_to_artist_count()

    @classmethod
    def add_song_to_count(cls):
        """Increment the total song count"""
        cls.count += 1

    @classmethod
    def add_to_genres(cls):
        """Add genre to genres list if not already present"""
        if cls._instance.genre not in cls.genres:
            cls.genres.append(cls._instance.genre)

    @classmethod
    def add_to_artists(cls):
        """Add artist to artists list if not already present"""
        if cls._instance.artist not in cls.artists:
            cls.artists.append(cls._instance.artist)

    @classmethod
    def add_to_genre_count(cls):
        """Update genre count histogram"""
        genre = cls._instance.genre
        cls.genre_count[genre] = cls.genre_count.get(genre, 0) + 1

    @classmethod
    def add_to_artist_count(cls):
        """Update artist count histogram"""
        artist = cls._instance.artist
        cls.artist_count[artist] = cls.artist_count.get(artist, 0) + 1

    def __init_subclass__(cls, **kwargs):
        """Store the current instance for use in class methods"""
        cls._instance = None
        super().__init_subclass__(**kwargs)

    def __new__(cls, *args, **kwargs):
        """Create new instance and store it for class methods"""
        instance = super().__new__(cls)
        cls._instance = instance
        return instance