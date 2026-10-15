"""app.py — your Blue Plate kitchen. Week 11: Tickets 1 to 5 on the Line.

Start it:      python app.py
Stop it:       Ctrl+C in the terminal
Your address:  the Ports panel, port 5000, set to Public. That address goes into the game.
The pass:      https://thebrightworkhouse.com/blueplate/  — clock in, The Line, paste your address.

Work on ONE ticket at a time. Run the pass after every change. Commit and push at every save point.
You never paste code you cannot explain. A plan tells you what to write; you type it.
"""

from flask import Flask, jsonify, request

app = Flask(__name__)


# ─────────────── Ticket 1 · Open the pass ───────────────
# Your server answers. The game runs in a browser on another address, and a browser will not
# READ an answer from a different address unless the server says it may. That permission is a
# header, and flask-cors adds it to every answer:
#
#   pip install flask-cors            (it is in requirements.txt already)
#   from flask_cors import CORS       (at the top, with the other imports)
#   CORS(app)                         (right after app = Flask(__name__))
#
# Then the health check: the floor reads ok (true or false) and kitchen (your place's name).
@app.route("/api/health")
def health():
    return jsonify(status="ok", week=9)


# ─────────────── Ticket 2 · The board ───────────────
# A menu is a list of plates. Every plate is a dict with the SAME keys:
#   id (a whole number that never changes), name, price (a number, no dollar sign), course.
# course is one of: starter, main, dessert, drink. Six plates at least, one in every course.
# MENU = [
#     {"id": 1, "name": "", "price": 0.0, "course": ""},
# ]
#
# @app.route("/api/menu")
# def menu():
#     return jsonify(MENU)


# ─────────────── Ticket 3 · One plate ───────────────
# <int:plate_id> in the route takes the number off the end of the address and hands it to you.
# When there is no such plate, say so IN JSON, with an error key, and say it with a 404.
# A 200 with nothing in it tells the floor the plate exists and is empty. It does not.
# @app.route("/api/menu/<int:plate_id>")
# def one_plate(plate_id):
#     for plate in MENU:
#         if plate["id"] == plate_id:
#             return jsonify(plate)
#     return jsonify(error=f"plate {plate_id} is not on the menu"), 404


# ─────────────── Ticket 4 · Eighty-six ───────────────
# Every plate gets "available": True in MENU. PATCH changes it; the body is JSON:
#   {"available": false}  takes it off     {"available": true}  puts it back
# Check the body before you trust it. Not a boolean → 400 with a message. No such plate → 404.
# @app.route("/api/menu/<int:plate_id>", methods=["PATCH"])
# def change_plate(plate_id):
#     data = request.get_json(silent=True)
#     if data is None:
#         return jsonify(error="send JSON, with Content-Type: application/json"), 400
#     if not isinstance(data.get("available"), bool):
#         return jsonify(error="available must be true or false"), 400
#     ...find the plate, or 404...
#     plate["available"] = data["available"]
#     return jsonify(plate)


# ─────────────── Ticket 5 · Full house ───────────────
# Nothing new to write. The house floor orders from your kitchen, in order, fast. Watch your
# terminal: every line it logs is a request you are answering for a stranger.


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
