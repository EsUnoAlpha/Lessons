class Hero():
    def __init__(self, name, health, armor, power, weapon):
        self.name = name
        self.health = health
        self.armor = armor
        self.power = power
        self.weapon = weapon
    def print_info(self):
        print('Поприветствуйте героя:', self.name)
        print('Уровень здоровья:', self.health)
        print('Броня:', self.armor)
        print('Сила удара:', self.power)
        print('Оружие:', self.weapon)

    def strike_hero(self, rascal):
        print(
            'Hit! ' + self.name + ' attack ' + rascal.name + ' with power ' + str(self.power) + ' using ' + self.weapon +'\n'
        )
        rascal.armor -= knight.power
        if rascal.armor < 0:
            rascal.health += rascal.armor
            rascal.armor = 0
        print (
            rascal.name + ' Armor class falled to ' + str(rascal.armor) + ' and HP falled to ' + str(rascal.health) + '\n'
        )

    def strike_enemy(self, knight):
        print(
            'Hit! ' + rascal.name + ' attack ' + self.name + ' with power ' + str(rascal.power) + ' using ' + rascal.weapon +'\n'
        )
        knight.armor -= rascal.power
        if knight.armor < 0:
            knight.health += knight.armor
            knight.armor = 0
        print (
            self.name + ' Armor class falled to ' + str(self.armor) + ' and HP falled to ' + str(self.health) + '\n'
        )


knight = Hero('Ричард', 50, 25, 20, 'меч')
knight.print_info()
rascal = Hero('Helen', 50, 5, 5, 'Bow')
rascal.print_info()
while True:
    print('Knight attacking')
    knight.strike_hero(rascal)
    print('Rascal attacking')
    knight.strike_enemy(rascal)
    if rascal.health <= 0:
        print('Knght wins')
        break
    elif knight.health <= 0:
        print('Rascal wins')
        break

    else:
        print('Fight continue')

