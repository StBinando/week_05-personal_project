from db.run_sql import run_sql
from models.customer import Customer

def add_customer(customer):
    sql = "INSERT INTO customers (name, contact) VALUES (%s, %s) RETURNING *"
    values = [customer.name, customer.contact]
    results = run_sql(sql, values)
    id = results[0]['id']
    customer.id = id
    return customer

def show_all():
    customers = []
    sql = "SELECT * FROM customers"
    results = run_sql(sql)
    for row in results:
        customer = Customer(row['name'], row['contact'], row['id'])
        customers.append(customer)
    return customers

def select_1_customer_by_id(id):
    sql = "SELECT * FROM customers WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    customer = Customer(result['name'], result['contact'], result['id'])
    return customer

def delete_1_customer_by_id(id):
    sql = "DELETE FROM customers WHERE id = %s"
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

