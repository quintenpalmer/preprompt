PostPrompt
========

PostPrompt virtual card game in Python (Java soon)

How to
---

To set up the environment (linux and mac only)
and set up the database
From the root of the project (e.g. /home/john/postprompt)
(the same location that this file is located in), run:

> ./bin/pyp setup

To see the help text of the main program, run:

> pyp

To run just the host (in the background), run:

> pyp hostback

To run the web server, run:

> pyp djr

To run just the client, run:

> pyp client

TODO:
---

Client:
 - Make requests and responses async
 - Frontend written for web browser

Host:
 - Need to have tickers for persistant cards
 - Make requests and responses async
 - Make host require 2 new requests to start a game (a game between the two users)
 - Add more card effects
 - Limit copies of a card

Web:
 - Ability to create decks (other than predefined ones)
 - Cards need unique ids (there will be one pool of cards)
 - Decks need to point to either the unique ids or have another set of ids for cards that you own
 - Interface for game play needs to be fleshed out
