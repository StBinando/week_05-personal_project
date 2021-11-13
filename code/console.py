# import pdb

from models.artist import Artist
from models.album import Album
from models.item import Item
from models.customer import Customer
from models.customer_item import CustomerItem


import repositories.artist_repository as artist_repository
import repositories.album_repository as album_repository
import repositories.item_repository as item_repository

# import os
# os.system('psql -d rubberduck_records -f db/rubberduck_records.sql')


# --------------------------- CREATES OBJECTS FOR TESTS ------------------------------
# artist_1 = Artist("Bowie", "David")
# artist_2 = Artist("Pop", "Iggy")

# album_1 = Album(artist_1, "Low")
# album_2 = Album(artist_1, "Pin-Up")

# item_1 = Item(album_1, "CD", 6.50, 9.99, 7, 2)
# item_2 = Item(album_1, "Vinyl", 9.50, 18.99, 2, 0)

# customer_1 = Customer("John Smith", "+447857634091")

# customer_item_1 = CustomerItem(customer_1, item_1)



# # --------------------------- TESTS FOR ARTIST REPO ------------------------------
# print("------------- ADDS 1st ARTIST ----------------")
# result = artist_repository.add_artist(artist_1)
# print(result.__dict__)

# print("------------- ADDS 2nd ARTIST ----------------")
# result = artist_repository.add_artist(artist_2)
# print(result.__dict__)

# print("------------- PRINT ALL ARTISTS ----------------")
# results = artist_repository.show_all()
# for row in results:
#     print(row.__dict__)

# print("------------- PRINTS 2nd ARTIST ----------------")
# result = artist_repository.select_1_artist_by_id(2)
# print(result.__dict__)

# print("-------------- DELETE 2nd ARTIST ------------")
# artist_repository.delete_1_artist_by_id(2)
# results = artist_repository.show_all()
# for row in results:
#     print(row.__dict__)

# # --------------------------- TESTS FOR ALBUM REPO ------------------------------
# print("------------- ADDS 1st ALBUM ----------------")
# result = album_repository.add_album(album_1)
# print(result.__dict__)

# print("------------- ADDS 2nd ALBUM ----------------")
# result = album_repository.add_album(album_2)
# print(result.__dict__)

# print("------------ PRINT ALL ALBUMS -------------")
# results = album_repository.show_all()
# for row in results:
#     print(row.__dict__)

# print("------------ PRINT 2nd ALBUM -------------")
# result = album_repository.select_1_album_by_id(2)
# print(result.__dict__)

# print("------------ DELETES 2nd ALBUM --------------")
# album_repository.delete_1_album_by_id(2)
# results = album_repository.show_all()
# for row in results:
#     print(row.__dict__)


# # --------------------------- TESTS FOR ITEM REPO ------------------------------
# print("------------- ADDS 1st ITEM ----------------")
# result = item_repository.add_item(item_1)
# print(result.__dict__)

# print("------------- ADDS 2nd ITEM ----------------")
# result = item_repository.add_item(item_2)
# print(result.__dict__)

# print("------------ PRINT ALL ITEMS -------------")
# results = item_repository.show_all()
# for row in results:
#     print(row.__dict__)

# print("------------ PRINT 2nd ITEM -------------")
# result = item_repository.select_1_item_by_id(2)
# print(result.__dict__)

# print("------------ DELETES 2nd ITEM --------------")
# item_repository.delete_1_item_by_id(2)
# results = item_repository.show_all()
# for row in results:
#     print(row.__dict__)

# *****************************************************
# *****************************************************
#                   FILTERS SECTION
# *****************************************************
# *****************************************************

# print("------------ ARTISTS beginning with B --------------")
# results = artist_repository.select_by_selection("B")
# for row in results:
#     print(row.__dict__)

# print("------------ ALBUMS of artists beginning with B --------------")
# results = album_repository.select_by_selection("B")
# for row in results:
#     print(row.__dict__)


# print("------------ ITEMS of artists beginning with B --------------")
# results = item_repository.select_by_selection("B")
# for row in results:
#     print(row.__dict__)


# print("------------ ITEMS ALL --------------")
# results = item_repository.select_filtered("all")
# print(len(results))

# print("------------ ITEMS IN-STOCK --------------")
# results = item_repository.select_filtered("in_stock")
# print(len(results))

# print("------------ ITEMS ORDERED --------------")
# results = item_repository.select_filtered("ordered")
# print(len(results))


# print()
# print()
# print("------------ ALBUMS ALL --------------")
# results = album_repository.select_filtered("all")
# print(len(results))

# print("------------ ALBUMS IN-STOCK --------------")
# results = album_repository.select_filtered("in_stock")
# print(len(results))

# print("------------ ALBUMS ORDERED --------------")
# results = album_repository.select_filtered("ordered")
# print(len(results))


# print()
# print()
# print("------------ ARTISTS ALL --------------")
# results = artist_repository.select_filtered("all")
# print(len(results))

# print("------------ ARTISTS IN-STOCK --------------")
# results = artist_repository.select_filtered("in_stock")
# print(len(results))

# print("------------ ARTISTS ORDERED --------------")
# results = artist_repository.select_filtered("ordered")
# print(len(results))


print("------------ ARTISTS ORDERED with B--------------")
results = artist_repository.select_by_filter_and_selection("ordered", "B")
print(len(results))

print("------------ ALBUMS ORDERED by artists with B--------------")
results = album_repository.select_by_filter_and_selection("ordered", "B")
print(len(results))

print("------------ Items ORDERED by artists with B--------------")
results = item_repository.select_by_filter_and_selection("ordered", "B")
print(len(results))
