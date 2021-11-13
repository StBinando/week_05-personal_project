from models.artist import Artist
from models.album import Album
from models.item import Item
from models.customer import Customer
from models.customer_item import CustomerItem
from random import Random, randint, uniform


import repositories.artist_repository as artist_repository
import repositories.album_repository as album_repository
import repositories.item_repository as item_repository

import os
os.system('psql -d rubberduck_records -f db/rubberduck_records.sql')


# --------------------------- CREATES ARTISTS ------------------------------
artist_1 = Artist("Bowie", "David")
artist_2 = Artist("B-52's", "The")
artist_3 = Artist("Prince")
artist_4 = Artist("Cure", "The")
artist_5 = Artist("Dead Kennedys")
artist_6 = Artist("Police", "The")
artist_7 = Artist("Gabriel", "Peter")
artist_8 = Artist("Arctic Monkeys")
artist_9 = Artist("Beatles", "The")
artist_10 = Artist("Clash", "The")
artist_11 = Artist("Who", "The")
artist_12 = Artist("Zappa", "Frank")
artist_13 = Artist("10,000 Maniacs")

for i in range(1,14):
    exec(f'artist_repository.add_artist(artist_{i})')

# --------------------------- CREATES ALBUMS ------------------------------
album_1 = Album(artist_1, "Scary Monsters (and Super Creeps)")
album_2 = Album(artist_1, "Hunky Dory")
album_3 = Album(artist_1, '"Heroes"')
album_4 = Album(artist_1, "The Rise and Fall of Ziggy Stardust and the Spiders from Mars")
album_5 = Album(artist_2, "The B-52's")
album_6 = Album(artist_3, "Purple Rain")
album_7 = Album(artist_3, "Signs of the times")
album_8 = Album(artist_4, "Boys don't cry")
album_9 = Album(artist_4, "Kiss me, kiss me, kiss me")
album_10 = Album(artist_4, "Three imaginary boys")
album_11 = Album(artist_5, "Fresh fruit for rotten vegetables")
album_12 = Album(artist_5, "Bedtime for democracy")
album_13 = Album(artist_6, "Sincronicity")
album_14 = Album(artist_7, "Us")
album_15 = Album(artist_7, "Peter Gabriel")
album_16 = Album(artist_8, "Whatever People Say I Am, That's What I'm Not")
album_17 = Album(artist_8, "Favourite worst nightmare")
album_18 = Album(artist_9, "Sgt. Pepper's Lonely Hearts Club Band")
album_19 = Album(artist_9, "Help!")
album_20 = Album(artist_9, "Revolver")
album_21 = Album(artist_9, "Abbey Road")
album_22 = Album(artist_10, "The Clash")
album_23 = Album(artist_10, "London Calling")
album_24 = Album(artist_11, "Who's Next")
album_25 = Album(artist_11, "Tommy")
album_26 = Album(artist_11, "Quadrophenia")
album_27 = Album(artist_12, "Sheik Yerbouti")
album_28 = Album(artist_12, "Joe's Garage")
album_29 = Album(artist_13, "Love Among the Ruins")
album_30 = Album(artist_1, "Black Star")

for i in range(1,31):
    exec(f'album_repository.add_album(album_{i})')

