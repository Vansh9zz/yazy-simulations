import pandas as pd

from simulation.simulation import Simulation
from players.random_player import RandomPlayer

sim = Simulation(RandomPlayer())
sim.run(1000)

df = sim.logger.summary

print(df.head())

