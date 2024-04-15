# AwakeningTrackerApp

## INSTRUCTIONS FOR THE GENERAL PUBLIC

Clicking this link to see the latest release of the executable. just download the executable (it's named 'AwakeningTracker.exe'). the compressed files won't give you what you want.
https://github.com/PissMidas/AwakeningTrackerApp/releases

if you need technical help, please go to https://discord.com/channels/780470426010255380/1119008450689634346/1119008450689634346 which is a post in the main omega strikers discord.

No installation required!

## INSTRUCTIONS FOR PEOPLE WHO WANT TO COMPILE OR DEVELOP THIS REPO
these instructions are for either:

-you are interested in building and compiling the files yourself (security concerns)

-developing the app further

-looking at the source code for a similar personal project.

-etc.

1. download this repo (the 'images' folder, and the file 'tk.py'. keep the structure the same as you see it in this repo)
2. pip install the relevant libraries (whatever warnings that pop up)
3. go to your local folder via the command prompt. if you do not want to compile, then simply type 'python tk.py' and press enter.
4. if you want to compile the app into a single executable file, type
   
   pyinstaller --onefile --icon=images/dubu.ico --add-data "images;images" --noconsole --name "AwakeningTracker" tk.py

   and then press enter.
6. i recommend disabling the 'check if omega strikers is open' code if you want to test simple changes.

If you are trying to develop software to be used alongside the game, dm me. I love hearing about new projects, even if it's just in the planning stages!

### Version history
6/15/2023 v0.0.1 release!

6/16/2023 v0.0.2 fixed edge case async behavior conflicting with each other. (gui and game event observer startup were overlapping/conflicting)

6/16/2023 v0.0.3 app is no longer compressed. compression is a common technique for viruses to infiltrate and obfuscate themselves. antivirus scans should have an easier time analyzing this app (and no longer triggering a false positive).

7/13/2023 v0.0.4 Micropatch! Rotated Out: Spark of Focus, Strength, Resilience, and Agility. Rotated In: Perfect Form, One-Two Punch, Stagger Swagger, Prize Fighter

9/7/2023 v0.0.5 Micropatch! Rotated Out: Orbs (Orb Dancer, Orb Ponderer, Orb Replicator) and Glass Cannon
ROTATED IN: Sparkington City (Spark of Strength, Spark of Agility, Spark of Focus, Spark of Resilience)

10/19/2023 v0.0.6 Patch. Rotated Out: Catalyst, Fire Up!, Rapid Fire
Rotated in: Fight or Flight, Knife's Edge, Demolitionist

10/19/2023 v0.0.7 Micropatch! Rotated Out: Demolitionist
Rotated in: Glass Cannon

11/16/2023 v0.0.8 Micropatch! Rotated out: Tempo Swing, Bulk up, Reverberation
Rotated in: Orb Dancer, Orb Ponderer, Orb Replicator

Also started to use the 'releases' page of github to release the executable. nothing has changed significantly, just follow the instructions at the top of this readme.

11/30/2023 v0.0.9 Patch. Rotated out: Orb Ponderer, Orb Dancer,  Orb Replicator, Stacks on Stacks 
Rotated in: Among Titans, Team Player, Spark of Leadership, Demolitionist

11/30/2023 v0.0.10 Patch. Rotated out: Spark of Leadership
Rotated in: Reverberation

12/15/2023 v0.0.11 Micropatch. Rotated out: Perfect Form
Rotated in: Rapid Fire

2/14/2024 v0.0.12 Patch. Rotated out: Super Surge, Big Fish, Peak Performance, Reverberation, Egoist
Rotated in: Spark of Leadership, Recovery Drone, Explosive Entrance, Siege Machine, Unstoppable


4/12/2024 v0.0.13 Patch. Rotated out: Spark of Strength, Spark of Agility, Spark of Focus, Spark of Resilience, Spark of Leadership, Built Different, Stagger Swagger, Fight or Flight, Glass Cannon
Rotated in: Reptile Remedy, Might of the Colossus, Rampage, Stinger, Adrenaline Rush, Stacks on Stacks, Peak Performance, Bulk Up, Reverberation



4/14/2024 v0.0.14 Now shows what team you are on.currently testing functionality
