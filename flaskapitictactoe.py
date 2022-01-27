from flask import Flask, jsonify, request

playerinfo = []

app = Flask(__name__)


# retrieve all playerinfo
@app.route('/players')
def get_allplayer():
    return jsonify({'players': playerinfo})


# retrieve all one playerinfo.
@app.route('/player/<string:name>')
def get_oneplayerinfo(name):
    for player in playerinfo:
        if player['name'] == name:
            return jsonify(player)

    return jsonify({'message': 'player not found'})


# create a new player .
@app.route('/player', methods=["POST"])
def player_input():
    request_data = request.get_json()
    playerinfo.append(request_data)
    return jsonify({"message": "Player has been added"})


# @app.route('/player/table', methods=["POST"])
# def display_table():
#     table = [["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]
#     print(table[0][0] + " | " + table[0][1] + " | " + table[0][2])
#     print(table[1][0] + " | " + table[1][1] + " | " + table[1][2])
#     print(table[2][0] + " | " + table[2][1] + " | " + table[2][2])
#     request_data1 = request.get_json()
#     return jsonify(request_data1)

if __name__ == "__main__":
 app.run(debug=True, port=8000)
