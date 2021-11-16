from flask import Flask, redirect, render_template, request
from flask import Blueprint
from jinja2.environment import TemplateStream
from app import app
# from collections import Counter

# CLASSES
from models.item import Item
from models.album import Album
from models.artist import Artist
from models.customer_item import CustomerItem

#  REPOSITORIES
import repositories.item_repository as item_repository
import repositories.artist_repository as artist_repository
import repositories.album_repository as album_repository
import repositories.customer_item_repository as customer_item_repository

artists_blueprint = Blueprint("artists", __name__)

@artists_blueprint.route('/artist/new', methods=['GET'])
def show_form_new_artist(back = None, error = None, input_new_artist = None, input_new_album = None, input_new_item = None):
    input_new_album = input_new_album
    input_new_item = input_new_item
    error = error
    input_new_artist = input_new_artist
    if error == None:
        # show (empty?) fields to be filled in
        pass
    else:
        # show ERROR MESSAGE: artist already exists check again
        pass
    return render_template(
        "/artists/new_artist.html",
        back = back,
        error = error,
        input_new_artist = input_new_artist,
        input_new_album = input_new_album,
        input_new_item = input_new_item
        )
        


@artists_blueprint.route('/artist/new', methods=['POST'])
def get_form_new_artist(back = None, error = None, input_new_artist = None, input_new_album = None, input_new_item = None):
    
    # back = back
    # input_new_album = input_new_album
    # input_new_item = input_new_item
    error = None
    input_new_artist = []
    input_new_artist.append(request.form['first_name_value'])
    input_new_artist.append(request.form['last_name_value'])
    if input_new_artist[1] == "":
        error = "Last name is required"
    else:
        existing_artists = artist_repository.show_all()
        for artist in existing_artists:
            if artist.first_name == input_new_artist[0] and artist.last_name == input_new_artist[1]:
                error = "This artist already exists"

    if error == None:
        new_artist = Artist(input_new_artist[1], input_new_artist[0])
        artist_repository.add_artist(new_artist)
        return redirect("/")
    else:
        return render_template(
            "/artists/new_artist.html",
            back = back,
            error = error,
            input_new_artist = input_new_artist,
            input_new_album = input_new_album,
            input_new_item = input_new_item
            )
    # return redirect("/")