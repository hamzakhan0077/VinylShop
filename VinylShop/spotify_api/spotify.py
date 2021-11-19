from requests import Request, post, put, get
from VinylShop.spotify_api.playlist import Playlist
from  VinylShop.spotify_api.song import Song
from pickle import *
from VinylShop.spotify_api.credentials import *
from flask import redirect
from copy import deepcopy
from flask import session

BASE_URL = "https://api.spotify.com/v1/"

null = None
false = False
true = True

availableVinyls = {'ab67616d0000b273692d9189b2bd75525893f0c1':"The Beatles",
                       'ab67616d0000b273370c12f82872c9cfaee80193':"Tame Impala",
                       'ab67616d0000b2734ada80e2e0d11d8f6a99d42e':"Pink Floyd"}



EXAMPLE_PLAYLISTS_RESPONSE = {
  "href": "https://api.spotify.com/v1/users/9zjte07qm6qxb3ynn9bm6atiu/playlists?offset=0&limit=3",
  "items": [
    {
      "collaborative": false,
      "description": "",
      "external_urls": {
        "spotify": "https://open.spotify.com/playlist/5p4U0hdrqumFpgpfIN30Eq"
      },
      "href": "https://api.spotify.com/v1/playlists/5p4U0hdrqumFpgpfIN30Eq",
      "id": "5p4U0hdrqumFpgpfIN30Eq",
      "images": [
        {
          "height": 640,
          "url": "https://mosaic.scdn.co/640/ab67616d0000b273176e82d09ac75d62810f0056ab67616d0000b273692d9189b2bd75525893f0c1ab67616d0000b273bfa99afb5ef0d26d5064b23bab67616d0000b273ca69f52416a728ebd0b9103c",
          "width": 640
        },
        {
          "height": 300,
          "url": "https://mosaic.scdn.co/300/ab67616d0000b273176e82d09ac75d62810f0056ab67616d0000b273692d9189b2bd75525893f0c1ab67616d0000b273bfa99afb5ef0d26d5064b23bab67616d0000b273ca69f52416a728ebd0b9103c",
          "width": 300
        },
        {
          "height": 60,
          "url": "https://mosaic.scdn.co/60/ab67616d0000b273176e82d09ac75d62810f0056ab67616d0000b273692d9189b2bd75525893f0c1ab67616d0000b273bfa99afb5ef0d26d5064b23bab67616d0000b273ca69f52416a728ebd0b9103c",
          "width": 60
        }
      ],
      "name": "T6 - Big Chungus Waz Ere",
      "owner": {
        "display_name": "johncaffrey",
        "external_urls": {
          "spotify": "https://open.spotify.com/user/creedbrattonheymah"
        },
        "href": "https://api.spotify.com/v1/users/creedbrattonheymah",
        "id": "creedbrattonheymah",
        "type": "user",
        "uri": "spotify:user:creedbrattonheymah"
      },
      "primary_color": null,
      "public": false,
      "snapshot_id": "NDcsN2FhYTU1MGUwMGZkODVkYjY5MjNjZWExMTY3MDI4YWZjY2FkYjI3OQ==",
      "tracks": {
        "href": "https://api.spotify.com/v1/playlists/5p4U0hdrqumFpgpfIN30Eq/tracks",
        "total": 69
      },
      "type": "playlist",
      "uri": "spotify:playlist:5p4U0hdrqumFpgpfIN30Eq"
    },
    {
      "collaborative": false,
      "description": "",
      "external_urls": {
        "spotify": "https://open.spotify.com/playlist/2LhU2BKMxiPDHjdM4QWzrq"
      },
      "href": "https://api.spotify.com/v1/playlists/2LhU2BKMxiPDHjdM4QWzrq",
      "id": "2LhU2BKMxiPDHjdM4QWzrq",
      "images": [
        {
          "height": 640,
          "url": "https://mosaic.scdn.co/640/ab67616d0000b273176e82d09ac75d62810f0056ab67616d0000b2732557f5ed1ca07d5111d49b93ab67616d0000b27334ef8f7d06cf2fc2146f420aab67616d0000b27358267bd34420a00d5cf83a49",
          "width": 640
        },
        {
          "height": 300,
          "url": "https://mosaic.scdn.co/300/ab67616d0000b273176e82d09ac75d62810f0056ab67616d0000b2732557f5ed1ca07d5111d49b93ab67616d0000b27334ef8f7d06cf2fc2146f420aab67616d0000b27358267bd34420a00d5cf83a49",
          "width": 300
        },
        {
          "height": 60,
          "url": "https://mosaic.scdn.co/60/ab67616d0000b273176e82d09ac75d62810f0056ab67616d0000b2732557f5ed1ca07d5111d49b93ab67616d0000b27334ef8f7d06cf2fc2146f420aab67616d0000b27358267bd34420a00d5cf83a49",
          "width": 60
        }
      ],
      "name": "Stephen’s Opti 24th Sep 2021",
      "owner": {
        "display_name": "Paulcaff123",
        "external_urls": {
          "spotify": "https://open.spotify.com/user/9zjte07qm6qxb3ynn9bm6atiu"
        },
        "href": "https://api.spotify.com/v1/users/9zjte07qm6qxb3ynn9bm6atiu",
        "id": "9zjte07qm6qxb3ynn9bm6atiu",
        "type": "user",
        "uri": "spotify:user:9zjte07qm6qxb3ynn9bm6atiu"
      },
      "primary_color": null,
      "public": false,
      "snapshot_id": "MjM1LDM0MzM4M2UxMWVkYjQwZDc2OTk5NDM2NzgxM2IyNjE5NzY3OTA3NWE=",
      "tracks": {
        "href": "https://api.spotify.com/v1/playlists/2LhU2BKMxiPDHjdM4QWzrq/tracks",
        "total": 70
      },
      "type": "playlist",
      "uri": "spotify:playlist:2LhU2BKMxiPDHjdM4QWzrq"
    },
    {
      "collaborative": false,
      "description": "The songs that influenced everything that has happened since. Cover: Jimi Hendrix",
      "external_urls": {
        "spotify": "https://open.spotify.com/playlist/37i9dQZF1DX5qNE4zrflL7"
      },
      "href": "https://api.spotify.com/v1/playlists/37i9dQZF1DX5qNE4zrflL7",
      "id": "37i9dQZF1DX5qNE4zrflL7",
      "images": [
        {
          "height": null,
          "url": "https://i.scdn.co/image/ab67706f00000003a37256f94f873658dfd43bb6",
          "width": null
        }
      ],
      "name": "Alternative 60s",
      "owner": {
        "display_name": "Spotify",
        "external_urls": {
          "spotify": "https://open.spotify.com/user/spotify"
        },
        "href": "https://api.spotify.com/v1/users/spotify",
        "id": "spotify",
        "type": "user",
        "uri": "spotify:user:spotify"
      },
      "primary_color": null,
      "public": false,
      "snapshot_id": "MTYzMzQ5MTc5MiwwMDAwMDAwNzAwMDAwMTdjNTNiMmIzZGEwMDAwMDE3YzUzOWVjNDgw",
      "tracks": {
        "href": "https://api.spotify.com/v1/playlists/37i9dQZF1DX5qNE4zrflL7/tracks",
        "total": 80
      },
      "type": "playlist",
      "uri": "spotify:playlist:37i9dQZF1DX5qNE4zrflL7"
    }
  ],
  "limit": 3,
  "next": "https://api.spotify.com/v1/users/9zjte07qm6qxb3ynn9bm6atiu/playlists?offset=3&limit=3",
  "offset": 0,
  "previous": null,
  "total": 71
}

