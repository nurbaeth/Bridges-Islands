# Bridges & Islands

## Overview
**Bridges & Islands** is a logic puzzle game where players connect islands with bridges according to specific rules. Each island has a number indicating how many bridges must be connected to it. Bridges can only be horizontal or vertical and cannot cross each other. Solve increasingly challenging levels by strategically linking all islands!

## Features
- Procedurally generated islands with randomized bridge requirements
- Simple and clean grid-based visuals
- Interactive bridge-drawing mechanics (coming soon)
- Developed using Python and Pygame

## Installation
### Prerequisites
- Python 3.8+
- Pygame library
 
### Install Dependencies
```bash 
pip install pygame
```

### Run the Game
```bash
python bridges_game.py
```

## How to Play
1. Islands are displayed on the grid, each marked with a number.
2. Your goal is to connect islands using bridges while following the rules:
   - Bridges must be horizontal or vertical.
   - Bridges cannot cross each other.
   - Each island must have the exact number of bridges shown.
3. Click and drag between islands to create bridges (feature in development).
4. Complete all connections to solve the puzzle!

## Roadmap
- [x] Generate islands with randomized positions and bridge counts
- [ ] Implement interactive bridge-drawing
- [ ] Add win condition detection
- [ ] Introduce different difficulty levels
- [ ] Enhance UI with animations and sound effects

## Contributing
Contributions are welcome! Feel free to open issues and pull requests to improve the game.

## License
This project is licensed under the MIT License. See `LICENSE` for details.
