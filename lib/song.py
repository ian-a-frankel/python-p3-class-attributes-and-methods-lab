class Song:

    count = 0
    genres = []
    artists = []

    artist_count = {}
    genre_count = {}

    @classmethod
    def add_song_to_count(cls, genre, artist):
        cls.count += 1
        cls.artist_count[artist] += 1
        cls.genre_count[genre] +=1

    def __init__(self,name,artist,genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        if self.genre not in Song.genres:
            Song.genres.append(self.genre)
            Song.genre_count[genre] = 0
        if artist not in Song.artists:
            Song.artists.append(artist)
            Song.artist_count[artist] = 0
        Song.add_song_to_count(genre, artist)
        
