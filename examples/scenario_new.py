# -*- coding: utf-8 -*-

import time

from kesslergame import Scenario, KesslerGame, GraphicsType
from src.FuzzyController import FuzzyController


my_test_scenario = Scenario(name='Test Scenario',
                            num_asteroids=10,
                            ship_states=[
                                {'position': (400, 400), 'angle': 90, 'lives': 3, 'team': 1},
                                {'position': (400, 600), 'angle': 90, 'lives': 3, 'team': 2},
                            ],
                            map_size=(1000, 800),
                            time_limit=60,
                            ammo_limit_multiplier=0,
                            stop_if_no_ammo=False)


game_settings = {'perf_tracker': True,
                 'graphics_mode': GraphicsType.Tkinter,
                 'realtime_multiplier': 1}
game = KesslerGame(settings=game_settings)  # Use this to visualize the game scenario
# game = TrainerEnvironment(settings=game_settings)  # Use this for max-speed, no-graphics simulation

pre = time.perf_counter()
score, perf_data = game.run(scenario=my_test_scenario, controllers = [FuzzyController(), FuzzyController()])

print('Scenario eval time: '+str(time.perf_counter()-pre))
print(score.stop_reason)
print('Asteroids hit: ' + str([team.asteroids_hit for team in score.teams]))
print('Deaths: ' + str([team.deaths for team in score.teams]))
print('Accuracy: ' + str([team.accuracy for team in score.teams]))
print('Mean eval time: ' + str([team.mean_eval_time for team in score.teams]))