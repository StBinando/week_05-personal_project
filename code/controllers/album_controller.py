from flask import Flask, redirect, render_template, request
from flask import Blueprint
from models.album import Album


# CLASSES
from models.artist import Artist

#  REPOSITORIES
import repositories.artist_repository as artist_repository
import repositories.album_repository as album_repository

album_blueprint = Blueprint("album", __name__)

# --- UTILITY FUNCTION --- creates ordered list of unique values for ALL artists FULL NAME
def create_list_of_all_artists_full_names():
    all_artists_unfiltered = artist_repository.show_all()
    artist_names= []
    for artist in all_artists_unfiltered:
        artist_full_name = f'{"" if artist.first_name == None else f"{artist.first_name} "}{artist.last_name}'
        artist_names.append(artist_full_name)
    artist_names = sorted(set(artist_names), key = lambda artist_names: artist_names)
    return artist_names

# --- UTILITY FUNCTION --- creates ordered list of unique values for ALL album titles
# def create_list_of_all_album_titles():
#     all_albums =album_repository.show_all()
#     albums = []
#     for album in all_albums:
#         album_title = album.title
#         albums.append(album_title)
#     album_titles = sorted(set(albums), key = lambda albums: albums)
#     return album_titles

@album_blueprint.route('/album/new', methods=['GET'])
def show_form_new_album(
    back = None,
    error = None,
    input_new_artist = None,
    input_new_album = None,
    input_new_item = None):

    full_names_list = create_list_of_all_artists_full_names()
    
    return render_template(
        "/albums/new_album.html",
        back = back,
        error = error,
        input_new_artist = input_new_artist,
        input_new_album = input_new_album,
        input_new_item = input_new_item,
        full_names_list = full_names_list
        )
        


@album_blueprint.route('/album/new', methods=['POST'])
def get_form_new_album(
    back = None,
    error = None,
    input_new_artist = None,
    input_new_album = None,
    input_new_item = None
    ):

    error = None
    msg = None
    input_artist = request.form['artist']
    input_new_album = request.form['title_value']
    if input_artist == "":
        error = "Artist is required"
    elif input_new_album == "":
        error = "Title is required"
    else:
        existing_albums = album_repository.show_all()
        for album in existing_albums:
            full_name = f'{"" if album.artist.first_name == None else f"{album.artist.first_name} "}{album.artist.last_name}'
            if album.title == input_new_album and full_name == input_artist:
                error = "This album, by this artist, already exists"
                msg = f"input artist: {input_artist} --- full name: {full_name}"
            else:
                artist = artist_repository.select_1_artist_by_id(album.artist.id)

    if error == None:
        new_album = Album(artist, input_new_album)
        msg = (album_repository.add_album(new_album)).title
        
        return render_template("/index.html", msg = msg)
    else:
        full_names_list = create_list_of_all_artists_full_names()

        return render_template(
            "/albums/new_album.html",
            back = back,
            error = error,
            input_new_artist = input_new_artist,
            input_new_album = input_new_album,
            input_new_item = input_new_item,
            full_names_list = full_names_list
            )