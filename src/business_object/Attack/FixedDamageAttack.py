from business_object.Attack.abstract_attack import AbstractAttack

class FixedDamageAttack(AbstractAttack):
    def compute_damage(self):
        return self._power
