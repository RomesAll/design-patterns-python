import uuid, enum, abc, typing, json

class SizeEnum(enum.Enum):
    SMALL = 25
    MEDIUM = 30
    LARGE = 35

class ToppingEnum(enum.Enum):
    MOZZARELLA = 'MOZZARELLA'
    PARMESAN = 'PARMESAN'
    CHEDDAR = 'CHEDDAR'
    BEEF = 'BEEF'
    BACON = 'BACON'
    CHICKEN = 'CHICKEN'
    PEPPERONI = 'PEPPERONI'
    RED_ONIONS = 'RED_ONIONS'
    SHRIMP = 'SHRIMP'
    TOMATOES = 'TOMATOES'

class DoughEnum(enum.Enum):
    TRADITIONAL = 'TRADITIONAL'
    FINE = 'FINE'

class SauceEnum(enum.Enum):
    CHEESE = 'CHEESE'
    GARLIC = 'GARLIC'
    BARBECUE = 'BARBECUE'

class Pizza:

    def __init__(self, name):
        self.id: uuid.UUID = uuid.uuid4()
        self.name: str = name
        self.price: float = 0
        self.size: SizeEnum | None = None
        self.toppings: list[ToppingEnum] | None = list()
        self.cooking_time: int = 0
        self.dough: DoughEnum | None = None
        self.sauce: SauceEnum | None = None

    def __get_attrs(self):
        object_attrs = {
            'pizza': self.name,
            'size': self.size.value,
            'price': self.price,
            'toppings': [topping.name for topping in self.toppings],
            'dough': self.dough.name,
            'sauce': self.sauce.name,
            'cooking_time': self.cooking_time
        }
        return object_attrs

    def __str__(self):
        return f"{self.__class__.__name__}({self.__get_attrs()})"

    def __repr__(self):
        object_attrs = self.__get_attrs()
        object_attrs.update({'id': self.id})
        return f"{self.__class__.__name__}({object_attrs})"

class BasePizzaBuilder(abc.ABC):

    @abc.abstractmethod
    def get_pizza(self) -> Pizza: pass

    @abc.abstractmethod
    def append_topping(self, additionally: list[ToppingEnum] | None = None) -> object: pass

    @abc.abstractmethod
    def append_sauce(self, sauce: SauceEnum) -> object: pass

    @abc.abstractmethod
    def prepare_dough(self, dough: DoughEnum) -> object: pass

    @abc.abstractmethod
    def set_size(self, size: SizeEnum) -> object: pass

class MargaritaPizzaBuilder(BasePizzaBuilder):

    def __init__(self):
        self.pizza: Pizza = Pizza('Margarita')
        self.pizza.cooking_time = 15
        self.pizza.price = 700

    def get_pizza(self) -> Pizza:
        return self.pizza

    def append_topping(self, additionally: list[ToppingEnum] | None = None) -> object:
        self.pizza.toppings.extend([
            ToppingEnum.MOZZARELLA,
            ToppingEnum.TOMATOES,
            ToppingEnum.RED_ONIONS,
        ])
        if additionally is not None:
            self.pizza.toppings.extend(additionally)
        return self

    def append_sauce(self, sauce: SauceEnum = SauceEnum.CHEESE) -> object:
        self.pizza.sauce = sauce
        return self

    def prepare_dough(self, dough: DoughEnum = DoughEnum.TRADITIONAL) -> object:
        self.pizza.dough = dough
        return self

    def set_size(self, size: SizeEnum = SizeEnum.MEDIUM) -> object:
        self.pizza.size = size
        return self

class PepperoniPizzaBuilder(BasePizzaBuilder):

    def __init__(self):
        self.pizza: Pizza = Pizza('Pepperoni')
        self.pizza.cooking_time = 20
        self.pizza.price = 800

    def get_pizza(self) -> Pizza:
        return self.pizza

    def append_topping(self, additionally: list[ToppingEnum] | None = None) -> object:
        self.pizza.toppings.extend([
            ToppingEnum.MOZZARELLA,
            ToppingEnum.TOMATOES,
            ToppingEnum.PEPPERONI,
        ])
        if additionally is not None:
            self.pizza.toppings.extend(additionally)
        return self

    def append_sauce(self, sauce: SauceEnum = SauceEnum.BARBECUE) -> object:
        self.pizza.sauce = sauce
        return self

    def prepare_dough(self, dough: DoughEnum = DoughEnum.TRADITIONAL) -> object:
        self.pizza.dough = dough
        return self

    def set_size(self, size: SizeEnum = SizeEnum.MEDIUM) -> object:
        self.pizza.size = size
        return self

class Director:

    def __init__(self):
        self.builder = None

    def set_builder(self, builder: BasePizzaBuilder):
        self.builder = builder

    def make_pizza_base_args(self):
        if self.builder is None:
            raise ValueError('Builder must be set before making pizza.')
        result_pizza = (
            self.builder.set_size().prepare_dough().append_sauce().append_topping().get_pizza()
        )
        return result_pizza

if __name__ == '__main__':
    director = Director()
    builder1 = MargaritaPizzaBuilder()
    builder2 = PepperoniPizzaBuilder()

    director.set_builder(builder1)
    result = director.make_pizza_base_args()
    print(result)

    director.set_builder(builder2)
    print(result)