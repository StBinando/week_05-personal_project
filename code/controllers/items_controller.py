from types import MethodType
from flask import Flask, redirect, render_template, request
from flask import Blueprint
from collections import Counter
from models.item import Item

#  REPOSITORIES
import repositories.item_repository as item_repository
import repositories.artist_repository as artist_repository
import repositories.album_repository as album_repository
import repositories.customer_item_repository as customer_item_repository

items_blueprint = Blueprint("items", __name__)


# --- UTILITY FUNCTION ---
# creates ordered list of unique values for ALL artists FULL NAME
def create_list_of_all_artists_full_names():
    all_artists_unfiltered = artist_repository.show_all()
    artist_names= []
    for artist in all_artists_unfiltered:
        artist_full_name = f'{"" if artist.first_name == None else f"{artist.first_name} "}{artist.last_name}'
        artist_names.append(artist_full_name)
    artist_names = sorted(set(artist_names), key = lambda artist_names: artist_names)
    return artist_names

def create_list_of_all_artists_full_names_for_search():
    all_artists_unfiltered = artist_repository.show_all()
    all_items = item_repository.show_all()
    artist_names= []
    for artist in all_artists_unfiltered:
        for item in all_items:
            if artist.id == item.album.artist.id:
                artist_full_name = f'{"" if artist.first_name == None else f"{artist.first_name} "}{artist.last_name}'
                break
        artist_names.append(artist_full_name)
    artist_names = sorted(set(artist_names), key = lambda artist_names: artist_names)
    return artist_names

# --- UTILITY FUNCTION ---
# creates ordered list of unique values for ALL album titles
def create_list_of_all_album_titles():
    all_albums =album_repository.show_all()
    albums = []
    for album in all_albums:
        album_title = album.title
        albums.append(album_title)
    album_titles = sorted(set(albums), key = lambda albums: albums)
    return album_titles

def create_list_of_all_album_titles_for_search():
    all_albums =album_repository.show_all()
    all_items = item_repository.show_all()

    albums = []
    for album in all_albums:
        for item in all_items:
            if album.id == item.album.id:
                album_title = album.title
                break
        albums.append(album_title)
    album_titles = sorted(set(albums), key = lambda albums: albums)
    return album_titles



# ================================================
# ----------------- R O U T E S ------------------
# ================================================

# ===================== EDIT =====================
@items_blueprint.route('/item/<item_id>/edit', methods=['GET'])
def edit_item(item_id):
    item = item_repository.select_1_item_by_id(item_id)
    return render_template("/items/edit.html", item=item)

@items_blueprint.route('/item/<item_id>/edit', methods=['POST'])
def get_form_edit_item(item_id):
    # error = None
    item = item_repository.select_1_item_by_id(item_id)
    # input_artist = request.form['artist']
    # input_album = request.form['album']
    item.support = request.form['support']
    item.cost = request.form['cost']
    item.selling_price = request.form['price']
    item.in_stock = request.form['in_stock']
    item.ordered = request.form['ordered']

    # artist = artist_repository.select_artist_by_full_name(input_artist).id
    # album = album_repository.select_by_title(input_album).id

    item_repository.update_item(item)
    return redirect(f'/items/search_result(t) {item.album.title}')
    # return redirect('/items/all/all')



# =================== DELETE =====================
@items_blueprint.route('/item/<item_id>')
def delete_item(item_id):
    selected_item = item_repository.select_1_item_by_id(item_id)
    all_items = item_repository.show_all()
    count_items_for_album = 0
    count_items_for_artist = 0
    for item in all_items:
        if item.album.artist.id == selected_item.album.artist.id:
            count_items_for_artist +=1
            if item.album.id == selected_item.album.id:
                count_items_for_album +=  1

    # last item for the artist - artist will be deleted
    if count_items_for_artist == 1:
        artist_id = selected_item.album.artist.id
        return redirect(f'/artist/{artist_id}')

    # last item for the artist - album will be deleted
    elif count_items_for_album == 1:
        album_id = selected_item.album.id
        return redirect(f'/album/{album_id}')
    
    item_repository.delete_1_item_by_id(item_id)
    return redirect('/items/all/all')




    # full_names_list = create_list_of_all_artists_full_names()
    # titles_list = create_list_of_all_album_titles()

    pass

    return render_template(
        "/items/edit.html",
        # error = error,
        # input_artist = input_artist,
        # input_album = input_album,
        # input_support = input_support,
        # input_cost = input_cost,
        # input_price = input_price,
        # input_in_stock = input_in_stock,
        # input_ordered = input_ordered,
        # artists = full_names_list,
        # albums = titles_list
        )

