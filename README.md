# RL-Projekt
This is a project made by 5 students which are participating in the course 02465: Introduction to reinforcement learning and control at the Technical University of Denmark. The code is greatly inspired by Rafael Mosca's (rfma23) repository https://github.com/rfma23/ChessAI.

## Code Documentation - Overview of Re-used Code in the project:
In the following we give an overview of what code we wrote ourself and what code is inspired by external sources. The general trend is that the implementation of the algorithm is taken from Rafael Mosca's (rfma23) repository which is in the format of a python-notebook and refit to be classes with methods implemented in a main script. **The remainder of the script-files in this folder is original work**

### Within the folder "ScriptImplementation":
- ```alphaBetaSearch.py``` - The specific implementation of the alpha beta search algorithm is taken from Rafael Mosca's (rfma23) repository and fitted the specifics regarding our project.
- ```chessEnvironment.py```-  Inspired from Rafael Mosca's (rfma23) repository and fitted the specifics regarding our project, making it a function that plays a set of chess.
- ```gui.py```- The implementation of a graphic userfase. Taken from Devin Alvaro’s (devinalvaro) repository (https://github.com/devinalvaro/yachess/blob/master/src/gui.py) and fitted to work with the rest of the code in our project.
- ```guiGame.py```- The implementation of a graphic userfase. Taken from Devin Alvaro’s (devinalvaro) repository and fitted to work with the rest of the code in our project.
- ```minimaxAgent.py``` - The implementation of the minimax agent itself. This is multiple elements from Rafael Mosca's (rfma23) repository combined into an agent.
- ```staticBoardEvaluation.py``` - The board evaluation heuristics used to evaluate the bord if not the stockfish engine is used. This is taken directly from  Rafael Mosca's (rfma23) repository and made into a class with a lookup table which the minimaxAgent uses together with the alpha beta pruning algorithm.

## Installing the environment:
For the project, we used python 3.8.4. The used libraries can be found in requirements.txt

## Making the code work:
In the ```main.py``` script, please change the ```path```variable to the folder where the stockfish engine is stored on you system. Furthermore, when initializing the stockfish engine, remember to change the name to the stockfish engine stored on your system. A stockfish engine for linux, mac and windows are included in the "ScriptImplementation" folder.

## Code Workings:
In the following we give a brief overview of the functionality of each script in the "ScriptImplementation" folder.
- `alphaBetaSearch.py` - The specific implementation of the alpha-beta search algorithm
- `chessEnvironment.py` - The environment that controls how the game is played with a 'play_game()' function, including keeping track of the turn and score.
- `getScores.py` - Calculation of Elo-rate (old way).
- `gui.py` - Implementation of the GUI that allows a human player to play against the chess-engine.
- `guiGame.py` - Implementation of the GUI that allows a human player to play against the chess-engine.
- `main.py` - The main script.
- `main_while.py` - Main script for playing games until win.
- `minimaxAgent.py` - The specific implementation of the agent, including the ability to evaluate the board and make a move.
- `staticBoardEvaluation.py` - The heuristics of the board used for evaluaiton by the agent.
- `stockfishAgent.py` - The stockfish agent chess player.
- `rl_proj_eval.py`(Found in the parent folder to "ScriptImplementation")

### "data_results" folder
The reconstructed dataframes used for the final results-plot.
### "raw_results" folder
All results obtained when running the experiment.
