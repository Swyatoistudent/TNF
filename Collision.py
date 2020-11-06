class Collision:

    def __init__(self, damage: int, collision_effect):
        self.__damage = damage
        self.__collision_effect = collision_effect

    def get_damage(self): return self.__damage

    def get_collision_effect(self): return self.__collision_effect