EXAMPLE_RESPONSE = {
  "items": [
    {
      "track": {
        "album": {
          "artists": [
            {
              "external_urls": {
                "spotify": "https://open.spotify.com/artist/3WrFJ7ztbogyGnTHbHJFl2"
              },
              "href": "https://api.spotify.com/v1/artists/3WrFJ7ztbogyGnTHbHJFl2",
              "id": "3WrFJ7ztbogyGnTHbHJFl2",
              "name": "The Beatles",
              "type": "artist",
              "uri": "spotify:artist:3WrFJ7ztbogyGnTHbHJFl2"
            }
          ],
          "href": "https://api.spotify.com/v1/albums/2BtE7qm1qzM80p9vLSiXkj",
          "id": "2BtE7qm1qzM80p9vLSiXkj",
          "name": "Magical Mystery Tour (Remastered)"
        },
        "href": "https://api.spotify.com/v1/tracks/0qHMhBZqYb99yhX9BHcIkV",
        "id": "0qHMhBZqYb99yhX9BHcIkV",
        "name": "Magical Mystery Tour - Remastered 2009"
      }
    },
      {
          "track": {
              "album": {
                  "artists": [
                      {
                          "external_urls": {
                              "spotify": "https://open.spotify.com/artist/16eRpMNXSQ15wuJoeqguaB"
                          },
                          "href": "https://api.spotify.com/v1/artists/16eRpMNXSQ15wuJoeqguaB",
                          "id": "16eRpMNXSQ15wuJoeqguaB",
                          "name": "The Flaming Lips",
                          "type": "artist",
                          "uri": "spotify:artist:16eRpMNXSQ15wuJoeqguaB"
                      }
                  ],
                  "href": "https://api.spotify.com/v1/albums/49LA20VMk65fQyEaIzYdvf",
                  "id": "49LA20VMk65fQyEaIzYdvf",
                  "name": "Yoshimi Battles the Pink Robots"
              },
              "href": "https://api.spotify.com/v1/tracks/0ScgmigVOJr2mFsAtwFQmz",
              "id": "0ScgmigVOJr2mFsAtwFQmz",
              "name": "Fight Test"
          }
      },
{
      "track": {
        "album": {
          "artists": [
            {
              "external_urls": {
                "spotify": "https://open.spotify.com/artist/16eRpMNXSQ15wuJoeqguaB"
              },
              "href": "https://api.spotify.com/v1/artists/16eRpMNXSQ15wuJoeqguaB",
              "id": "16eRpMNXSQ15wuJoeqguaB",
              "name": "The Flaming Lips",
              "type": "artist",
              "uri": "spotify:artist:16eRpMNXSQ15wuJoeqguaB"
            }
          ],
          "href": "https://api.spotify.com/v1/albums/49LA20VMk65fQyEaIzYdvf",
          "id": "49LA20VMk65fQyEaIzYdvf",
          "name": "Yoshimi Battles the Pink Robots"
        },
        "href": "https://api.spotify.com/v1/tracks/0ScgmigVOJr2mFsAtwFQmz",
        "id": "0ScgmigVOJr2mFsAtwFQmz",
        "name": "Fight Test"
      }
    },
    {
      "track": {
        "album": {
          "artists": [
            {
              "external_urls": {
                "spotify": "https://open.spotify.com/artist/0epOFNiUfyON9EYx7Tpr6V"
              },
              "href": "https://api.spotify.com/v1/artists/0epOFNiUfyON9EYx7Tpr6V",
              "id": "0epOFNiUfyON9EYx7Tpr6V",
              "name": "The Strokes",
              "type": "artist",
              "uri": "spotify:artist:0epOFNiUfyON9EYx7Tpr6V"
            }
          ],
          "href": "https://api.spotify.com/v1/albums/2xkZV2Hl1Omi8rk2D7t5lN",
          "id": "2xkZV2Hl1Omi8rk2D7t5lN",
          "name": "The New Abnormal"
        },
        "href": "https://api.spotify.com/v1/tracks/5ruzrDWcT0vuJIOMW7gMnW",
        "id": "5ruzrDWcT0vuJIOMW7gMnW",
        "name": "The Adults Are Talking"
      }
    }
  ]
}


