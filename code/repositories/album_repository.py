from db.run_sql import run_sql
from models.artist import Artist
from models.album import Album

import repositories.artist_repository as artist_repository


def add_album(album):
    sql = "INSERT INTO albums (artist_id, title) VALUES (%s, %s) RETURNING *"
    values = [album.artist.id, album.title]
    results = run_sql(sql, values)
    id = results[0]['id']
    album.id = id
    return album

def show_all():
    albums = []
    sql = "SELECT * FROM albums"
    results = run_sql(sql)
    for row in results:
        artist = artist_repository.select_1_artist_by_id(row['artist_id'])
        album = Album(artist, row['title'], row['id'])
        albums.append(album)
    return albums

def select_1_album_by_id(id):
    sql = "SELECT * FROM albums where id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    artist = artist_repository.select_1_artist_by_id(result['artist_id'])
    album = Album(artist, result['title'], result['id'])
    return album

def delete_1_album_by_id(id):
    sql = "DELETE FROM albums WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def select_by_selection(selection = "all_albums"):
    if selection == "all_albums":
        sql = "SELECT * FROM albums"
    else:
        artists_id = []
        artists = artist_repository.select_by_selection(selection)
        for artist in artists:
            artists_id.append(artist.id)
        sql = "SELECT * FROM albums where artist_id IN %s"
        values = [tuple(artists_id)]
        print(artists_id)
    albums = []
    results = run_sql(sql, values)
    for row in results:
        artist = artist_repository.select_1_artist_by_id(row['artist_id'])
        album = Album(artist, row['title'], row['id'])
        albums.append(album)
    return albums
        