from db.run_sql import run_sql
from models.customer_item import CustomerItem
from models.customer import Customer
from models.item import Item

import repositories.customer_repository as customer_repository
import repositories.item_repository as item_repository

def add_customer_item(customer_item):
    sql = "INSERT INTO customers_items (customer_id, item_id) VALUES (%s, %s) RETURNING *"
    values = [customer_item.customer.id, customer_item.item.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    customer_item.id = id
    return customer_item

def show_all():
    customers_items = []
    sql = "SELECT * FROM customers_items"
    results = run_sql(sql)
    for row in results:
        customer = customer_repository.select_1_customer_by_id(row['customer_id'])
        item = item_repository.select_1_item_by_id(row['item_id'])
        customer_item = CustomerItem(customer, item)
        customers_items.append(customer_item)
    return customers_items

def select_1_customer_item_by_id(id):
    sql = "SELECT * FROM customers_items WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    customer = customer_repository.select_1_customer_by_id(result['customer_id'])
    item = item_repository.select_1_item_by_id(result['item_id'])
    customer_item = CustomerItem(customer, item)
    return customer_item


def select_all_customer_item_by_customer_id(customer_id):
    customers_items = []
    sql = "SELECT * FROM customers_items WHERE customer_id = %s"
    values = [customer_id]
    results = run_sql(sql, values)
    for row in results:
        customer = customer_repository.select_1_customer_by_id(row['customer_id'])
        item = item_repository.select_1_item_by_id(row['item_id'])
        customer_item = CustomerItem(customer, item)
        customers_items.append(customer_item)
    return customers_items

def select_all_customer_item_by_item_id(item_id):
    customers_items = []
    sql = "SELECT * FROM customers_items WHERE item_id = %s"
    values = [item_id]
    results = run_sql(sql, values)
    for row in results:
        customer = customer_repository.select_1_customer_by_id(row['customer_id'])
        item = item_repository.select_1_item_by_id(row['item_id'])
        customer_item = CustomerItem(customer, item)
        customers_items.append(customer_item)
    return customers_items

def delete_1_customer_item_by_id(id):
    sql = "DELETE FROM customers_items WHERE id = %s"
    values = [id]
    run_sql(sql, values)

# def select_by_selection(selection = "all_albums"):
#     if selection == "all_albums":
#         sql = "SELECT * FROM items"
#         values = None
#     else:
#         albums_id = []
#         albums = album_repository.select_by_selection(selection)
#         for album in albums:
#             albums_id.append(album.id)
#         sql = "SELECT * FROM items where album_id IN %s"
#         values = [tuple(albums_id)]
#     items = []
#     results = run_sql(sql, values)
#     for row in results:
#         album = album_repository.select_1_album_by_id(row['album_id'])
#         item = Item(album, row['support'], row['cost'], row['selling_price'], row['in_stock'], row['ordered'], row['id'])
#         items.append(item)
#     return items

# def select_filtered(filter = "all"):
#     if filter == "all":
#         sql = "SELECT * FROM items"
#     else:
#         sql = f"SELECT * FROM items where {filter} >0"
#     results = run_sql(sql)
#     items = []
#     for row in results:
#         album = album_repository.select_1_album_by_id(row['album_id'])
#         item = Item(album, row['support'], row['cost'], row['selling_price'], row['in_stock'], row['ordered'], row['id'])
#         items.append(item)
#     return items

# def select_by_filter_and_selection(filter = "all", selection = "all_albums"):
#     filtered = select_filtered(filter)
#     selected = select_by_selection(selection)
#     items_id =[]
#     for s in selected:
#         for f in filtered:
#             if s.id == f.id:
#                 items_id.append(s.id)
#     items_id = set(items_id)
#     items =[]
#     for id in items_id:
#         items.append(select_1_item_by_id(id))
#     return items

