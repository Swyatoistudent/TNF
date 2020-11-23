import Hero


class Control:
    def __init__(self, keys: {}, hero: Hero):
        self.keys = keys
        self.__hero = hero

    def __move_hero(self, hero: Hero, direction: [int, int]):
        hero.move(direction)

    def __attack_hero(self, hero: Hero, direction: [int, int]):
        hero.current_weapon.attack()

    def __use_item(self, hero: Hero):
        hero.active_item.effect(hero)

    def __switch_weapon(self, hero: Hero):
        hero.weapons.append(hero.weapons.pop())
        hero.current.weapon = hero.weapons[0]

    def __reload_weapon(self,hero):
        hero.current_weapon.reload()

