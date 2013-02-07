pyprompt
========

postprompt card game in python

---
How to
---

To set up the environment (linux and mac only)
From the root of the project (e.g. /home/john/pyprompt)
(the same location that this file is located in), run:

./bin/pyp setup

To run the full program, run:

pyp

To run just the host, run:

pyp host

To run just the client, run:

pyp client

To shut the host down, run:

pyp dc

To clear all game data, run:

pyp drop

To clear out all .pyc files, run:

pyp pyc


----------
TODO:
----------
Client:
 - Frontend written for web browser
 - Make requests and responses async
Host:
 - Add more card effects
 - Limit copies of a card
 - Add real database for player decks, card effects, and maybe save data
 - Make host require 2 new requests to start a game (a game between the two users)
 - Make requests and responses async
 - Need to have tickers for persistant cards
