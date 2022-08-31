"""
Contains Battle class and all it's methods to allow reading and creating player's armies to fight based on what
formation and then declare a winner or draw.
"""

__author__ = "Zaid"

from army import Army
from army import Fighter


class Battle:

    def gladiatorial_combat(self, player_one: str, player_two: str) -> int:
        """
        reads and creates an army for each player in the stack formation, then sets the armies using choose_army()
        then starts combat between both armies and returns the winner.
        :param player_one: Name of player1
        :param player_two: Name of player2
        :complexity: Best and worst is O(n) where n is the length of the Stack. Because when calling __conduct_combat
                     it will loop through all the elements in both armies till one of the armies is empty
        """
        army1 = Army()
        army2 = Army()
        army1.choose_army(player_one, 0)
        army2.choose_army(player_two, 0)

        return self.__conduct_combat(army1, army2, 0)

    def fairer_combat(self, player_one: str, player_two: str) -> int:
        """
        reads and creates an army for each player in the queue formation, then sets the armies using choose_army()
        then starts combat between both armies and returns the winner.
        :param player_one: Name of player1
        :param player_two: Name of player2
        :complexity: Best and worst is O(n) where n is the length of the Queue. Because when calling __conduct_combat
                     it will loop through all the elements in both armies till one of the armies is empty
        """
        army1 = Army()
        army2 = Army()
        army1.choose_army(player_one, 1)
        army2.choose_army(player_two, 1)

        return self.__conduct_combat(army1, army2, 1)

    def __conduct_combat(self, army1: Army, army2: Army, formation: int) -> int:
        """
        Conducts the combat based on formation of the two armies
        :param army1: Army object with a force of units within it
        :param army2: Army object with a force of units within it
        :param formation: The formation of the army (Stack or Queue)
        :return: returns an integer 0,1,2 indicating which player won or if it is a draw
        :complexity: Best and worst is O(n) where n is the length of queue or stack, it will loop through all the
        elements in both armies till one of the armies is empty
        """

        # step 4: at least one army is empty, end
        while not army1.force.is_empty() and not army2.force.is_empty():
            if formation == 0:
                # step 1: pop/serve units
                U1 = army1.force.pop()
                U2 = army2.force.pop()
            else:
                U1 = army1.force.serve()
                U2 = army2.force.serve()

            # step 2: attack & defend
            self.combat(U1, U2)

            # step 3: if alive push units back
            self.alive_units(U1, U2, formation, army1, army2)

        # Declaring a winner
        return self.result(army1, army2)

    def combat(self, U1: Fighter, U2: Fighter) -> None:
        """
        Implements the second step of Attacking and defending between 2 units of opposite armies.
        Created in a separate method to avoid duplicate code in both formations.
        :param U1: Unit from army1
        :param U2: Unit from army2
        :complexity: Best and worst is O(1), because just if statements, comparing and changing values, which are
                     all constant time operations
        """
        # step 2: attack & defend
        # when U1 is faster than U2
        if U1.get_speed() > U2.get_speed():
            U2.defend(U1.get_attack_damage())
            if U2.is_alive():
                U1.defend(U2.get_attack_damage())

        # when U2 is faster than U1
        elif U2.get_speed() > U1.get_speed():
            U1.defend(U2.get_attack_damage())
            if U1.is_alive():
                U2.defend(U1.get_attack_damage())

        # U1 and U2 have equal speed
        else:
            U1.defend(U2.get_attack_damage())
            U2.defend(U1.get_attack_damage())

    def alive_units(self, U1: Fighter, U2: Fighter, formation: int, army1: Army, army2: Army) -> None:
        """ Implements if a unit can be pushed back into stack only if it is alive.
        :param U1: Unit1
        :param U2: Unit2
        :param formation: Stack
        :param army1: player1's army
        :param army2: player2's army
        :complexity: best and worst O(1) only constant operations, if statements
        """        
        # if both alive, lose_life(1) and append back for both
        if U1.is_alive() and U2.is_alive():
            U1.lose_life(1)
            U2.lose_life(1)

        # if still alive after both losing life
        if U1.is_alive() and U2.is_alive():
            if formation == 0:
                army1.force.push(U1)
                army2.force.push(U2)
            else:
                army1.force.append(U1)
                army2.force.append(U2)

        # if U1 alive and U2 is not, U1 gain's experience
        elif U1.is_alive() and not U2.is_alive():
            U1.gain_experience(1)
            if formation == 0:
                army1.force.push(U1)
            else:
                army1.force.append(U1)

        # if U2 alive and U1 is not, U2 gain's experience
        elif U2.is_alive() and not U1.is_alive():
            U2.gain_experience(1)
            if formation == 0:
                army2.force.push(U2)
            else:
                army2.force.append(U2)

    def result(self, army1: Army, army2: Army) -> int:
        """
        Determines the result of the game, which player won or if its a draw and returns the winner
        :param army1: player1's army
        :param army2: player2's army
        :complexity: Best and worst is O(1), if statements and then returning an integer
        """
        draw = 0
        player1Win = 1
        player2Win = 2

        if army2.force.is_empty() and army1.force.is_empty():
            return draw

        # Player1's army won
        elif army2.force.is_empty():
            return player1Win

        # Player2's army won
        else:
            return player2Win

