#MINI TREASURE HUNT GAME
A simple desktop treasure hunt game developed using Python and Tkinter. The player moves across a randomly generated map to find the hidden treasure.

##Features:

-Randomly generated map

-Objective:Find the treasure

-Trap system

-Hint system

-Grid-based player movement

-Graphical user interface(Tkinter)

##Technologies Used

-Python

-Tkinter(for GUI)

-Random module

##Installation & Run

###Clone the repository

-git clone https://github.com/your-username/mini-treasure-hunt-game.git

###Navigate to the project folder

-cd mini-treasure-hunt-game

###Run the game

-python main.py

##Project Structure
```bash
mini-treasure-hunt-game/
│── main.py        # Entry point of the application
│── gui.py         # Tkinter GUI (Game interface)
│── game.py        # Core game logic
│── map.py         # Map generation system
│── player.py      # Player movement and state
```
##How to Play

-The players start at position(0,0)

-Move using directional controls

-Your goal is find the hidden treasure

-Be careful

  -Traps can edn the game
  
  -Hints can guide you

##Game Logic

-The map is randomly generated at each run map.py

-Player movement is restricted within boundaries player.py

-Game rules and flow are handled in game.py

-The interface is managed via gui.py

##Games Screenshot

<img width="1918" height="1020" alt="Ekran görüntüsü 2026-04-20 150640" src="https://github.com/user-attachments/assets/c222206e-29a8-4c93-9b60-23ebdb672d72" />


##Future Improvements

-Score system improvements

-Level system

-Larger maps

-Sound effects

-Save/Load feature

##Licence

-MIT licence





