"""
Contains the abstract class Fighter and its abstract and non-abstract methods. Also contains Soldier, Archer, and
Cavalry classes with their methods. The Army class is responsible for inputting the values of units of each army and
then, setting each army in a stack or queue.

"""
__author__ = "Zaid"

from abc import ABC, abstractmethod
from stack_adt import ArrayStack
from queue_adt import CircularQueue


class Fighter(ABC):
    def __init__(self, life: int, experience: int) -> None:
        """ initialises the variables using the amounts received as input.
        :param life: Life points of the fighter
        :param experience: Experience points of the fighter
        :pre: life and experience >= 0
        :raises ValueError: if life or experience >= 0
        :complexity: Best and worst is O(1) Because just assigning value to instance variables.
        """
        if life < 0 or experience < 0:
            raise ValueError("Values of life and experience must be positive numbers")

        self.life = life
        self.experience = experience

    def is_alive(self) -> bool:
        """ Return if the fighter’s life is greater than 0, False otherwise.
        :complexity: Best and worst is O(1) because just comparing values between 2 integers.
        """
        if self.life > 0:
            return True
        else:
            return False

    def lose_life(self, lost_life: int) -> None:
        """ Decreases the life of the unit by the amount indicated by lost life.
        :param lost_life: Value to subtract from the current fighter's life points.
        :pre: lost_life must be >= 0
        :raises ValueError: if lost_life < 0
        :complexity: best and worst is O(1) because just comparing int value and then subtracting self.life
                     by an int provided by lost_life
        """
        if lost_life < 0:
            raise ValueError("lost_life cannot be a negative integer")
        self.life -= lost_life

    def get_life(self) -> int:
        """
        Returns the current fighter's life integer value.
        :complexity: best and worst O(1) because just returning an integer
        """
        return self.life

    def gain_experience(self, gained_experience: int) -> None:
        """
        increases the experience of the fighter by the amount indicated by gained experience
        :param gained_experience: Value to add to current fighter's experience points.
        :pre: value >= 0
        :raises: ValueError if negative value
        :complexity: Best and worst is O(1) because just adding and assigning integers
        """
        if gained_experience < 0:
            raise ValueError("gained experience cannot be a negative integer")
        self.experience += gained_experience

    def get_experience(self) -> int:
        """returns the current fighter's experience value
        :complexity: best and worst is O(1), just returning an integer
        """
        return self.experience

    @abstractmethod
    def get_speed(self) -> int:
        """returns the current fighter's speed."""
        pass

    def get_cost(self) -> int:
        """returns the current fighter's cost. """
        pass

    @abstractmethod
    def get_attack_damage(self) -> int:
        """returns damage performed by the Fighter when it attacks. """
        pass

    @abstractmethod
    def defend(self, damage: int) -> None:
        """
        Evaluates the current fighter's life lost after defence inflicted by the amount of damage
        indicated by the damage parameter.
        :param damage: Value of damage that wil reduce the defender's life points
        :pre: damage >= 0
        :raises ValueError: if damage is a negative value
        :complexity: Best and worst is O(1), only comparing integers
        """
        if damage < 0:
            raise ValueError("Damage cannot be negative")

    def get_unit_type(self) -> str:
        """ returns the current Fighter's type.
        :complexity: best and worst O(1), returning a String
        """
        return self.__class__.__name__

    @abstractmethod
    def __str__(self) -> str:
        """returns a string describing the type of unit, its current life and experience."""
        pass


class Soldier(Fighter):
    """This class represents Fighter of type Soldier. Always costs 1, Starts with life value of 3 and experience 0."""
    COST = 1

    def __init__(self) -> None:
        """initialises the variables using Parent's init method with the amounts received as input.
        :complexity: Best and worst is O(1), because just assigning values
        """
        super().__init__(3, 0)

    def get_speed(self) -> int:
        """Returns the speed of the current Soldier.
        :complexity: Best and worst is O(1), just subtracting 2 integers and then returning the result
        """
        return 1 - self.get_experience()

    def get_attack_damage(self) -> int:
        """The amount of damage performed by Soldier when it attacks.
        :complexity: Best and worst is O(1), just adding 2 integers and then returning the result
        """
        return 1 + self.get_experience()

    def defend(self, damage: int) -> None:
        """Evaluates the current Soldier's life lost after getting attacked.
        :param damage: incoming damage
        :complexity: Best and worst is O(1), comparing 2 integers then subtracting life by 1
        """
        if damage > self.get_experience():
            self.lose_life(1)

    def get_cost(self) -> int:
        """returns the soldier's cost.
        :complexity: Best and worst is O(1), returning a constant integer
        """
        return Soldier.COST

    def __str__(self) -> str:
        """ Returns a string describing Soldier's current life and experience
        :complexity: O(1), just returning a string of the current soldier's life and experience values.
        """
        return f"Soldier's life = {self.get_life()} and experience = {self.get_experience()}"


class Archer(Fighter):
    """This class represents Fighter of type Archer. Always costs 2, Starts with life value of 3 and experience 0."""
    COST = 2

    def __init__(self) -> None:
        """initialises the variables using Parent's init method with the amounts received as input.
        :complexity: Best and worst is O(1), because just assigning value to instance variables
        """
        super().__init__(3, 0)

    def get_speed(self) -> int:
        """Returns the speed of the current Archer.
        :complexity: Best and worst is O(1), always returns 3
        """
        return 3

    def get_attack_damage(self) -> int:
        """The amount of damage performed by Archer when it attacks.
        :complexity: Best and worst is O(1), returning the result of multiplying 2 values and then adding 1.
        """
        return 2 * self.get_experience() + 1

    def defend(self, damage: int) -> None:
        """Evaluates the current Archer's life lost after getting attacked.
        :param damage: incoming damage
        :complexity: Best and worst is O(1), Subtrcting 1 from current Archer's life
        """
        self.lose_life(1)

    def get_cost(self) -> int:
        """returns the archer's cost.
        :complexity: Best and worst is O(1), returning a constant integer
        """
        return Archer.COST

    def __str__(self) -> str:
        """ Returns a string describing Archer's current life and experience.
        :complexity: O(1), just returning a string of the current archer's life and experience values
        """
        return f"Archer's life = {self.get_life()} and experience = {self.get_experience()}"


