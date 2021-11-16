from flask import Flask, redirect, render_template, request
from flask import Blueprint
from models.album import Album


# CLASSES
from models.artist import Artist

#  REPOSITORIES
import repositories.artist_repository as artist_repository
import repositories.album_repository as album_repository
from repositories.customer_item_repository import show_all

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


@album_blueprint.route('/album/new', methods=['GET'])
def show_form_new_album(
    error = None,
    input_artist = "",
    input_album = ""
    ):

    full_names_list = create_list_of_all_artists_full_names()
    
    return render_template(
        "/albums/new_album.html",
        error = error,
        input_artist = input_artist,
        input_album = input_album,
        full_names_list = full_names_list
        )
        


@album_blueprint.route('/album/new', methods=['POST'])
def get_form_new_album():

    error = None
    input_artist = request.form['artist']
    input_album = request.form['title_value']
    full_names_list = create_list_of_all_artists_full_names()
    name_exists = False
    for name in full_names_list:
        if name == input_artist:
            name_exists = True
            break

    if input_artist == "": error = "Artist is required"
    elif name_exists == False: error = "the artist typed doesn't exists. Please click on the button to create it"
    elif input_album == "": error = "Title is required"
    else:
        existing_albums = album_repository.show_all()
        for album in existing_albums:
            full_name = f'{"" if album.artist.first_name == None else f"{album.artist.first_name} "}{album.artist.last_name}'
            if album.title == input_album and full_name == input_artist:
                error = "This album, by this artist, already exists"
                break
            else:
                artist = artist_repository.select_1_artist_by_id(album.artist.id)

    if error == None:
        new_album = Album(artist, input_album)
        album_repository.add_album(new_album)
        
        return render_template("/index.html")

    else:
        return render_template(
            "/albums/new_album.html",
            error = error,
            input_artist = input_artist,
            input_album = input_album,
            full_names_list = full_names_list
            )