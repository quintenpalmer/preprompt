README for PostPrompt!

1.     ENVIRONMENT SETUP
------------------------------
Some simple environment can be done to run the code the same way I do.
If you are running linux, edit your bashrc (or similar file) to include the following 2 lines:

export postprompt="/PATH/TO/PROJECT/DIRECTORY"
export PATH=$postprompt/bin:$PATH

and replacing /PATH/TO/PROJECT/DIRECTORY with whatever the path to the directory that 
contains this project (in linux/mac this can be found by navigating to the project directory and entering the command pwd
in windows this can be done by going to the directory of the project and typing  the command cd )

2.     COMPILING CODE
------------------------------
2.1    FROM THE LINUX TERMINAL
2.1.1  WITH LINUX ENVIRONMENT SET UP
Simply enter 

ppcompile 

to compile both the host and the client
To compile only the host type 

ppcompileh 

and to compile the client type 

ppcompilec

2.1.2  WITHOUT LINUX ENVIRONMENT SET UP
To compile the client code you need to include the lwjgl.jar and lwjgl_util.jar
This can be done from the command line by navigating to the directory of the project 
and then executing the command:

javac -cp src:bin/lwjgl.jar:bin/lwjgl_util.jar -d build src/client/Main.java

Compiling the host does not require the lwjgl libraries, and can be done by running:

java -cp src -d build src/host/Main.java

from the directory the project is in.

2.2    FROM ECLIPSE
When including the project into eclipse it should recognize the jars and 
include them in the build path, but if not instructions for including them are included below:
Right clicking the project from the Package Explorer and selecting "Properties"
From here select "Java Build Path" on the left hand side, and then select the "Libraries" tab.
Click the Add JAR and add the bin/lwjgl.jar and bin/lwjgl_util.jar
If this does not work you can do the Add External JAR and give the absolute location to the JAR's.

3.    RUNNING CODE
------------------------------
3.1   FROM THE LINUX TERMINAL
3.1.1 WITH LINUX ENVIRONMENT SET UP
To run the client you can enter

ppclient

and to run the host you can enter

pphost

3.1.2  WITHOUT LINUX ENVIRONMENT SET UP
Navigate to the project directory and type

java -cp build:bin/lwjgl.jar:bin/lwjgl_util.jar -Djava.library.path=bin/native/linux client.Main

and to run the host simply type

java -cp build host.Main

3.2    FROM ECLIPSE
For the client select the Main.java within the client package and select Run Configurations.
Within the "(x)= Arguments" tab enter the one of the following into VM arguments depending on your operating system:

3.2.1 FOR WINDOWS

-Djava.library.path=bin/native/windows

3.2.2 FOR LINUX

-Djava.library.path=bin/native/linux

3.2.3 FOR MAC

-Djava.library.path=bin/native/macosx

4.    FINAL STUFF
If you notice any errors, or have any advice, or want to help work on this project, or want to contact me for any other reason send me an email at quintenpalmer@gmail.com
