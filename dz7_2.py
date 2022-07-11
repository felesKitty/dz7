from abc import ABC, abstractmethod


class Wear(ABC):
    result = 0
    def __init__(self, textile):
        self.textile = textile

    @property
    @abstractmethod
    def consumption(self):
        pass

    def __add__(self, other):
        Wear.result += self.consumption + other.consumption
        return Suit(0)

    def __str__(self):
        all = Wear.result
        Wear.result = 0
        return f'{all}'


class Overcoat(Wear):
    @property
    def consumption(self):
        return round(self.textile / 6.5) + 0.5


class Suit(Wear):
    @property
    def consumption(self):
        return round((2 * self.textile + 0.3) / 100)


coat = Overcoat(88)
suit = Suit(127)
suit_2 = Suit(29)
print(f'You used up {coat + suit + coat} metres of textile')
