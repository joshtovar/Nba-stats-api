from flask import Flask, request, jsonify
from nba_service import get_player_stats, compare_players


@app.route("/player", methods=["POST"])
def player():
    data = request.json

    name = data.get("player")
    season = data.get("season")

    stats = get_player_stats(name, season)

    return jsonify(stats)