at = None

def get_auth_code():
    scopes = 'playlist-read-private playlist-read-collaborative user-library-read user-top-read user-read-private user-read-email'

    url = Request('GET', 'https://accounts.spotify.com/authorize',
                  params={
                      'scope': scopes,
                      'response_type': 'code',
                      'redirect_uri': REDIRECT_URI,
                      'client_id': CLIENT_ID
                  }).prepare().url

    return url


def spotify_callback(request):
    code = request.args['code']

    response = post('https://accounts.spotify.com/api/token', data={
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': REDIRECT_URI,
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET
    }).json()

    access_token = response.get('access_token')
    token_type = response.get('token_type')
    refresh_token = response.get('refresh_token')
    expires_in = response.get('expires_in')
    error = response.get('error')

    global at

    at = access_token

    return redirect(SERVER_URL+"/displayPlaylists/" + str(access_token))


def spotify_api_request(endpoint, at, post_=False, put_=False):
    #access_token = at  # FIX - User token
    access_token = session.get('access_token')
    headers = {'Content-Type': 'application/json',
               'Authorization': "Bearer " + access_token}

    if post_:
        post(BASE_URL + endpoint, headers=headers)
    if put_:
        put(BASE_URL + endpoint, headers=headers)

    response = get(BASE_URL + endpoint, {}, headers=headers)
    try:
        return response.json()
    except:
        return {'Error': 'Issue with request'}


