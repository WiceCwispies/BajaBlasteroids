import numpy as np
import sys
from fuzzy_tools import CustomFIS
from fuzzy_asteroids.fuzzy_asteroids import AsteroidGame, FuzzyAsteroidGame
from HeiTerryController import FuzzyController
from fuzzy_asteroids.fuzzy_asteroids import TrainerEnvironment
from sample_score import SampleScore


def AsteriodFitness(chrom, game):
    score = game.run(controller=FuzzyController(chrom), score=SampleScore())
    return score.fitness
