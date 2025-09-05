from business_object.pokemon.abstract_pokemon import AbstractPokemon

class DefenderPokemon(AbstractPokemon):
    # def __init__(self, stat_max=None, stat_current=None, level=0, name=None, type_pk=None):
    #     super().__init__(self, stat_max=None, stat_current=None, level=0, name=None, type_pk=None)
    
    def get_pokemon_attack_coef(self):
        return 1 + (self.attack_current + self.defense_current) / 200