# ===================== ADD ======================
@items_blueprint.route('/item/new', methods=['GET'])
def show_form_new_item(
    error = None,
    input_artist = "",
    input_album = "",
    input_support = "",
    input_cost = 0.00,
    input_price = 0.00,
    input_in_stock = 0,
    input_ordered = 0,
    ):

    full_names_list = create_list_of_all_artists_full_names()
    titles_list = create_list_of_all_album_titles()

    return render_template(
        "/items/new_item.html",
        error = error,
        input_artist = input_artist,
        input_album = input_album,
        input_support = input_support,
        input_cost = input_cost,
        input_price = input_price,
        input_in_stock = input_in_stock,
        input_ordered = input_ordered,
        artists = full_names_list,
        albums = titles_list
        )

@items_blueprint.route('/item/new', methods=['POST'])
def get_form_new_item():

    error = None
    input_artist = request.form['artist']
    input_album = request.form['album']
    input_support = request.form['support']
    input_cost = request.form['cost']
    input_price = request.form['price']
    input_in_stock = request.form['in_stock']
    input_ordered = request.form['ordered']

    full_names_list = create_list_of_all_artists_full_names()
    name_exists = False
    for name in full_names_list:
        if name == input_artist:
            name_exists = True
            break

    titles_list = create_list_of_all_album_titles()
    title_exists = False
    for title in titles_list:
        if title == input_album[4:]:
            title_exists = True
            break

    artist_album_exists = False
    albums_list = album_repository.show_all()
    for album in albums_list:
        artist_full_name = f'{"" if album.artist.first_name == None else f"{album.artist.first_name} "}{album.artist.last_name}'
        if artist_full_name == input_artist:
            if album.title == input_album[4:]:
                artist_album_exists = album
                break

    if input_artist == "": error = "Artist is required"
    elif name_exists == False: error = "the artist typed doesn't exists. Please click on the button to create it"
    elif input_album == "": error = "Title is required"
    elif title_exists == False: error = "the album typed doesn't exists. Please click on the button to create it"
    elif artist_album_exists == False: error = "This album doesn't exists with this artist. Please check the combination of artist and album, or create a new one"
        
    elif input_support == "": error = "Support is required"
    elif input_cost == "": error = "Cost is required"
    elif input_price == "": error = "Selling price is required"
    else:
        existing_items = item_repository.show_all()
        for item in existing_items:
            if item.album.id == artist_album_exists.id and item.support == input_support:
                error = "This album, by this artist, on this support, already exists"

    if error == None:
        new_item = Item(album, input_support, input_cost, input_price, input_in_stock, input_ordered)
        item_repository.add_item(new_item)
        error = f"displaying all items for album {new_item.album.title}"
        return redirect(f"/items/search_result(t) {new_item.album.title}")
        # return redirect("/items/all/all")

    else:
        full_names_list = create_list_of_all_artists_full_names()
        titles_list = create_list_of_all_album_titles()


        return render_template(
            "/items/new_item.html",
            error = error,
            input_artist = input_artist,
            input_album = input_album,
            input_support = input_support,
            input_cost = input_cost,
            input_price = input_price,
            input_in_stock = input_in_stock,
            input_ordered = input_ordered,
            artists = full_names_list,
            albums = titles_list
            )