def get_playlists(at):
    endpoint = "me/playlists"  # "users/user_id/playlists"
    response = spotify_api_request(endpoint, at)


    if 'error' in response or 'items' not in response:
        print("ERROR IN RESPONSE FOR PLAYLISTS")
        return response, None  # FIX: RETURN AN ERROR

    playlists_dictionary = response.get('items')

    playlists = list()

    for playlist in playlists_dictionary:
        playlists.append({'name': playlist['name'], 'id': playlist['id'],
                          'playlist_img': playlist['images'][0]['url'][27:]})

    return playlists




def get_songs_in_playlist(playlist_id, at, playlist_obj=None):
    playlist = playlist_obj
    if playlist is None:
        print("Printing")
        playlist = uploadPlaylist(playlist_id, at, save_playlist=False)

    songs = list()

    for song in playlist.songs:
        songs.append({'name': song.name, 'artist': song.artist,
                      'album': song.album, 'album_img': song.album_img, 'artist_img': song.artist_img})

    return songs


def make_playlist_objects():
    playlist_ids, playlist_names = get_playlists()
    playlist_objects = list()
    for i in range(len(playlist_ids)):
        playlistID = playlist_ids[i]
        playlistName = playlist_names[i]
        newPlaylist = Playlist(playlistName, playlistID)
        playlist_objects.append(newPlaylist)


def find_most_popular_album(playlist):
    albums = dict()
    highest_album_amount = 0
    highest_album_name = ""
    for song in playlist.songs:
        album = song.album
        if album in albums:
            albums[album] += 1
        else:
            albums[album] = 1
        if albums[album] > highest_album_amount:
            highest_album_name = album
            highest_album_amount = albums[album]
    print(highest_album_amount, highest_album_name)


def getTopArtists(playlist):
    artists = dict()
    playlist_songs = deepcopy(playlist.songs)
    for song in playlist_songs:
        artist = song.artist
        if artist in artists:
            artists[artist]['count'] += 1
        else:
            artists[artist] = {'count':1, 'song':song}
    sortedArtists = sorted(artists, key=lambda i: artists[i]['count'], reverse=True)
    orderedArtists = list()
    position = 0
    for artist in sortedArtists:
        song_of_artist = artists[artist]['song']
        artist_img = song_of_artist.artist_img
        count = artists[artist]['count']
        artist_info = {'name': artist, 'artist_img': artist_img, 'count': count, 'position': str(position)}
        position += 1
        orderedArtists.append(artist_info)
    return orderedArtists


