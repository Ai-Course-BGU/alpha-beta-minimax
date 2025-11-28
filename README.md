# IsoKnight AI Agent ♞

[cite_start]This repository contains the solution for **Assignment 2: Games** in the *Introduction to Artificial Intelligence* course (Winter 2026)[cite: 2, 3, 4].

## 📋 Overview
The project involves implementing AI agents to play a two-player adversarial game called **IsoKnight**. [cite_start]The goal was to implement search algorithms such as **Minimax** and **Alpha-Beta Pruning**, along with designing heuristic evaluation functions to solve game states on varying board sizes[cite: 41, 47].

## 🎮 The Game: IsoKnight
IsoKnight is played on an $m \times n$ grid. Two players control a "Knight" character starting at specific locations.

### Rules
1.  [cite_start]**Movement:** Players take turns moving their character exactly like a Knight in Chess (L-shape: 2 steps one direction, 1 step perpendicular)[cite: 23, 26].
2.  **Constraints:**
    * [cite_start]A character **cannot** land on a square that has been visited previously[cite: 25].
    * [cite_start]A character **can** jump over visited squares or the opponent's piece[cite: 25, 30].
3.  **Objective:** The game ends when a player cannot make a legal move. [cite_start]The last player able to move wins (or conversely, the player unable to move loses)[cite: 44].

![IsoKnight Moves](path/to/your/image.png)
*(Note: You can include the screenshot of the legal moves from Page 2 of the assignment PDF here)*

## 🧠 Algorithms Implemented

### 1. Alpha-Beta Pruning
* **File:** `alpha_beta_isoKnight.py`
* **Description:** An optimization of the Minimax algorithm that prunes branches of the game tree that do not influence the final decision. [cite_start]This implementation calculates the **Maximin** value of the game[cite: 47, 48].
* **Key Feature:** Implements distinct handling for maximizing and minimizing players while maintaining the state of visited squares.

### 2. Heuristic Alpha-Beta (Depth-Limited)
* **File:** `heuristic_alpha_beta_isoKnight.py`
* **Description:** To handle larger board sizes (larger than $5 \times 5$), this version limits the search depth. [cite_start]When the search cut-off is reached, a heuristic function estimates the value of the state[cite: 53, 55, 63].

### 3. Heuristics
* **File:** `heuristics.py`
* **Base Heuristic:** Calculates the difference between the number of legal moves available to Player 1 and Player 2:
    $$h(s) = \text{moves}(P1) - \text{moves}(P2)$$
    [cite_start][cite: 56, 57].
* [cite_start]**Advanced Heuristic:** A custom strategy designed for tournament play to optimize win rates on complex boards[cite: 58].

## 📂 File Structure

| File Name | Description |
| :--- | :--- |
| `alpha_beta_isoKnight.py` | [cite_start]Implementation of Alpha-Beta Pruning algorithm[cite: 11]. |
| `heuristic_alpha_beta_isoKnight.py` | [cite_start]Implementation of Alpha-Beta with depth limit and heuristics[cite: 12]. |
| `heuristics.py` | [cite_start]Contains `base_heuristic` and `advanced_heuristic` functions[cite: 10]. |
| `minimax_isoKnight.py` | [cite_start]Basic Minimax implementation (Base for Alpha-Beta)[cite: 8]. |
| `game_engine.py` | [cite_start]The main engine that runs the game logic[cite: 14]. |
| `game_state.py` | [cite_start]Manages the state representation of the board[cite: 13]. |
| `player_agent.py` | [cite_start]Interface for the player agents[cite: 9]. |

## ⚙️ Installation & Requirements
The project is written in **Python**.
[cite_start]You must install the `numpy` package to run the code[cite: 19].

```bash
pip install numpy
