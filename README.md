# COSC-3796-assignment-2
Screenshots from Super Mario game
SuperMario Bundled Malware Demonstration (COSC 3796)

This repository holds a teaching sample built for a security course, wherein a working copy of a SuperMario game written in Python also carries a second component that behaves the way bundled malware behaves outside the classroom. The aim of the exercise is awareness: a program can look and play like a normal game while another program runs in the background that the player never agreed to.

What is in the project

The game sits in the SuperMario folder and has the components you would expect from a small Python game: graphics, level maps, player data, and the source modules that run the levels. A packaged Windows executable is built from the Python source with a bundling tool, so that the whole thing ships as a single file a player can double-click.

The Server folder

The Server folder is the part that turns this sample into a demonstration rather than a plain game, since it holds the pieces that gather information and carry it off the machine. Inside it you find a small script called capture.py, a server program called server.py, a configuration file holding connection settings, a landing page, and a screenshots folder that fills up while the sample runs. The capture.py script takes pictures of the display at intervals, while server.py waits on the other side to receive those pictures and store them. The screenshots folder already holds a few timestamped sample images, which are the output this component produces once it has been left running for a short while.

How the game connects to capture.py

The teaching value lies in the way the two halves are joined together, in that the game’s startup routine does double duty: it begins the game the player wanted, and it quietly sets the capture script going in the background. Nothing on the screen announces the second task, so the player watches Mario load and starts playing without any prompt, consent screen, or visible window. A bundled executable hides the arrangement further, since the player receives a single file and has no easy way to notice the extra script tucked inside the package.

Warning signs a reviewer should notice

A handful of clues tend to give this kind of trick away before any harm reaches the machine, and a careful reader will catch most of them within a few minutes:

- A game that reaches for the internet when nothing about its play calls for an online feature.
- Extra folders carrying names such as server, capture, or upload, sitting right beside the ordinary game assets.
- A configuration file holding an address or a key that points somewhere outside the player’s own machine.
- Screenshot or log folders that grow on their own while the program is running in the background.
- A single packaged executable handed over without the matching source code that anyone can open and read.

Looking inside a bundle before trusting it

A little skepticism toward an unknown game bundle costs very little, and a few habits catch most of this problem before it reaches your files or your accounts. Running an unknown program inside a virtual machine or a throwaway account keeps it away from your real documents, your saved passwords, and the rest of your home network. Watching what the program does to the network while it runs will expose connections to places a game has no business talking to, and reading the source, when source comes with it, lets you see scripts that have nothing to do with gameplay sitting where they do not belong.

Defenses that prevent this pattern

Several plain protections blunt this kind of trick without asking much of the person playing the game. Antivirus and endpoint tools raise a flag on screen capture and silent uploads from something that presents itself as a game, since that behaviour matches known malware families. An operating system that asks permission before an app records the display or reaches the network gives the player a moment to refuse something that looks wrong. Downloading games only from stores and authors with a track record takes away most of the risk, since reputable channels screen what they let through.

Handling this sample

Keep this project away from a computer you rely on day to day, and hold it in a closed lab or a classroom machine set aside for the exercise. The .env file and the server piece are wired for a controlled setup, so point them at nothing real and clear the screenshots folder once the lesson is finished. The sample exists to teach people how to identify and shut down this behaviour, never to be aimed at anyone, which is the line that keeps security study within the law.
