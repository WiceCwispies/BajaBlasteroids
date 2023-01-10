from kesslergame import KesslerController
from typing import Dict, Tuple


class FuzzyController(KesslerController):
    def __init__(self) -> None:
        super().__init__()

    def actions(self, ship_state: Dict, game_state: Dict) -> Tuple[float, float, bool]:
        """
        Method processed each time step by this controller.
        """

        thrust = 0
        turn_rate = 50
        fire = True

        return thrust, turn_rate, fire

    @property
    def name(self) -> str:
        return "BajaBlasteroids"