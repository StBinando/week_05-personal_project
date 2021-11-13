from flask import Flask, redirect, render_template, request
from app import app

# CLASSES
from models.item import Item
from models.album import Album
from models.artist import Artist

#  REPOSITORIES
import repositories.item_repository as item_repository
import repositories.artist_repository as artist_repository



# INVENTORY
@app.route('/inventory/<selection>')
def inventory(selection = "all_albums", filter = "all"):

    all_artists_unsorted = artist_repository.show_all()
    all_artists_sorted = sorted(all_artists_unsorted, key = lambda artists: artists.last_name)  
    all_items_unsorted = item_repository.show_all()

    initials = []
    for artist in all_artists_sorted:
        initials.append(artist.last_name[0])
    initials = sorted(set(initials))

    selected_artists = []
    if selection == "all_albums":
        selected_artists = all_artists_sorted
    else:
        for artist in all_artists_sorted:
            if artist.last_name[0] == selection:
                selected_artists.append(artist)

    all_items_sorted = sorted(all_items_unsorted, key=lambda item: (item.album.artist.last_name, item.album.title, item.support))

    return render_template("inventory.html", all_items = all_items_sorted, all_artists = selected_artists, initials = initials, selection = selection)