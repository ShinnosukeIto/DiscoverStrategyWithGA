import numpy as np
from geneticalgorithm import GA


def simulate(individual):
  score = 0
  strategy = np.array(list(map(lambda x: 'H' if x == 0 else 'S', individual))).reshape(10, 28)
  #ゲームのシミュレート

  return score

def search():
  ga = GA(70, 10000, 0.85, 0.25, 280)
  ga.Solve(simulate)