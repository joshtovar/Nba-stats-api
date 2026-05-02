from flask import Flask, request, jsonify, render_template
from nba_service import get_player_stats, compare_players

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

# Flask route for single player statistics in a season
@app.route("/player", methods=["POST"])
def player():
    data = request.json

    name = data.get("player")
    season = data.get("season")

    stats = get_player_stats(name, season)

    return jsonify(stats)

# Flask route for comparing two players stats in a season
@app.route("/compare", methods=["POST"])
def compare():
    data = request.json

    name1 = data.get("player1")
    name2 = data.get("player2")
    season = data.get("season")

    result = compare_players(name1, name2, season)

    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)