class Cavalry(Fighter):
    """This class represents Fighter of type Cavalry. Always costs 3, Starts with life value of 4 and experience 0."""
    COST = 3

    def __init__(self) -> None:
        """Initialises the variables using Parent's init method with the amounts received as input.
        :complexity: Best and worst is O(1), because just assigning value to instance variables
        """
        super().__init__(4, 0)

    def get_speed(self) -> int:
        """Returns the speed of the current cavalry.
        :complexity: Best and worst is O(1), adding 2 to current cavalry's experience points
        """
        return 2 + self.get_experience()

    def get_attack_damage(self) -> int:
        """The amount of damage performed by cavalry when it attacks.
        :complexity: Best and worst is O(1), just adds integers then returns result
        """
        return 1 + self.get_experience()

    def defend(self, damage: int) -> None:
        """Evaluates the current Cavalry's life lost after getting attacked.
        :param damage: incoming damage
        :complexity: Best and worst is O(1), Subtracting 1 from current Cavalry's life after comparing values
        """
        if damage > (self.get_experience() / 2):
            self.lose_life(1)

    def get_cost(self) -> int:
        """returns the cavalry's cost.
        :complexity: Best and worst is O(1), returning a constant integer
        """
        return Cavalry.COST

    def __str__(self) -> str:
        """ Returns a string describing cavalry's current life and experience.
        :complexity: O(1), just returning a string of the current cavalry's life and experience values
        """
        return f"Cavalry's life = {self.get_life()} and experience = {self.get_experience()}"


class Army:

    def __init__(self) -> None:
        """Initialises the name and force to None.
        :complexity: Best and worst is O(1), just assigning values to None
        """
        self.name = None
        self.force = None

    def __correct_army_given(self, soldiers: int, archers: int, cavalry: int) -> bool:
        """Return true if sum of all fighter's cost doesnt exceed the budget which is 30.
        :param soldiers: number of soldiers in army
        :param archers: number of archers in army
        :param cavalry: number of cavalries in army
        :complexity: Best and worst O(1), just computing the price of the army and compare if exceed budget
        """
        for i in [soldiers, archers, cavalry]:
            if i < 0:
                return False

        price = sum([Soldier.COST * soldiers,
                     Archer.COST * archers,
                     Cavalry.COST * cavalry])
        if price > 30 or price < 0:
            return False
        else:
            return True

    def __assign_army(self, name: str, sold: int, arch: int, cav: int, formation: int) -> None:
        """Assigns the units into Stack or Queue based on the formation value.
        :param name: name of the player
        :param sold: number of soldiers
        :param arch: number of archers
        :param cav: number of cavalries
        :param formation: using Stack or Queue
        :complexity: Best and worst is O(n) where n is the sum of the number of soldiers, archers and cavalries.
                     because just looping based on those numbers and assigning into stack or queue.
        """
        self.name = name
        self.formation = formation
        capacity = sum([sold, arch, cav])

        # Stack
        if formation == 0:
            self.force = ArrayStack(capacity)
            # Adding Cavalry
            for i in range(cav):
                self.force.push(Cavalry())
            # Adding Archers
            for i in range(arch):
                self.force.push(Archer())
            # Adding Soldiers
            for i in range(sold):
                self.force.push(Soldier())

        # Queue
        else:
            self.force = CircularQueue(max_capacity=capacity)
            # Adding Soldiers
            for i in range(sold):
                self.force.append(Soldier())
            # Adding Archers
            for i in range(arch):
                self.force.append(Archer())
            # Adding Cavalry
            for i in range(cav):
                self.force.append(Cavalry())

    def choose_army(self, name: str, formation: int) -> None:
        """Always the user to input the number of soldiers, archers and cavalries, checks if they are correct,
           then assigns them, then prints them.
        :param name: the player's name
        :param formation: using Stack or Queue
        :complexity: Best and worst is O(n) because inputting values is O(1), __correct_army_given is always O(1),
                     __assign_army is O(n) where n is the number of soldiers,archers, and cavalries,
                     so overall it is O(n)
        """
        self.name = name
        self.name = formation

        while True:
            s1, a1, c1 = [int(x) for x in input("Player " + name + " choose your army as ").split()]
            if self.__correct_army_given(s1, a1, c1):
                self.__assign_army(name, s1, a1, c1, formation)
                print("Where ", end='')
                print(f"{s1} is the number of soldiers")
                print(f"      {a1} is the number of archers")
                print(f"      {c1} is the number of cavalries")
            else:
                print("Invalid number of units, try again")
                self.choose_army(name, formation)
            break

    def __str__(self) -> str:
        """
        returns string containing the information of each army element in force.
        :complexity: Best and worst is O(n) because use's stack_adt or queue_adt __str__ method which is O(n)
        """
        return str(self.force)


if __name__ == '__main__':
    a = Army()
    b = Army()
    a.choose_army("zaid", 1)
    b.choose_army("diaz", 0)
    print(str(a))
    print(str(b))

