from flask import Flask, redirect, render_template, request
from jinja2.environment import TemplateStream
from app import app
from collections import Counter

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


@app.route('/inventory/search', methods=['POST'])
def get_search():
    result = request.form['search']
    return redirect(f"/inventory/search_result{result}")


@app.route('/inventory/search_result<result>', methods=['GET'])
def show_search(result):

    if result[0:3] == "(t)":
        title = result[4:]
        album = album_repository.select_by_title(title)[0]
        items = item_repository.select_items_by_album_id(album.id)

    else:
        artist = artist_repository.select_artist_by_full_name(result)
        items = item_repository.select_items_by_artist_id(artist.id)
    return render_template("empty.html", items = items)




#                           INVENTORY FILTER/INITIAL
# returns a list of items to display
# based on "filter" (availability/genre/label) ONLY, doesn't use "selection" (initials)
@app.route('/inventory/<filter>/<selection>', methods=['GET'])
def inventory_selected(filter = "all", selection = "all"):

    # sets initial error message to None
    error = None

    # creates ordered list of unique values for ALL artists FULL NAME
    all_artists_unfiltered = artist_repository.show_all()
    artist_names= []
    for artist in all_artists_unfiltered:
        artist_full_name = f'{"" if artist.first_name == None else f"{artist.first_name} "}{artist.last_name}'
        artist_names.append(artist_full_name)
    artist_names = sorted(set(artist_names), key = lambda artist_names: artist_names)

    # creates ordered list of unique values for ALL aalbum titles
    all_items_unfiltered =item_repository.show_all()
    albums = []
    for item in all_items_unfiltered:
        album_title = item.album.title
        albums.append(album_title)
    album_titles = sorted(set(albums), key = lambda albums: albums)




    # if filter is "ALL" returns a list of ALL Item objects, unfiltered
    if filter == "all":
        if selection == "all":
            results = item_repository.show_all()
        else:
            results = item_repository.select_by_selection(selection)
        if len(results) == 0:
            error = "The inventory is empty!"
    
    
    
    # if filter is ANYTHING ELSE returns a list of ALL Item objects
    # based on criteria set on item_repository     
    else:
        results_filtered = item_repository.select_filtered(filter)
        if selection == "all":
            results = results_filtered
        else:
            results = []
            for rf in results_filtered:
                if rf.album.artist.last_name[0] == selection:
                    results.append(rf)
            pass
        if len(results) == 0:
            error = f"There are no {filter} items to display"
    
    # if the list is not empty
    initials = []
    artists_filtered = []
    items_sorted = []
    pre_booked_items = []
    if error == None:
        all_items_filtered = results
        # checks the number of pre-booked items in customers_items table
        # that match items in the filtered list 
        all_pre_booked_items = customer_item_repository.show_all()
        
        for item in all_items_filtered:
            for pbi in all_pre_booked_items:
                if pbi.item.id == item.id:
                    pre_booked_items.append(pbi.item.id)
        pre_booked_items = Counter(pre_booked_items)
        # sorts the list of item OBJECTS by album title, then support
        items_sorted = sorted(all_items_filtered, key=lambda item: (item.album.title, item.support))
        
        
        
        # creates a list of unique artists OBJECTS applying the same filter
        artists_filtered = artist_repository.select_filtered(filter)

        # creates a list of unique initials based on filtered artists
        for artist in artists_filtered:
            initials.append(artist.last_name[0])

        
        # sorts both initials and artists lists
        initials = sorted(set(initials))
        artists_filtered = sorted(artists_filtered, key=lambda artist: (artist.last_name, artist.first_name))

    return render_template(
        "inventory.html",
        filter = filter, # value for availability selected (str)
        selection = selection, # value for initial selected (str)
        error = error, # error message returned if the list is empty
        artist_names = artist_names, # ordered list of artist names (str) for serach box - unfiltered
        album_titles = album_titles, # ordered list of album titles (str) for serach box - unfiltered
        initials = initials, # ordered list of artists.last_name first letter (char) - filtered by availability only
        artists_filtered = artists_filtered, # ordered list of all artists (obj) - filtered
        items = items_sorted, # ordered list of all items (obj) - filtered
        pre_booked_items = pre_booked_items # unordered list of the number of customers_items for filtered items
    )

