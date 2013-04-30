PostPrompt
========

PostPrompt virtual card game in Java

 How to
-------

To set up the environment
From the root of the project (e.g. /home/john/postprompt)
(the same location that this file is located in), run:

	./tool/postprompt bashrc

Then source your bashrc

	source ~/.bashrc

Then to set up the database
and get the requirements for this project
(Fedora/Ubuntu only)

	postprompt setup

To see the help text of the main program, run:

	postprompt

To compile the host backend, tyep:

	postprompt javac

To run just the host, type:

	postprompt host

Then navigate to a new terminal and
To run the web server, type:

	postprompt django

OR

To run the command line client, type:

	postprompt client

 TODO:
------

Host:
 - Need to have tickers for persistant cards
 - Make requests and responses async
 - Make host require 2 new requests to start a game (a game between the two users)
 - Add more card effects
 - Limit copies of a card
 - Finish Actions
 - Finish Play
 - Still have parameters per different type of card

Web:
 - Make requests and responses async
 - Interface for game play needs to be fleshed out
 - More info for card viewing (images, text, name, stats)
 - Have deck creation inform about failed requirements for playing (too small, too many copies of card, etc)
