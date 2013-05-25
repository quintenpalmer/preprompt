PostPrompt
========

PostPrompt - a virtual card game in Go and Python

 How to
-------

To set up the environment

From the root of the project (e.g. /home/john/postprompt)

(the same location that this file is located in)

	./bin/postprompt bashrc

Then source your bashrc

	source ~/.bashrc

Then to set up the database

and get the requirements for this project

(Fedora/Ubuntu only)

	postprompt setup

To see the help text of the main program

	postprompt

To run just the host

	postprompt host

Then navigate to a new terminal and

To run the web server

	postprompt django

OR

To run the command line client

	postprompt client

 TODO:
------

Host:
 - Make requests and responses async
 - Make host require 2 new requests to start a game (a game between the two users)
 - Add more card effects
 - Limit copies of a card
 - Ability for triggers to spawn new SubActions
 - Card Play needs ability to handle parameters

Web:
 - Make requests and responses async
 - Interface for game play needs to be fleshed out
 - More info for card viewing (images, text, name, stats)
 - Have deck creation inform about failed requirements for playing (too small, too many copies of card, etc)
