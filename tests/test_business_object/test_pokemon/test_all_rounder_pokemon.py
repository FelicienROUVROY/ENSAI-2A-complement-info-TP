from business_object.pokemon.all_rounder_pokemon import All_rounderPokemon
from business_object.statistic import Statistic


class TestAll_rounderPokemon:
    def test_get_coef_damage_type(self):
        # GIVEN
        snorlax = All_rounderPokemon(stat_current=Statistic(sp_def=50, sp_atk=50))

        # WHEN
        multiplier = snorlax.get_pokemon_attack_coef()

        # THEN
        assert multiplier == 1.5

    def test_level_up(self):
        # GIVEN
        snorlax = All_rounderPokemon(level=3)

        # WHEN
        snorlax.level_up()

        # THEN
        assert snorlax.level == 4

if __name__ == "__main__":
    import pytest

    pytest.main([__file__])