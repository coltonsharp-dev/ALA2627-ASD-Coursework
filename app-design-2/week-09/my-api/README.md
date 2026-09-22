# my-api — Week 9

Start the server:

```
python app.py
```

The terminal prints an address. Your routes hang off the end of it:

```
<your address>/api/health
```

If `python app.py` says Flask is not installed:

```
pip install -r requirements.txt
```

Stop the server with Ctrl+C. Leave it running while you test — open a **second**
terminal for `curl`, or the server has no one listening.

Set the forwarded port to **Public**, or your turn-in link only works for you.