def getTopAlbums(playlist):
    albums = dict()
    playlist_songs = deepcopy(playlist.songs)
    for song in playlist_songs:
        album = song.album
        if album in albums:
            albums[album]['count'] += 1
        else:
            albums[album] = {'count': 1, 'song': song}
    sortedAlbums = sorted(albums, key=lambda i: albums[i]['count'], reverse=True)
    orderedAlbums = list()
    for album in sortedAlbums:
        song_of_album = albums[album]['song']
        album_img = song_of_album.album_img
        artist = song_of_album.artist
        count = albums[album]['count']
        album_info = {'name': album, 'album_img': album_img, 'artist': artist, 'count': count}
        orderedAlbums.append(album_info)
    return orderedAlbums


def find_most_popular_artist(playlist):
    artists = dict()
    highest_artist_amount = 0
    highest_artist_name = ""
    for song in playlist.songs:
        artist = song.artist
        if artist in artists:
            artists[artist] += 1
        else:
            artists[artist] = 1
        if artists[artist] > highest_artist_amount:
            highest_artist_name = artist
            highest_artist_amount = artists[artist]
    print(highest_artist_name, highest_artist_amount)


def getArtistImages(artistIDs, accessToken=None):
    global at
    if accessToken is None:
        accessToken = at

    artist_id_string = ""

    count = 0
    for artist in artistIDs:
        if count == 0:
            artist_id_string += artist
        else:
            artist_id_string += "%2C" + artist
        count += 1

    endpoint = "artists?ids=" + artist_id_string
    response = spotify_api_request(endpoint, accessToken)

    if 'error' in response or 'artists' not in response:
        print(response)
        return  # FIX: RETURN AN ERROR

    artists_list = response.get('artists')
    artistImgs = list()

    for artist in artists_list:
        artistImgs.append(artist['images'][0]['url'][24:])

    print("Artist imgs", artistImgs)

    return artistImgs


def updateArtistImages(playlist):
    artistIDs = list()

    songs = playlist.songs

    for song in songs:
        artistIDs.append(song.artistID)

    artistImgs = getArtistImages(artistIDs)

    count = 0
    for song in songs:
        song.artist_img = artistImgs[count]
        count += 1


def uploadPlaylist(playlist_id, at, playlist_name='Playlist', playlist_img='None', save_playlist=False):

    endpoint = "playlists/" + playlist_id + "/tracks?fields=items(track(name%2Chref%2Calbum(name%2Chref%2Cimages%2C%20artists)))&limit=50"
    response = spotify_api_request(endpoint, at)

    if 'error' in response or 'items' not in response:
        print(response)
        return  # FIX: RETURN AN ERROR

    songs_dictionary = response.get('items')  

    songs = list()

    for song in songs_dictionary:
        track = song['track']
        name = track['name']
        song_id = 2
        album = track['album']['name']
        artist = track['album']['artists'][0]['name']
        artistID = track['album']['artists'][0]['id']
        artist_img = track['album']['images'][0]['url'][24:]
        album_img = track['album']['images'][0]['url'][24:]

        newSong = Song(name, song_id, album, artist, artistID, artist_img=artist_img, album_img=album_img)

        songs.append(newSong)

    playlist_obj = Playlist(playlist_name, playlist_id, img=playlist_img)
    playlist_obj.songs = songs

    if save_playlist:
        print("Saved playlist to database") # FIX DATABASE STUFF

    updateArtistImages(playlist_obj)

    return playlist_obj


def getAvailableVinylsByArtist(artist_name):
    global availableVinyls
    vinyls = list()
    for vinyl in availableVinyls:
        if availableVinyls[vinyl] == artist_name:
            vinyls.append(vinyl)

    return vinyls


def checkAlbumAvailability(album):
    global availableVinyls
    if album in availableVinyls:
        return True
    return False
