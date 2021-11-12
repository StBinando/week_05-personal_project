from db.run_sql import run_sql
from models.artist import Artist
from models.album import Album
from models.item import Item

import repositories.artist_repository as artist_repository
import repositories.album_repository as album_repository


def add_item(item):
    sql = "INSERT INTO items (album_id, support, cost, selling_price, in_stock, ordered) VALUES (%s, %s, %s, %s, %s, %s) RETURNING *"
    values = [item.album.id, item.support, item.cost, item.selling_price, item.in_stock, item.ordered]
    results = run_sql(sql, values)
    id = results[0]['id']
    item.id = id
    return item

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

    