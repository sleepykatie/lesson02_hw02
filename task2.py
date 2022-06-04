from abc import ABC, abstractmethod


class Clothes(ABC):

    def __init__(self, main_param):
        self.main_param = main_param

    @abstractmethod
    def consumption_fabric(self):
        pass


class Coat(Clothes):

    @property
    def consumption_fabric(self):
        return self.main_param/6.5 + 0.5


class Suit(Clothes):

    @property
    def consumption_fabric(self):
        return 2 * self.main_param + 0.3


blue_coat = Coat(46)
beige_suit = Suit(1.74)
sum_consump_fabric = blue_coat.consumption_fabric + beige_suit.consumption_fabric
print(blue_coat.consumption_fabric)
print(beige_suit.consumption_fabric)
print(sum_consump_fabric)
