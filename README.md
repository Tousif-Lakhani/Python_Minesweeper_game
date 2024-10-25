# Minesweeper Game
This project is a Python implementation of the classic Minesweeper game. It features a customizable game board where players reveal squares to avoid mines, using logic to deduce the locations of hidden mines. The game is played via the terminal, and it includes functionalities like mine flagging, board size customization, and adjustable mine count.

# Overview
Minesweeper is a logic-based game where players reveal squares on a grid, attempting to avoid mines that are hidden within it. With each revealed square, the game indicates the number of adjacent mines, giving clues to the player. The goal is to reveal all squares without hitting a mine.

This Python version allows players to define the board size and number of mines, making it adaptable for different difficulty levels.

# Gameplay

1 - The player defines the board size and the number of mines to be placed.

2 - The game randomly places mines across the board.

3 - The player reveals squares by entering coordinates (e.g., A1).

4 - If a square contains a mine, the game ends. Otherwise, the game displays the count of adjacent mines.

5 - Players can flag potential mine locations by typing F followed by the square coordinates.

6 - The game ends when:
- All non-mine squares are revealed (Win)
- A mine is revealed (Lose)

# Features
- Customizable Board: Players can define the board size and number of mines.
- Recursive Square Reveal: If a square has no neighboring mines, the surrounding squares are automatically revealed.
- Flagging Mechanism: Players can flag squares they suspect contain mines.
 - User-Friendly Board Display: The board shows clear grid coordinates, making navigation easier.

# Setup
1 - Clone the Repository:
```
git clone https://github.com/Tousif_Lakhani/minesweeper-game.git
cd minesweeper-game
```
2 - Run the Game:
- Open your terminal and navigate to the project directory.
- Start the game by running:
```
python minesweeper.py
```
# Game Design
The game is built with modular functions for clarity and reusability:

1 - **create_board and create_uboard**: Initialize the solution and user boards.

2 - **place_mines**: Randomly places mines on the solution board based on user-defined parameters.

3 - **total_mines_around**: Calculates the number of mines around a selected square.

4 - **reveal_square**: Recursively reveals squares with zero adjacent mines until a square with mines around it is reached.

5 - **flag_square**: Flags or unflags a chosen square as a suspected mine.

6 - **print_board**: Displays the current user board in a clear, user-friendly format.

7 - **start_game**: Manages game flow, including user input, win/loss conditions, and replay options.

# Usage
1 - Define Game Parameters:

- Enter the board size (e.g., 8 for an 8x8 board).
- Define the number of mines (e.g., 10).

2 - Gameplay Commands:

- Reveal a Square: Enter a square by typing its coordinates (e.g., A1).
- Flag a Square: Type F and then the coordinates of the square (e.g., F A1).
- The game provides feedback, including mine counts for revealed squares and updates on flagged squares.

3 - Winning/Losing:

- Avoid all mines and reveal all safe squares to win.
- If you reveal a mine, the game ends, and the full solution board is displayed.

#
Enjoy playing Minesweeper, and thank you for exploring this project!
