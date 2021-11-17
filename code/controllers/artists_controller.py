from flask import Flask, redirect, render_template, request
from flask import Blueprint

from models.artist import Artist


#  REPOSITORIES
import repositories.artist_repository as artist_repository
import repositories.album_repository as album_repository

artists_blueprint = Blueprint("artists", __name__)


# ================================================
# ----------------- R O U T E S ------------------
# ================================================


@artists_blueprint.route('/artist/<artist_id>', methods=['POST'])
def artist_delete(artist_id):
    artist_repository.delete_1_artist_by_id(artist_id)
    return redirect("/items/all/all")


@artists_blueprint.route('/artist/<artist_id>', methods=['GET'])
def confirm_artist_delete(artist_id):
    artist=artist_repository.select_1_artist_by_id(artist_id)
    return render_template("/artists/delete_artist.html", artist = artist)


@artists_blueprint.route('/artist/new', methods=['GET'])
def show_form_new_artist(
    error = None,
    input_artist = None
    ):

    return render_template(
        "/artists/new_artist.html",
        error = error,
        input_artist = input_artist
        )

@artists_blueprint.route('/artist/new', methods=['POST'])
def get_form_new_artist():
    
    error = None
    input_artist = []
    input_artist.append(request.form['first_name_value'])
    input_artist.append(request.form['last_name_value'])
    if input_artist[1] == "":
        error = "Last name is required"
    else:
        existing_artists = artist_repository.show_all()
        for artist in existing_artists:
            if artist.first_name == input_artist[0] and artist.last_name == input_artist[1]:
                error = "This artist already exists"

    if error == None:
        new_artist = Artist(input_artist[1], input_artist[0])
        artist_repository.add_artist(new_artist)
        return redirect("/item/new")
    else:
        return render_template(
            "/artists/new_artist.html",
            error = error,
            input_artist = input_artist,
            )
