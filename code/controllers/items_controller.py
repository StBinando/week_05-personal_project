from flask import Flask, redirect, render_template, request
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
import repositories.customer_item_repository as customer_item_repository



# INVENTORY
@app.route('/inventory/<selection>/<filter>')
# "selecetion" is based on the initails buttons
# "filter" is based on the availability filter
def inventory(selection = "all_albums", filter = "all"):

    # ********* SEARCH BOX ***********
    # ********************************
    # creates a list of unique album titles for search box that overrides filter and selection
    all_artists_unfiltered = artist_repository.show_all()
    artist_names= []
    for artist in all_artists_unfiltered:
        artist_first_name = ("" if artist.first_name == None else f"{artist.first_name} ")
        artist_full_name = f'{"" if artist.first_name == None else f"{artist.first_name} "}{artist.last_name}'
        artist_names.append(artist_full_name)
    artist_names = sorted(set(artist_names), key = lambda artist_names: artist_names)

    all_items_unfiltered =item_repository.show_all()
    albums = []
    for item in all_items_unfiltered:
        album_title = item.album.title
        albums.append(album_title)
    album_titles = sorted(set(albums), key = lambda albums: albums)


    # ********* ARTISTS AND ITEMS ***********
    # ***************************************
    # to speed up the loading of the page, it checks first if the there are no filters
    # it simply returns an ordered list of all items and all initials (of artists) in the database
    # so we can use the same result used for the search box
    if selection == "all_albums" and filter == "all":
        all_artists_unsorted = all_artists_unfiltered
        all_items_unsorted = all_items_unfiltered
    # otherwise it returns only the items both filtered and selected
    else:
        all_artists_unsorted = artist_repository.select_by_filter_and_selection(filter, selection)
        all_items_unsorted = item_repository.select_by_filter_and_selection(filter, selection)
    
    # sorts out the list of artists only by name,
    # and the list of items by artist's name and then by title
    all_artists_sorted = sorted(all_artists_unsorted, key = lambda artists: artists.last_name) 
    all_items_sorted = sorted(all_items_unsorted, key=lambda item: (item.album.artist.last_name, item.album.title, item.support))
        

    # ********* INITIALS ***********
    # ******************************
    # the initials are for the buttons; they are filtered by availability, but not by selection
    artists_for_initials_unsorted = artist_repository.select_filtered(filter)
    artists_for_initials_sorted = sorted(artists_for_initials_unsorted, key = lambda artists: artists.last_name)
    initials = []
    for artist in artists_for_initials_sorted:
        initials.append(artist.last_name[0])
    # create a SET of initialswith unique elements and sort them alphabetically
    initials = sorted(set(initials))
   

    # ********* PRE-BOOKED ***********
    # ********************************
    # returns all records in the database related to items displayed
    # according to filters applied
    customers_items_id=[]
    all_customers_items = customer_item_repository.show_all()
    for item in all_items_sorted:
        for ci in all_customers_items:
            if ci.item.id == item.id:
                customers_items_id.append(ci.item.id)
    customers_items_id = Counter(customers_items_id)
    
  
    return render_template("inventory.html",
    artist_names = artist_names, # ordered list of artist names (str) for serach box - unfiltered
    albums = album_titles, # ordered list of album titles (str) for serach box - unfiltered
    all_artists = all_artists_sorted, # ordered list of all artists (obj) - filtered
    all_items = all_items_sorted, # ordered list of all items (obj) - filtered
    customers_items = customers_items_id, # unordered list of the number of customers_items for filtered items
    initials = initials, # ordered list of artists.last_name first letter (char) - filtered by availability only
    filter = filter, # value for availability selected
    selection = selection # value for initial selected
    )