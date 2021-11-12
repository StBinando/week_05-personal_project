import pdb

from models.artist import Artist
from models.album import Album
from models.item import Item
from models.customer import Customer
from models.pre_order import PreOrder


import repositories.artist_repository as artist_repository

import os
os.system('psql -d rubberduck_records -f db/rubberduck_records.sql')


artist_1 = Artist("David Bowie")
artist_2 = Artist("Iggy Pop")
album_1 = Album(artist_1, "Low")
item_1 = Item(album_1, "CD", 6.50, 9.99, 7, 2, 1)
customer_1 = Customer("John Smith", "+447857634091")
pre_order_1 = PreOrder(customer_1, item_1)


result = artist_repository.add_artist(artist_1)
print("------------- ADDS 1st ARTIST ----------------")
print( result.__dict__ )

result = artist_repository.add_artist(artist_2)
print("------------- ADDS 2nd ARTIST ----------------")
print( result.__dict__ )

results = artist_repository.show_all()
print("------------- PRINT ALL ARTISTS ----------------")
for row in results:
    print(row.__dict__)




