from business_object.Attack.VariableDamageAttack import PhysicalFormulaAttack
from business_object.pokemon.attacker_pokemon import AttackerPokemon

class physicalVariableAttack:
    def test_physical_variable_attack(self):
        ### When

        attack = PhysicalFormulaAttack(50, "charge")
        ### Given
        damage = attack.compute_damage()
        pok1 = atta
        ### Then 
        assert damage == 50