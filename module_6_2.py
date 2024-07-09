class Vehicle:
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    def __init__(self, owner, _model, _color, _engine_power):
        self.owner = owner
        self._model = _model
        self._color = _color
        self._engine_power = _engine_power

    def get_model(self):
        return print(f'Модель {self._model}')

    def get_horsepower(self):
        return print(f'Мощность двигателя {self._engine_power}')

    def get_color(self):
        if self._color.lower() in self.__COLOR_VARIANTS[:]:
            return print(f'Цвет {self._color}')

    def print_info(self):
        return self.get_model(), self.get_horsepower(), self.get_color(), print(f'Владелец {self.owner}')

    def set_color(self, new_color):
        self.new_color = new_color
        if self.new_color.lower() in self.__COLOR_VARIANTS[:]:
            self._color = self.new_color
        else:
            return print(f'Невозможно покрасить в {self.new_color}')


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5
    pass


vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)
vehicle1.print_info()
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'
vehicle1.print_info()
