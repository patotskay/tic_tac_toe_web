from flask import Flask
from web.module.controller import create_game, post_game
from di.container import Container

app = Flask(__name__)

container = Container()
service = container.get_service()

@app.route('/game', methods=['POST'])
def new_game_route():
    return create_game(service)

@app.route('/game/<uuid>', methods=['POST'])
def game_route(uuid):
    return post_game(uuid, service)

if __name__ == '__main__':
    app.run(debug=True)