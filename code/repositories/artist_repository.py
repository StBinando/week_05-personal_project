from db.run_sql import run_sql
from models.artist import Artist

import repositories.album_repository as album_repository

def add_artist(artist):
    sql = "INSERT INTO artists (last_name, first_name) VALUES (%s, %s) RETURNING *"
    values = [artist.last_name, artist.first_name]
    results = run_sql(sql, values)
    id = results[0]['id']
    artist.id = id
    return artist

def show_all():
    artists = []
    sql = "SELECT * FROM artists"
    results = run_sql(sql)
    for row in results:
        artist = Artist(row['last_name'], row['first_name'], row['id'])
        artists.append(artist)
    return artists

def select_1_artist_by_id(id):
    sql = "SELECT * FROM artists where id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    artist = Artist(result['last_name'], result['first_name'], result['id'])
    return artist

def delete_1_artist_by_id(id):
    sql = "DELETE FROM artists WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def select_by_selection(selection = "all_albums"):
    if filter == "all":
        pass
    else:
        pass

    if selection == "all_albums":
        sql = "SELECT * FROM artists"
    else:
        sql = f"SELECT * FROM artists where last_name LIKE '{selection}%'"
    results = run_sql(sql)
    artists = []
    for row in results:
        artist = Artist(row['last_name'], row['first_name'], row['id'])
        artists.append(artist)
    return artists

def select_filtered(filter = "all"):
    artists = []
    if filter == "all":
        artists = show_all()
    else:
        albums = album_repository.select_filtered(filter)
        artists_id = []
        for album in albums:
            artists_id.append(album.artist.id)
        artists_id = set(artists_id)
        for id in artists_id:
            artist = select_1_artist_by_id(id)
            artists.append(artist)
        artists = set(artists)
    return artists