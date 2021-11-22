from flask import Flask,render_template, url_for,flash, redirect,request,abort, session

from VinylShop.forms import *
from flask_login import login_user,current_user,logout_user,login_required
from VinylShop.spotify_api import spotify, playlist, song, credentials
from VinylShop.spotify_api.credentials import SERVER_URL
from VinylShop.models import *

from VinylShop import app,db,bcrypt

# ALL Pages configuration goes in here

PLAYLIST_UPLOAD_URL = SERVER_URL + "/uploadPlaylist"
IMAGE_BASE = "https://i.scdn.co/image/"

## PLACEHOLDERS BEFORE USING A DATABASE
at = None  # TO DO: STORE ACCESS TOKENS FOR EACH USER
uploadedPlaylist = None
playlistImg = None


@app.route("/")
@app.route("/home")
def home():
    spotifyAuth = spotify.SERVER_URL + "/spotifyAuth"
    return render_template('home.html', spotifyAuth=spotifyAuth)


@app.route("/spotifyAuth")
def spotifyAuth():
    return redirect(spotify.get_auth_code())


@app.route("/spotifyCallback")
def spotifyCallback():
    return spotify.spotify_callback(request)


@app.route("/displayPlaylists/<access_token>")
def displayPlaylists(access_token):
    global at
    at = access_token
    session['access_token'] = access_token  # setting session data
    playlistTest = spotify.get_playlists(access_token)
    return render_template('spotifyDisplayPlaylistsTest.html', playlists=playlistTest, redirect_url=PLAYLIST_UPLOAD_URL)


@app.route("/uploadPlaylist/<playlist_id>/<playlist_img>/<playlist_name>")
def uploadPlaylist(playlist_id, playlist_img, playlist_name):
    global playlistImg
    playlistImg = playlist_img
    global uploadedPlaylist
    global at
    global IMAGE_BASE
    view_url = spotify.SERVER_URL + "/viewPlaylist/" + playlist_id
    uploadedPlaylist = spotify.uploadPlaylist(playlist_id, at, playlist_name=playlist_name)
    return render_template('spotifyUploadTest.html', view_url=view_url, img_base=IMAGE_BASE)


@app.route("/viewPlaylist/<playlist_id>/")
def viewPlaylist(playlist_id):
    global at
    global uploadedPlaylist
    global IMAGE_BASE
    playlistSongs = spotify.get_songs_in_playlist(playlist_id, at, uploadedPlaylist)
    analyse_url = spotify.SERVER_URL + "/analysePlaylist/" + playlist_id
    playlist_img = uploadedPlaylist.img
    return render_template('spotifyViewPlaylistTest.html', playlistSongs=playlistSongs,
                           analyse_url=analyse_url, playlist_img=playlist_img, img_base=IMAGE_BASE)


@app.route("/analysePlaylist/<playlist_id>")
def analysePlaylist(playlist_id):
    global at
    global uploadedPlaylist
    global IMAGE_BASE
    playlistName = uploadedPlaylist.name
    topArtists = spotify.getTopArtists(uploadedPlaylist)[:3]
    artistNames = list()
    for artist in topArtists:
        artistNames.append(artist)
    session['topArtists'] = artistNames
    topAlbums = spotify.getTopAlbums(uploadedPlaylist)[:3]
    check_url = spotify.SERVER_URL + "/checkAvailability"
    checkArtistVinylUrl = spotify.SERVER_URL + "/checkArtistVinyl"
    return render_template('spotifyAnalyseTest.html', topArtists=topArtists, topAlbums=topAlbums,
                           playlistName=playlistName, check_url=check_url, img_base=IMAGE_BASE, checkArtistVinylUrl=checkArtistVinylUrl)


@app.route("/checkAvailability/<album_img>")
def checkAvailability(album_img):
    shipping_url = spotify.SERVER_URL + "/enterShippingDetails"
    card_url = spotify.SERVER_URL + "/enterCardDetails"
    request_url = spotify.SERVER_URL + "/enterRequestDetails"
    global uploadedPlaylist
    global playlistImg
    global IMAGE_BASE
    album_img = album_img
    available = spotify.checkAlbumAvailability(album_img)
    return render_template('spotifyCheckAvailability.html', card_url=card_url,
                           shipping_url=shipping_url, playlist_img=album_img, img_base=IMAGE_BASE,
                           request_url=request_url, available=available)

