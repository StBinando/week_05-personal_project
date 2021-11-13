from flask import Flask, redirect, render_template, request
from app import app

# CLASSES
from models.item import Item
from models.album import Album
from models.artist import Artist

#  REPOSITORIES
import repositories.item_repository as item_repository



# INVENTORY
@app.route('/inventory')
def inventory():
    all_albums = item_repository.show_all()
    return render_template("inventory.html", all_albums = all_albums)