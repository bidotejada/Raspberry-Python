class BottleRocket:
    def __init__(self, name):
        self.name = name

    def display_info(self):
        print(f'Rocket name: {self.name}')


class RocketLauncher:
    rocket_list = []

    @classmethod
    def add_rocket(cls, *rockets):
        for i in rockets:
            cls.rocket_list.append(i)

    @classmethod
    def list_rockets(cls):
        for rocket_list in cls.rocket_list:
            rocket_list.display_info()


rocket_1 = BottleRocket('Mars 1')
rocket_2 = BottleRocket('Mars 2')
rocket_3 = BottleRocket('Mars 3')

RocketLauncher.add_rocket(rocket_1, rocket_2, rocket_3)
RocketLauncher.list_rockets()
