# README: Tic Tac Toe AI with Minimax Algorithm

## Overview

This project implements an intelligent Tic Tac Toe game using Python, designed for a graduate program at the University of Michigan. The game features a graphical user interface (GUI) powered by Pygame and employs the Minimax algorithm to enable an AI opponent that plays optimally. This README provides essential information on setting up the game environment, running the game, and a brief theoretical background on the game theory principles underlying the AI's strategy.

## Installation and Setup

### Dependencies

To run this Tic Tac Toe game, you will need Python 3 and Pygame. Ensure Python 3.10 or newer is installed on your system. Pygame is a cross-platform set of Python modules designed for writing video games, providing functionalities for creating visually engaging games.

### Setting Up the Environment

1. **Install Pygame**: The project dependencies, including Pygame, can be easily installed using the `requirements.txt` file. Open a terminal or command prompt, navigate to the project directory where `requirements.txt` is located, and run the following command:

```bash
pip install -r requirements.txt
```

This command installs all the necessary Python packages listed in `requirements.txt`, setting up your environment for running the Tic Tac Toe game.

### Downloading the Game

- #### GitHub

```bash
git clone <repository-url>
```

- #### Zip file

Download and extract the project files to a local directory on your machine and open the project in your code editor of choice.

## Running the Game

Navigate to the game directory where you've saved the project files. Run the game using Python by executing the following command in your terminal or command prompt:

```bash

python runner.py

```

This command launches the game's GUI, where you can play against the AI opponent.

## Background Information

### Game Theory

Game theory is a mathematical framework for analyzing strategies in competitive situations where the outcome of a participant's choice of action depends on the actions of other participants. Tic Tac Toe, while simple, serves as an illustrative example of game theory applied to AI.

### Minimax Algorithm

The Minimax algorithm is a decision rule for minimizing the possible loss while maximizing the potential gain. Applied to Tic Tac Toe, it involves simulating all possible moves in the game (for both the AI and its opponent), creating a game tree that represents these moves, and choosing the move that leads to the best possible outcome for the AI, assuming optimal play by the opponent.

The algorithm recursively examines the game tree, alternating between minimizing and maximizing the utility of the board states, which represent the desirability of those states to the AI. The utility is usually expressed in terms of game outcomes: a win, loss, or draw, with values like 1, -1, and 0, respectively.

- **Maximizing Player (AI)**: Aims to maximize the score, seeking moves that lead toward victory.
- **Minimizing Player (Opponent)**: Aims to minimize the score, blocking the AI's winning strategies and steering the game towards a draw or a win for themselves.

### Utility Function

The utility function assesses the value of terminal states, with 1 for a win, -1 for a loss, and 0 for a draw. By examining these terminal states, the Minimax algorithm decides on the optimal moves to either secure a victory or prevent a defeat.

## Additional Features

- **Graphical User Interface**: The GUI, developed with Pygame, provides a visually engaging way to play Tic Tac Toe.
- **AI Opponent**: The Minimax algorithm ensures that the AI opponent plays optimally, making the game challenging and educational.
- **Game Reset**: Players can easily start a new game after each round, facilitating continuous play and strategy experimentation.

## Contributing

Contributions to this project are welcome. Whether it's suggesting improvements, reporting bugs, or enhancing the AI strategy, your input is valuable. Please visit the [Pygame community contribution page](https://www.pygame.org/contribute.html) for guidelines on contributing to projects using Pygame.

## License

This project is open-source and available under the MIT License.
