"""Task 4"""


class BeeElephant:
    def __init__(self, bee, elephant):
        self.bee = bee
        self.elephant = elephant

    def fly(self):
        if self.bee >= self.elephant:
            return True
        else:
            return False

    def trumpet(self):
        if self.elephant >= self.bee:
            return 'tu-tu-doo-doo!'
        else:
            return 'wzzzzz'

    def eat(self, meal, value):
        if meal == 'nectar':
            print('Пчелка покушала и стала больше')
            self.elephant -= value
            if self.elephant < 0:
                self.elephant = 0
            self.bee += value
            if self.bee > 100:
                self.bee = 100
        elif meal == 'grass':
            print('Слоник покушал и стал больше')
            self.elephant += value
            if self.elephant > 100:
                self.elephant = 100
            self.bee -= value
            if self.bee < 0:
                self.bee = 0

    def get_parts(self):
        return self.bee, self.elephant


gybrid = BeeElephant(55, 45)
print(list(gybrid.get_parts()))
print(gybrid.fly())
print(gybrid.trumpet())
gybrid.eat('grass', 60)
print(list(gybrid.get_parts()))
print(gybrid.fly())
print(gybrid.trumpet())
