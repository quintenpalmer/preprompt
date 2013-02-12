README for PostPrompt!

1.     ENVIRONMENT SETUP
________________________________________
Some simple environment can be done to run the code the same way I do.
If you are running linux, edit your bashrc (or similar file) to include the following 2 lines:

export postprompt="/PATH/TO/PROJECT/DIRECTORY"
export PATH=$postprompt/bin:$PATH

and replacing /PATH/TO/PROJECT/DIRECTORY with whatever the path to the directory that 
contains this project (in linux/mac this can be found by navigating to the project directory and 
entering the command 

pwd


2.     COMPILING CODE
________________________________________
2.1    FROM THE TERMINAL
========================================
2.1.1  WITH LINUX ENVIRONMENT SET UP
----------------------------------------
To compile both the host and the client simply enter

ppcompile 

To compile only the host type 

ppcompileh 

To compile the client type 

ppcompilec

2.1.2  WITHOUT LINUX ENVIRONMENT SET UP
----------------------------------------
To compile the client code you need to include the lwjgl.jar and lwjgl_util.jar
This can be done from the command line by navigating to the directory of the project 
and then executing the command:

javac -cp src:bin/lwjgl.jar:bin/lwjgl_util.jar -d build src/client/Main.java

Compiling the host does not require the lwjgl libraries, and can be done by 
navigating to the directory the project is in and running:

java -cp src -d build src/host/Main.java


2.2    FROM ECLIPSE
========================================
When including the project into eclipse it should recognize the jars and 
include them in the build path, but if not instructions for including them are included below:
Right clicking the project from the Package Explorer and selecting "Properties"
From here select "Java Build Path" on the left hand side, and then select the "Libraries" tab.
Click the Add JAR and add the bin/lwjgl.jar and bin/lwjgl_util.jar
If this does not work you can do the Add External JAR and give the absolute location to the JARs.

To run the code later you want to add the native libraries as well. 
If the code does not work as is, you have to add the native libraries yourself.
To do so, do the following for both JARs (lwjgl.jar and lwjgl_util.jar):
Expand the JAR options and select "Native library location". For the location enter:
For Linux users:

[PROJECT_NAME]/bin/native/linux

For Windows users:

[PROJECT_NAME]\bin\native\windows

For Mac users:

[PROJECT_NAME]/bin/native/macosx

where [PROJECT_NAME] should be the name of the project. 
You can also navigate to the location by selecting "Workspace..." and then navigating to 
bin->native->linux for linux users or 
bin->native->windows for windows users and 
bin->native->macosx for mac users.

3.    RUNNING CODE
________________________________________
3.1   FROM THE TERMINAL
========================================
3.1.1 WITH LINUX ENVIRONMENT SET UP
----------------------------------------
To run the client you can enter

ppclient

and to run the host you can enter

pphost

3.1.2  WITHOUT LINUX ENVIRONMENT SET UP
----------------------------------------
Navigate to the project directory and type

java -cp build:bin/lwjgl.jar:bin/lwjgl_util.jar -Djava.library.path=bin/native/linux client.Main

and to run the host simply type

java -cp build host.Main

3.2    FROM ECLIPSE
========================================
For the client select the Main.java in the client package and select "Run as Java Application"
For the host select the Main.java in the host package and select "Run as Java Application"

If this does not work, see the second half of Compiling the Code in 2.2 where it describes 
how to get the native libraries working.

4     THE CODE
________________________________________
4.1   GENERAL
========================================
This project is meant to be a virtual trading card game, similar to Magic: The Gather or Yu-Gi-Oh. There are 2 players, 
each that has a deck of custom cards.
Currently the objective of the game is to reduce the opposing player's life points to 0.
In any one game there is one of each for each player:
Deck (A facedown stack of the players not-yet-used cards)
Hand (The cards that the player can play)
Field (Where active cards are)
Grave (Where cards that have expired go)
Other (There might be need for more types of card collections)

Each card will serve as a buff or debuff for a player. Cards can be "instant" where they expire immediatly upon use, 
or can persist for a given amount of time. Some cards might help players a lot but only last a short period of time, 
while some may last a longer period of time, but not provide as useful of a buff. Example types of effects include:
"When a card deals fire damage, it deals 1 additional fire damage" or "When you draw a card, you gain one life"
There are a lot more details, and although this is pretty generic, the part that is interesting, to me at least, is
the duration part of the cards. A card that says that you gain 1 extra life per turn might last 5 turns, while a 
card that says you gain 2 life per turn might only last 2 turns. The vision of the project might change a lot as it 
goes, and I'm hoping that the framework for a card game in general is going to be extensible enough to handle almost 
any type of trading card game with only the need to change some rules and logic code in the project.


4.2   PACKAGE STRUCTURE
========================================
There are 3 packages within the src: client, model, and shared. The client package contains all of the code for the 
client to run. The host package contains all of the code for the host to run. The shared package contains code that 
is shared between the client and the host. For example the general behavior of the card at the lowest level is 
within the shared package. The parsing of xml is also in the shared package. If this is split into 2 projects, one 
for client and one for host, the shared would probably be a library that they both include.

4.2.1 CLIENT PACKAGE
----------------------------------------
The client follows an M-V-C pattern (Model-View-Control) in its package structure. The view package contains all of 
the lwjgl code, to make the window, display the game, etc. The model package contains the model as far as the client 
needs to see. This partial view does not know information about either person's deck, or the opposing person's hand. 
The control package contains networking code to send the request to the server.

4.2.2 HOST PACKAGE
----------------------------------------
The Host package structure also follows an M-V-C pattern, although it doesn't need a view, so it doesn't have a view 
package. The model for the host contains all information about the entire game. Nothing is hidden from the host, 
because it needs to see everything, and then only reports as much information as it needs to when it sends a client 
the game state. The control handles all of the logic for dictating what happens when a card is player, or a player 
changes their phase or ends their turn, etc. the control also has the networking set up to have a listener that 
listens for client requests, and then passes them off to handlers.

4.2.3 SHARED PACKAGE
----------------------------------------
The shared package package structure also follows the M-V-C, but has not view either. The model contains the shared 
base information about any model component. The control simply contains a Parser made to handle xml strings and dom 
elements.

5.    FINAL STUFF
If you notice any errors, have any advice/questions, want to help work on this project, or want to contact me for any 
other reason send me an email at quintenpalmer@gmail.com
Thanks for reading this README, and happy coding! :)
