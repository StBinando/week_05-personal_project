from db.run_sql import run_sql
from models.artist import Artist
from models.album import Album
from models.item import Item

import repositories.artist_repository as artist_repository
import repositories.album_repository as album_repository
import repositories.customer_item_repository as customer_item_repository


def add_item(item):
    sql = "INSERT INTO items (album_id, support, cost, selling_price, in_stock, ordered) VALUES (%s, %s, %s, %s, %s, %s) RETURNING *"
    values = [item.album.id, item.support, item.cost, item.selling_price, item.in_stock, item.ordered]
    results = run_sql(sql, values)
    id = results[0]['id']
    item.id = id
    return item

def update_item(item):
    sql = "UPDATE items SET (album_id, support, cost, selling_price, in_stock, ordered) = (%s, %s, %s, %s, %s, %s) WHERE id = %s"
    values = [item.album.id, item.support, item.cost, item.selling_price, item.in_stock, item.ordered, item.id]
    run_sql(sql, values)

def show_all():
    items = []
    sql = "SELECT * FROM items"
    results = run_sql(sql)
    for row in results:
        album = album_repository.select_1_album_by_id(row['album_id'])
        item = Item(album, row['support'], row['cost'], row['selling_price'], row['in_stock'], row['ordered'], row['id'])
        items.append(item)
    return items

def select_1_item_by_id(id):
    sql = "SELECT * FROM items where id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    album = album_repository.select_1_album_by_id(result['album_id'])
    item = Item(album, result['support'], result['cost'], result['selling_price'], result['in_stock'], result['ordered'], result['id'])
    return item

def delete_1_item_by_id(id):
    sql = "DELETE FROM items WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def select_by_selection(selection = "all"):
    if selection == "all":
        sql = "SELECT * FROM items"
        values = None
    else:
        albums_id = []
        albums = album_repository.select_by_selection(selection)
        for album in albums:
            albums_id.append(album.id)
        sql = "SELECT * FROM items where album_id IN %s"
        values = [tuple(albums_id)]
    items = []
    results = run_sql(sql, values)
    for row in results:
        album = album_repository.select_1_album_by_id(row['album_id'])
        item = Item(album, row['support'], row['cost'], row['selling_price'], row['in_stock'], row['ordered'], row['id'])
        items.append(item)
    return items

def select_filtered(filter = "all"):
    if filter == "pre_booked":
        results = customer_item_repository.show_all()
        item_ids = []
        for row in results:
            item_ids.append(row.item.id)
        item_ids = set(item_ids)
        items = []
        for id in item_ids:
            item = select_1_item_by_id(id)
            items.append(item)
    else:
        if filter == "all":
            sql = "SELECT * FROM items"
        else:
            if filter == "in_stock" or filter == "ordered":
                sql = f"SELECT * FROM items where {filter} >0"
            else: # not active until GENRE is added - i should be added to albums, though...
                sql = f"SELECT * FROM items where genre = {filter}"
        results = run_sql(sql)
        items = []
        for row in results:
            album = album_repository.select_1_album_by_id(row['album_id'])
            item = Item(album, row['support'], row['cost'], row['selling_price'], row['in_stock'], row['ordered'], row['id'])
            items.append(item)
    return items

def select_by_filter_and_selection(filter = "all", selection = "all_albums"):
    filtered = select_filtered(filter)
    selected = select_by_selection(selection)
    items_id =[]
    for s in selected:
        for f in filtered:
            if s.id == f.id:
                items_id.append(s.id)
    items_id = set(items_id)
    items =[]
    for id in items_id:
        items.append(select_1_item_by_id(id))
    return items

def select_items_by_artist_id(artist_id):
    artist_items = []
    all_items = show_all()
    for i in all_items:
        if i.album.artist.id == artist_id:
            artist_items.append(i)
    return artist_items

def select_items_by_album_id(album_id):
    album_items = []
    all_items = show_all()
    for i in all_items:
        if i.album.id == album_id:
            album_items.append(i)
    return album_items


