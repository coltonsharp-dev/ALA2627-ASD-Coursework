"""app.py — your Week 9 server. One file, five days.

Start it:      python app.py
Stop it:       Ctrl+C in the terminal
Your address:  the terminal prints it. Add your route on the end, like /api/health

Work on ONE day's section at a time. Commit and push at every save point.
You never paste code you cannot explain. A plan tells you what to write; you type it.
"""

from flask import Flask, jsonify, request

app = Flask(__name__)


# ─────────────── MON · Prove the server is alive ───────────────
# A route is a URL your server answers to. jsonify turns a Python dict into JSON
# and sets the content type, so the browser shows data instead of a web page.
@app.route("/api/health")
def health():
    return jsonify(status="ok", week=9)


# TODO MON: open your forwarded address with /api/health on the end and read the JSON.
#           Then find the line your request logged in the terminal and read the 200 off it.
#           Set the port to Public, or the link only works for you.


# ─────────────── TUE · /api/about returns YOUR bio JSON ───────────────
# Not one flat row: a list inside it, and an object inside it. Nothing you would
# mind a stranger reading — this address is public.
# @app.route("/api/about")
# def about():
#     return jsonify({
#         "name": "your first name only",
#         "course": "App Design 2",
#         "skills": ["", "", ""],                 # a LIST inside the object
#         "project": {"title": "", "status": ""},  # an OBJECT inside the object
#     })


# ─────────────── WED · POST, and the body of a request ───────────────
# A GET asks for something. A POST carries something with it — the body.
# methods=["POST"] is what makes this route accept one. Take it off and a POST
# to this address comes back 405: the route exists, that method does not.
# @app.route("/api/note", methods=["POST"])
# def note():
#     data = request.get_json()          # the body, as a Python dict
#     return jsonify(received=data["text"])
#
# Test it from the terminal, in a SECOND terminal, with the server still running:
#   curl -X POST http://localhost:5000/api/note \
#        -H "Content-Type: application/json" \
#        -d '{"text":"hello"}'


# ─────────────── THU · /api/echo sends back what you sent ───────────────
# It has to be reading the body, not repeating a hard-coded answer. The test:
# change what you send, and the reply changes with it.
# @app.route("/api/echo", methods=["POST"])
# def echo():
#     data = request.get_json()
#     return jsonify(you_sent=data, keys=len(data))   # plus ONE thing of your own


# ─────────────── FRI · Whose fault was it? 400 against 500 ───────────────
# 400 means the caller sent something wrong. 500 means your code broke.
# Reading data["text"] when there is no "text" raises a KeyError, and Flask turns
# that into a 500 — your fault, for a mistake that was theirs. Check first.
#
# @app.route("/api/echo", methods=["POST"])
# def echo():
#     data = request.get_json(silent=True)
#     if data is None:
#         return jsonify(error="Send JSON, with Content-Type: application/json"), 400
#     if "text" not in data:
#         return jsonify(error="Missing key: text"), 400
#     return jsonify(you_sent=data, length=len(data["text"])), 200
#
# The check must not block the normal case: a good request still comes back 200.


if __name__ == "__main__":
    # host 0.0.0.0 so the forwarded address reaches it, not just this machine.
    # debug=True reloads the server when you save, and prints the line that broke.
    app.run(host="0.0.0.0", port=5000, debug=True)
