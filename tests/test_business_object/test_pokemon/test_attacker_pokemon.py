from business_object.pokemon.attacker_pokemon import AttackerPokemon
from business_object.statistic import Statistic


class TestAttackerPokemon:
    def test_get_coef_damage_type(self):
        # GIVEN
        snorlax = AttackerPokemon(stat_current=Statistic(speed = 25, attack = 75))

        # WHEN
        multiplier = snorlax.get_pokemon_attack_coef()

        # THEN
        assert multiplier == 1.5

    def test_level_up(self):
        # GIVEN
        snorlax = AttackerPokemon(level=3)

        # WHEN
        snorlax.level_up()

        # THEN
        assert snorlax.level == 4

if __name__ == "__main__":
    import pytest

    pytest.main([__file__])