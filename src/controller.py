from typing import Tuple, Dict, Any, List

from fuzzy_asteroids.fuzzy_controller import ControllerBase, SpaceShip


class FuzzyController(ControllerBase):
    """
    Class to be used by UC Fuzzy Challenge competitors to create a fuzzy logic controller
    for the Asteroid Smasher game.

    Note: Your fuzzy controller class can be called anything, but must inherit from the
    the ``ControllerBase`` class (imported above)

    Users must define the following:
    1. __init__()
    2. actions(self, ship: SpaceShip, input_data: Dict[str, Tuple])

    By defining these interfaces, this class will work correctly
    """
    def __init__(self):
        """
        Create your fuzzy logic controllers and other objects here
        """
        super().__init__()
        
    def name(self):
        return "Baja"
        

    def actions(self, ships: List[SpaceShip], input_data: Dict[str, Tuple]) -> None:
        """
        Compute control actions of the ship. Perform all command actions via the ``ship``
        argument. This class acts as an intermediary between the controller and the environment.

        The environment looks for this function when calculating control actions for the Ship sprite.

        TODO populate this function with your fuzzy-AI behavior.

        Follow good OOP/functional programming practices and don't make this 400 lines long.
        Split up functionality into to make your code more legible, understandable, debuggable.

        :param ships: Object to use when controlling the SpaceShip
        :param input_data: Input data which describes the current state of the environment
        """
        
        # for ship in ships:
        #ships.turn_rate = 23
        #ships.thrust = ships.thrust_range[0.5]
        #print("x")
        print(input_data)
        #print(input_data['asteroids'][0]['position'][0])
        if abs(ships.position[0] - input_data['asteroids'][0]['position'][0]) <= 50:
            ships.shoot()
            print("he")
        



    """

    Ship Logic 

    Get Information about the State of the Game

    Decide on a target to shoot at

    Aim

    Shoot

    """

