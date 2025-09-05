import copy
from abc import ABC, abstractmethod

from business_object.statistic import Statistic

class AbstractAttack(ABC):
    """ Classe Abstraite pour une attaque"""
    def __init__(self, power, name, description=None):
        self._power = power
        self._name = name
        self.description = description
    
    # Les méthodes
    @abstractmethod
    def compute_damage(self, pok1, pok2):
        """A une capacité renvoie les dégats
        Returns:
            int
        """
        pass

     