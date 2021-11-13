from VinylShop.spotify_api.song import Song


class Playlist:
    def __init__(self, name, playlist_id, img='None'):
        self.name = name
        self.playlist_id = playlist_id
        self.songs = list()
        self.img = img

    def add_song(self, song):
        self.songs.append(song)
