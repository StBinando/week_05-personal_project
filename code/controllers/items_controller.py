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


#                           INVENTORY FILTER
# returns a list of items to display
# based on "filter" (availability/genre/label) ONLY, doesn't use "selection" (initials)
@app.route('/inventory/<filter>')
def inventory(filter = "all"):

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
        results = item_repository.show_all()
        if len(results) == 0:
            error = "The inventory is empty!"
    # if filter is ANYTHING ELSE returns a list of ALL Item objects
    # based on criteria set on item_repository     
    else:
        results = item_repository.select_filtered(filter)
        if len(results) == 0:
            error = f"There are no {filter} items to display"
    
    # if the list is not empty
    if error == None:
        all_items_filtered = results
        # checks the number of pre-booked items in customers_items table
        # that match items in the filtered list 
        all_pre_booked_items = customer_item_repository.show_all()
        pre_booked_items=[]
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
        initials = []
        for artist in artists_filtered:
            initials.append(artist.last_name[0])
        # sorts both initials and artists lists
        initials = sorted(set(initials))
        artists_filtered = sorted(artists_filtered, key=lambda artist: (artist.last_name, artist.first_name))

    return render_template(
        "inventory.html",
        filter = filter, # value for availability selected (str)
        selection = "all", # value for initial selected (str)
        artist_names = artist_names, # ordered list of artist names (str) for serach box - unfiltered
        album_titles = album_titles, # ordered list of album titles (str) for serach box - unfiltered
        initials = initials, # ordered list of artists.last_name first letter (char) - filtered by availability only
        artists_filtered = artists_filtered, # ordered list of all artists (obj) - filtered
        items = items_sorted, # ordered list of all items (obj) - filtered
        pre_booked_items = pre_booked_items # unordered list of the number of customers_items for filtered items
    )


# ================================================================================================
# ================================================================================================
# ================================================================================================
# ================================================================================================
# ================================================================================================
# ================================================================================================
# ================================================================================================

#                           INVENTORY FILTER/INITIALS
#           COMMENT
#       returns a list of items to display
#       based on "filter" (availability/genre/label) ONLY, doesn't use "selection" (initials)

#           PSEUDOCODE
# #     1 -   creates list of all artists FULL NAME (unique values - sorted)
#           for search box that overrides filter

#     2 -   creates list of all album titles (unique values - sorted)
#           for search box that overrides filter

#     3 -   if filter is pre-booked -> 
#           -   if list is empy ->
#                   - creates error message
#           -   else ->
#                   - go through customers_items table first
#                   - create a list of unique item_id in that table
#                     with number of pre-book for each id
#           -   uses the list created to create and return
#               restricted list of items with the same item_id in the list
#       -   else if filter is all -> 
#           -   if list is empy ->
#                   - creates error message
#           -   else ->
#                   - returns all items
#       -   else ->
#           -   if list is empy ->
#                   - creates error message
#           -   else ->
#               -   returns restricted list of items based on filter matching
#                   column name in table items with values > 0

#     4 -   if error message is empty ->
#           -   order resulting list
#           -   creates list of INITIALS of artists LAST NAME (unique values - sorted)
#               based on restricted item list

#     5 -   returns:
#           -   variable selection as selected
#           -   list of ALL artists FULL NAME
#           -   list of ALL albums TITLES
#           -   variable filter = "all"
#           -   list of filtered INITIALS
#           -   list of pre-booked ids and numbers
#           -   list of filtered items
#           -   error message






