# YAZY Simulation Architecture Reference

## Philosophy

A production-grade simulation is not just a game. It is a simulation
platform composed of independent layers.

------------------------------------------------------------------------

## Layer 1 -- Game Engine

Responsible only for the rules of the game.

-   Board
-   Dice
-   ScoreCard
-   Turn
-   Rules

It should answer questions like: - Is this move legal? - How many points
does this category give?

It should **not** know anything about AI or simulations.

------------------------------------------------------------------------

## Layer 2 -- Game State

Store the entire game inside one object.

``` python
class GameState:
    board
    scorecard
    dice
    turn
```

Benefits: - Easy copying (`deepcopy`) - Save/load games - Debugging -
Simulation branching

------------------------------------------------------------------------

## Layer 3 -- Policies (Players)

A policy answers:

> Given the current game state, what action should I take?

Examples:

-   HumanPlayer
-   RandomPolicy
-   GreedyPolicy
-   Monte Carlo Tree Search
-   Reinforcement Learning Agent

The game engine should never know which policy is playing.

------------------------------------------------------------------------

## Layer 4 -- Simulation Runner

Responsible for running many games.

``` python
for _ in range(100000):
    game = Game()
    score = game.play(RandomPolicy())
```

The runner collects results but does not implement game rules.

------------------------------------------------------------------------

## Layer 5 -- Analytics

Instead of printing one score:

``` python
scores.append(score)
```

Analyse:

-   Mean
-   Median
-   Variance
-   Histograms
-   Win rates
-   Strategy comparisons

------------------------------------------------------------------------

## Layer 6 -- Parallelism

Large simulations should run in parallel.

Instead of:

``` text
100000 games sequentially
```

use multiprocessing to distribute work across CPU cores.

------------------------------------------------------------------------

## Layer 7 -- Reproducibility

Every simulation should accept a random seed.

``` python
Game(seed=42)
```

Benefits:

-   Repeat experiments
-   Easier debugging
-   Scientific comparisons

------------------------------------------------------------------------

## Layer 8 -- Logging

Store structured logs instead of print statements.

Example:

``` json
{
    "game": 1832,
    "policy": "Greedy",
    "score": 254,
    "rolls": 53,
    "time": 0.008
}
```

------------------------------------------------------------------------

## Layer 9 -- Experiment Manager

High-level API:

``` python
run(policy=Greedy, games=100000)
```

or

``` python
run(policy=RLAgent, games=1000000)
```

Compare strategies automatically.

------------------------------------------------------------------------

# Suggested YAZY Architecture

``` text
Game
│
├── Dice
├── Player
├── ScoreCard
├── Rules
├── TurnManager
├── GameState
│
├── Strategy
│     ├── HumanPlayer
│     ├── RandomAI
│     ├── GreedyAI
│     └── RLAgent
│
├── Simulator
│
└── Statistics
```

## Responsibilities

-   **Rules**: Implements the game's logic.
-   **Game**: Orchestrates one game.
-   **Simulator**: Runs many games.
-   **Strategy**: Decides moves.
-   **Statistics**: Analyses outcomes.

Each class should have one clear responsibility.

------------------------------------------------------------------------

# Long-Term Vision

Instead of building only a playable game, build a simulation platform.

Possible research questions:

-   Which strategy performs best?
-   What is the expected score of each decision?
-   Which category should be prioritized?
-   Can an RL agent outperform a greedy heuristic?
-   How many simulations are needed for statistically significant
    conclusions?

This architecture keeps the code modular, testable, and extensible,
making it suitable for AI experiments and future features.
