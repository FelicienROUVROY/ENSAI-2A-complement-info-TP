from business_object.Attack.FixedDamageAttack import FixedDamageAttack

class TestFixedAttack:
    def test_fixed_attack(self):
        ### When
        attack = FixedDamageAttack(50, "charge")
        ### Given
        damage = attack.compute_damage()
        ### Then 
        assert damage == 50