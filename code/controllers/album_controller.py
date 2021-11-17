from flask import Flask, redirect, render_template, request
from flask import Blueprint
from models.album import Album

# =================== CLASSES ====================
from models.artist import Artist

# ================= REPOSITORIES =================
import repositories.artist_repository as artist_repository
import repositories.album_repository as album_repository
from repositories.customer_item_repository import show_all

album_blueprint = Blueprint("album", __name__)

# ============== UTILITY FUNCTION ================
# creates ordered list of unique values for ALL artists FULL NAME
def create_list_of_all_artists_full_names():
    all_artists_unfiltered = artist_repository.show_all()
    artist_names= []
    for artist in all_artists_unfiltered:
        artist_full_name = f'{"" if artist.first_name == None else f"{artist.first_name} "}{artist.last_name}'
        artist_names.append(artist_full_name)
    artist_names = sorted(set(artist_names), key = lambda artist_names: artist_names)
    return artist_names



# ================================================
# ----------------- R O U T E S ------------------
# ================================================

# =================== DELETE =====================
@album_blueprint.route('/album/<album_id>', methods=['POST'])
def album_delete(album_id):
    album_repository.delete_1_album_by_id(album_id)
    return redirect("/items/all/all")

@album_blueprint.route('/album/<album_id>', methods=['GET'])
def confirm_album_delete(album_id):
    album=album_repository.select_1_album_by_id(album_id)
    return render_template("/albums/delete_album.html", album = album)



# ================== ADD ========================

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
                artist = artist_repository.select_artist_by_full_name(input_artist)

    if error == None:
        new_album = Album(artist, input_album)
        album_repository.add_album(new_album)
        return redirect("/item/new")

    else:
        return render_template(
            "/albums/new_album.html",
            error = error,
            input_artist = input_artist,
            input_album = input_album,
            full_names_list = full_names_list
            )