from business_object.Attack.abstract_attack import AbstractAttack
from business_object.pokemon.abstract_pokemon import AbstractPokemon
import random

class AbstractVariableDamageAttack(AbstractAttack):
    def get_attack_stat(pok):
         pass
    def get_defense_stat(pok):
        pass
    def compute_damage(self, pok1, pok2):
        return (((2 * pok1.level() / 5) + 2) * self.power() * pok1.get_attack_stat() / 
        (pok2.get_defense_stat * 50) + 2) * random.uniform(0.8, 1)

class SpecialFormulaAttack(AbstractVariableDamageAttack):
    def get_attack_stat(pok):
        return pok.sp_atk()
    def get_defense_stat(pok):
        return pok.sp_def()

class PhysicalFormulaAttack(AbstractVariableDamageAttack):
    def get_attack_stat(pok):
        return pok.attack()
    def get_defense_stat(pok):
        return pok.defense()