# ==================== SEARCH =====================
@items_blueprint.route('/items/search', methods=['POST'])
def get_search():
    result = request.form['search']
    full_names_list = create_list_of_all_artists_full_names_for_search()
    name_exists = False
    for name in full_names_list:
        if name == result:
            name_exists = True
            break

    albums_list = create_list_of_all_album_titles_for_search()
    album_exists =False
    for album in albums_list:
        if album == result[4:]:
            album_exists = True
            break
    if name_exists or album_exists:
        return redirect(f"/items/search_result{result}")
    else:
        return redirect('/items/all/all')


@items_blueprint.route('/items/search_result<result>', methods=['GET'])
def show_search(result):

    if result[0:3] == "(t)":
        choice = "album"
        choice_string = result[0:3]
        title = result[4:]
        album = album_repository.select_by_title(title)[0]
        items = item_repository.select_items_by_album_id(album.id)
        artist_found = artist_repository.select_1_artist_by_id(album.artist.id)
    else:
        choice = "artist"
        choice_string = result
        artist_found = artist_repository.select_artist_by_full_name(result)
        items = item_repository.select_items_by_artist_id(artist_found.id)
    items = sorted(items, key=lambda item: (item.album.title, item.support))


    artist_names = create_list_of_all_artists_full_names_for_search()
    album_titles = create_list_of_all_album_titles_for_search()
    all_artists_unfiltered = artist_repository.show_all()

    initials = []
    for artist in all_artists_unfiltered:
        initials.append(artist.last_name[0])
        initials = sorted(set(initials))


    pre_booked_items = []
    all_pre_booked_items = customer_item_repository.show_all()        
    for item in items:
        for pbi in all_pre_booked_items:
            if pbi.item.id == item.id:
                pre_booked_items.append(pbi.item.id)
    pre_booked_items = Counter(pre_booked_items)

    # if choice == "artist":
    #     error = f"displaying items by {choice_string}"
    # else:
    #     full_name = ("" if artist.first_name == None else f"{artist.first_name} ")+(artist.last_name)
    #     error = f"displaying items for {choice_string} by {full_name}"
    return render_template(
        "items/inventory.html",
        filter ="all",
        selection = artist_found.last_name[0],
        error = None,
        artist_names = artist_names,
        album_titles = album_titles,
        initials = initials,
        artists_filtered = [artist_found],
        items = items,
        pre_booked_items = pre_booked_items
        )


# ============== FILTER / INITIALS ==================
# returns a list of items to display
# based on "filter" (availability/genre/label) ONLY, doesn't use "selection" (initials)
# @items_blueprint.route('/items?filter=<filter>&selection=<selection', methods=['GET'])
@items_blueprint.route('/items/<filter>/<selection>', methods=['GET'])
def inventory_selected(filter = "all", selection = "all"):

    # sets initial error message to None
    error = None

    artist_names = create_list_of_all_artists_full_names_for_search()
    album_titles = create_list_of_all_album_titles_for_search()

    # if filter is "ALL"...
    if filter == "all":
        # ...ant the "selection" (initials) is "ALL"
        # it returns a list of ALL Item objects, unfiltered
        if selection == "all":
            results = item_repository.show_all()
        # otherwise it returns a list of ITEM OBJECTS WHERE THE
        # first letter of the argument item > album > artist > last_name
        # matches the selection
        else:
            results = item_repository.select_by_selection(selection)

        # in both cases, then it checks if the list is empty and
        # in that case returns an error message
        if len(results) == 0:
            error = "The inventory is empty!"

    # if filter is ANYTHING ELSE returns a list of ALL Item objects
    # based on criteria set on item_repository     
    else:
        results_filtered = item_repository.select_filtered(filter)
        
        # then it checks if an initial has been selected
        if selection == "all":
            results = results_filtered
        
        # and in that case goes through the list already filtered
        # to narrow it down to only the items that match the criteria
        # for the initial as above
        else:
            results = []
            for rf in results_filtered:
                if rf.album.artist.last_name[0] == selection:
                    results.append(rf)
            pass
        if len(results) == 0:
            error = f"There are no {filter} items to display"
    

    initials = []
    artists_filtered = []
    items_sorted = []
    pre_booked_items = []

    # if the list is not empty
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
        "/items/inventory.html",
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