@app.route("/checkArtistVinyl/<artistNum>")
def checkArtistVinyl(artistNum):
    artistName = session.get('topArtists')[int(artistNum)]['name']
    check_url = spotify.SERVER_URL + "/checkAvailability"
    global uploadedPlaylist
    global playlistImg
    global IMAGE_BASE
    availableVinyls = spotify.getAvailableVinylsByArtist(artistName)
    print("eaifhefa", availableVinyls)
    available = False
    if len(availableVinyls) > 0:
        available = True
    home_url = spotify.SERVER_URL + "/home"
    check_url = spotify.SERVER_URL + "/checkAvailability"
    return render_template('checkAvailableVinyls.html', check_url=check_url, home_url=home_url, artistName=artistName, available=available, availableVinyls=availableVinyls)


@app.route("/enterShippingDetails",methods=['GET','POST'])
def enterShippingDetails():
    form = ShippingDetails()
    if form.validate_on_submit():
        card_url = spotify.SERVER_URL + "/enterCardDetails"
        # DO YOU WANT TO REDIRECT USER HERE  IF THE INPUT IS VALID @Paul
    
     return render_template('enterShippingDetails.html', title='Shipping', form=form,
                           card_url=card_url)


@app.route("/enterCardDetails",methods=['GET','POST'])
def enterCardDetails():
    form = Card()
    if form.validate_on_submit():
        success_url = spotify.SERVER_URL + "/paymentSuccessful"
        # DO YOU WANT TO REDIRECT USER HERE  IF THE INPUT IS VALID @PAUL
        
    return render_template('enterCardDetails.html', title='Card', form=form,
                           success_url=success_url)


@app.route("/enterRequestDetails")
def enterRequestDetails():
    request_success_url = spotify.SERVER_URL + "/requestSuccessful"
    return render_template('enterRequestDetails.html',
                           request_success_url=request_success_url)


@app.route("/paymentSuccessful")
def paymentSuccessful():
    global at
    global IMAGE_BASE
    home_url = spotify.SERVER_URL + "/home"
    return render_template('shippingSuccess.html',
                           home_url=home_url, img_base=IMAGE_BASE)

@app.route("/requestSuccessful")
def requestSuccessful():
    global at
    global IMAGE_BASE
    home_url = spotify.SERVER_URL + "/home"
    return render_template('requestSuccess.html',
                           home_url=home_url, img_base=IMAGE_BASE)

# Hamza

@app.route("/register",methods = ['GET','POST'] )
def register():
    if current_user.is_authenticated:
        flash(f'{current_user.username}!, You are already logged In ', 'success')
        return redirect(url_for('index'))
    form = registrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username = form.username.data, email= form.email.data, password = hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'{form.username.data}!, Your are successfully Registered ','success')
        return  redirect(url_for('login')) # where index is the name of the function
    return render_template('register.html',title = 'Register', form = form)




@app.route("/login",methods = ['GET','POST'])
def login():

    if current_user.is_authenticated:
        flash(f'{current_user.username}!, You are already logged In ', 'success')
        return redirect(url_for('home'))
    form = loginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first() # return non if no user with the same email
        # if there is on it returns the first email
        if user and bcrypt.check_password_hash(user.password, form.password.data): # checking if the password provided #
            # is equal to one in the db
            # so now if the user exist and the password that they enter is valid with whats in the db
            # so we wan to log the user in we go
            login_user(user)
            next_page = request.args.get('next') # getting the route in the url) args is a dictionary


            # if the user has logged in successfully we redirect them to the homepage
            flash(f'{user.username}!, Welcome ', 'success')
            return redirect(next_page) if next_page else redirect(url_for('home'))
            # redirct to nextpage if it is not none else redirect to homepage

        else:
            flash('Invalid email or Password')
    return render_template('login.html',title = 'Login', form = form)


@app.route("/logout")
def logout():
    logout_user()
    flash('You are successfully Logged Out')
    return redirect(url_for('home'))






