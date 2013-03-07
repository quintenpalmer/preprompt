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

Host:
 - Need to have tickers for persistant cards
 - Make requests and responses async
 - Make host require 2 new requests to start a game (a game between the two users)
 - Add more card effects
 - Limit copies of a card

Web:
 - Make requests and responses async
 - Interface for game play needs to be fleshed out
 - More info for card viewing (images, text, name, stats)
 - Have deck creation inform about failed requirements for playing (too small, too many copies of card, etc)
