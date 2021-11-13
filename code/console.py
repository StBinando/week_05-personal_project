# import pdb

from models.artist import Artist
from models.album import Album
from models.item import Item
from models.customer import Customer
from models.customer_item import CustomerItem


import repositories.artist_repository as artist_repository
import repositories.album_repository as album_repository
import repositories.item_repository as item_repository
import repositories.customer_repository as customer_repository
import repositories.customer_item_repository as customer_item_repository

import os
os.system('psql -d rubberduck_records -f db/rubberduck_records.sql')


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


# print("------------ ARTISTS ORDERED with B--------------")
# results = artist_repository.select_by_filter_and_selection("ordered", "B")
# print(len(results))

# print("------------ ALBUMS ORDERED by artists with B--------------")
# results = album_repository.select_by_filter_and_selection("ordered", "B")
# print(len(results))

# print("------------ Items ORDERED by artists with B--------------")
# results = item_repository.select_by_filter_and_selection("ordered", "B")
# print(len(results))


# # *****************************************************
# # *****************************************************
# #                   CUSTOMERS SECTION
# # *****************************************************
# # *****************************************************

# customer_1 = Customer("John Smith", "+447857634091")
# customer_2 = Customer("Lewis Carroll", "lewis.Carroll@gmail.com")
# customer_3 = Customer("Nick Hornby", "+441317543329")

# # --------------------------- TESTS FOR CUSTOMER REPO ------------------------------
# print("------------- ADDS 1st CUSTOMER ----------------")
# result = customer_repository.add_customer(customer_1)
# print(result.__dict__)

# print("------------- ADDS 2nd and 3rd CUSTOMERS ----------------")
# result = customer_repository.add_customer(customer_2)
# print(result.__dict__)
# result = customer_repository.add_customer(customer_3)
# print(result.__dict__)

# print("------------- PRINT ALL CUSTOMERS ----------------")
# results = customer_repository.show_all()
# for row in results:
#     print(row.__dict__)

# print("------------- PRINTS 2nd CUSTOMER ----------------")
# result = customer_repository.select_1_customer_by_id(2)
# print(result.__dict__)

# print("-------------- DELETE 2nd CUSTOMER ------------")
# customer_repository.delete_1_customer_by_id(2)
# results = customer_repository.show_all()
# for row in results:
#     print(row.__dict__)


# *****************************************************
# *****************************************************
#             CUSTOMERS-ITEMS SECTION
# *****************************************************
# *****************************************************

# customer_1 = Customer("John Smith", "+447857634091")
# customer_2 = Customer("Lewis Carroll", "lewis.Carroll@gmail.com")
# customer_3 = Customer("Nick Hornby", "+441317543329")
# for i in range(1,4):
#     exec(f'customer_repository.add_customer(customer_{i})')

# artist_1 = Artist("Bowie", "David")
# artist_2 = Artist("B-52's", "The")
# artist_3 = Artist("Prince")
# for i in range(1,4):
#     exec(f'artist_repository.add_artist(artist_{i})')

# album_1 = Album(artist_1, "Scary Monsters (and Super Creeps)")
# album_2 = Album(artist_1, "Hunky Dory")
# album_3 = Album(artist_1, '"Heroes"')
# album_4 = Album(artist_1, "The Rise and Fall of Ziggy Stardust and the Spiders from Mars")
# album_5 = Album(artist_2, "The B-52's")
# album_6 = Album(artist_3, "Purple Rain")
# for i in range(1,7):
#     exec(f'album_repository.add_album(album_{i})')

# item_1 = Item(album_1, "CD", 6.50, 9.99, 0, 0)
# item_2 = Item(album_3, "Vinyl", 11.90, 18.99, 2, 0)
# item_3 = Item(album_4, "CD", 10, 9.99, 7, 0)
# item_4 = Item(album_5, "Vinyl", 14.50, 18.99, 2, 0)
# item_5= Item(album_6, "Vinyl", 14, 18.99, 2, 0)
# item_6= Item(album_2, "Vinyl", 15, 18.99, 2, 0)
# for i in range(1,7):
#     exec(f'item_repository.add_item(item_{i})')

# customer_item_1 = CustomerItem(customer_1, item_3)
# customer_item_2 = CustomerItem(customer_2, item_1)
# customer_item_3 = CustomerItem(customer_2, item_5)
# customer_item_4 = CustomerItem(customer_3, item_3)
# customer_item_5 = CustomerItem(customer_2, item_3)
# customer_item_6 = CustomerItem(customer_3, item_6)
# customer_item_7 = CustomerItem(customer_3, item_2)
# customer_item_8 = CustomerItem(customer_3, item_4)


# # --------------------------- TESTS FOR CUSTOMER REPO ------------------------------
# print("------------- ADDS 1st CUSTOMER-ITEM ----------------")
# result = customer_item_repository.add_customer_item(customer_item_1)
# print(result.__dict__)

# print("------------- ADDS 2 to 8 CUSTOMER-ITEM ----------------")
# for i in range(2,9):
#     exec(f'customer_item_repository.add_customer_item(customer_item_{i})')

# print("------------- PRINT ALL CUSTOMER-ITEMs ----------------")
# results = customer_item_repository.show_all()
# for row in results:
#     print(row.__dict__)

# print("------------- PRINTS 2nd CUSTOMER-ITEM ----------------")
# result = customer_item_repository.select_1_customer_item_by_id(2)
# print(result.__dict__)

# print("-------------- DELETE 2nd CUSTOMER-ITEM ------------")
# customer_item_repository.delete_1_customer_item_by_id(2)
# results = customer_item_repository.show_all()
# for row in results:
#     print(row.__dict__)

# print("------------- PRINT ALL CUSTOMER-ITEMs of one customer----------------")
# results = customer_item_repository.select_all_customer_item_by_customer_id(customer_1.id)
# for row in results:
#     print(row.__dict__)

# print("------------- PRINT ALL CUSTOMER-ITEMs for one item----------------")
# results = customer_item_repository.select_all_customer_item_by_item_id(item_3.id)
# for row in results:
#     print(row.__dict__)
