from flask import Flask, render_template

app = Flask(__name__)
from controllers.items_controller import items_blueprint
from controllers.artists_controller import artists_blueprint
from controllers.album_controller import album_blueprint

app.register_blueprint(items_blueprint)
app.register_blueprint(artists_blueprint)
app.register_blueprint(album_blueprint)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