# --------------------------- CREATES ITEMS ------------------------------
item_1 = Item(album_1, "CD", 6.50, 9.99, 7, 0)
item_2 = Item(album_1, "Vinyl", 9.50, 18.99, 2, 0)
item_3 = Item(album_2, "CD", 7, 13.89, 7, 2)
item_4 = Item(album_3, "CD", 7.50, 9.99, 12, 0)
item_5 = Item(album_3, "Vinyl", 11.90, 18.99, 2, 0)
item_6 = Item(album_4, "Vinyl", 10.30, 18.99, 2, 0)
item_7 = Item(album_4, "CD", 10, 9.99, 7, 2)
item_8 = Item(album_2, "Vinyl", 9.50, 9.99, 7, 2)
item_9 = Item(album_5, "Vinyl", 14.50, 18.99, 2, 0)
item_10= Item(album_5, "CD", 9, 9.99, 7, 2)
item_11= Item(album_6, "Vinyl", 14, 18.99, 2, 0)
item_12= Item(album_6, "CD", 9, 9.99, 7, 2)
item_13= Item(album_7, "CD", 12, 9.99, 7, 2)
item_14= Item(album_8, "CD", 12, 9.99, 7, 2)
item_15= Item(album_8, "Vinyl", 15, 18.99, 2, 0)
item_16= Item(album_9, "CD", 14, 9.99, 7, 2)
item_17= Item(album_9, "Vinyl", 19, 18.99, 2, 0)
item_18= Item(album_10, "CD", 5, 9.99, 7, 2)
item_19= Item(album_10, "Vinyl", 11, 18.99, 2, 0)
item_20= Item(album_11, "Vinyl", 10, 18.99, 2, 0)
item_21= Item(album_12, "Vinyl", 14, 18.99, 2, 0)
item_22= Item(album_13, "Vinyl", 13.70, 18.99, 2, 0)
item_23= Item(album_14, "Vinyl", 15, 18.99, 2, 0)
item_24= Item(album_14, "CD", 7.50, 9.99, 7, 2)
item_25= Item(album_15, "Vinyl", round(uniform(5,10),2), round(uniform(10,18),2), randint(0,10), randint(0,3))
item_26= Item(album_15, "CD", round(uniform(5,10),2), round(uniform(10,18),2), randint(0,10), randint(0,3))
item_27= Item(album_16, "Vinyl", round(uniform(5,10),2), round(uniform(10,18),2), randint(0,10), randint(0,3))
item_28= Item(album_16, "CD", round(uniform(5,10),2), round(uniform(10,18),2), randint(0,10), randint(0,3))
item_29= Item(album_17, "Vinyl", round(uniform(5,10),2), round(uniform(10,18),2), randint(0,10), randint(0,3))
item_30= Item(album_17, "CD", round(uniform(5,10),2), round(uniform(10,18),2), randint(0,10), randint(0,3))
item_31= Item(album_18, "Vinyl", round(uniform(5,10),2), round(uniform(10,18),2), randint(0,10), randint(0,3))
item_32= Item(album_18, "CD", round(uniform(5,10),2), round(uniform(10,18),2), randint(0,10), randint(0,3))
item_33= Item(album_19, "Vinyl", round(uniform(5,10),2), round(uniform(10,18),2), randint(0,10), randint(0,3))
item_34= Item(album_19, "CD", round(uniform(5,10),2), round(uniform(10,18),2), randint(0,10), randint(0,3))
item_35= Item(album_20, "CD", round(uniform(5,10),2), round(uniform(10,18),2), randint(0,10), randint(0,3))
item_36= Item(album_21, "CD", round(uniform(5,10),2), round(uniform(10,18),2), randint(0,10), randint(0,3))
item_37= Item(album_22, "CD", round(uniform(5,10),2), round(uniform(10,18),2), randint(0,10), randint(0,3))
item_38= Item(album_23, "CD", round(uniform(5,10),2), round(uniform(10,18),2), randint(0,10), randint(0,3))
item_39= Item(album_24, "CD", round(uniform(5,10),2), round(uniform(10,18),2), randint(0,10), randint(0,3))
item_40= Item(album_24, "Vinyl", round(uniform(5,10),2), round(uniform(10,18),2), randint(0,10), randint(0,3))
item_41= Item(album_25, "Vinyl", round(uniform(5,10),2), round(uniform(10,18),2), randint(0,10), randint(0,3))
item_42= Item(album_26, "Vinyl", round(uniform(5,10),2), round(uniform(10,18),2), randint(0,10), randint(0,3))
item_43= Item(album_27, "Vinyl", round(uniform(5,10),2), round(uniform(10,18),2), randint(0,10), randint(0,3))
item_44= Item(album_28, "Vinyl", round(uniform(5,10),2), round(uniform(10,18),2), randint(0,10), randint(0,3))
item_45= Item(album_29, "Vinyl", round(uniform(5,10),2), round(uniform(10,18),2), randint(0,10), randint(0,3))
item_46= Item(album_29, "CD", round(uniform(5,10),2), round(uniform(10,18),2), randint(0,10), randint(0,3))
item_47= Item(album_30, "Vinyl", round(uniform(5,10),2), round(uniform(10,18),2), randint(0,10), randint(0,3))
item_48= Item(album_30, "CD", round(uniform(5,10),2), round(uniform(10,18),2), randint(0,10), randint(0,3))
item_49= Item(album_12, "CD", round(uniform(5,10),2), round(uniform(10,18),2), randint(0,10), randint(0,3))

for i in range(1,50):
    exec(f'item_repository.add_item(item_{i})')

# --------------------------- CREATES CUSTOMERS ------------------------------
customer_1 = Customer("John Smith", "+447857634091")

# --------------------------- CREATES CUSTOMERS-ITEMS ------------------------------
customer_item_1 = CustomerItem(customer_1, item_1)

