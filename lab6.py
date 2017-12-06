from flask import Flask, jsonify, abort, render_template

from find import Game

app = Flask(__name__, static_url_path='', static_folder='static')
names = Game.names
games = dict()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/names', methods=['GET'])
def get_names():
    return jsonify(names)


@app.route('/api/start/<int:level>', methods=['GET'])
def start_game(level):
    g = Game(level)
    games[g.id] = g
    return jsonify(g.__dict__)


@app.route('/api/finish/<int:game_id>/<string:name>', methods=['GET'])
def finish_game(game_id, name):
    try:
        game = games[game_id]
        return jsonify({'result': game.test_name(name)})
    except KeyError:
        return abort(400)


if __name__ == '__main__':
    app.run(debug=True)
