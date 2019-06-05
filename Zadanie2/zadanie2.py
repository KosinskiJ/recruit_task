import random


class Car:

    def __init__(self, brand, tank_capacity, tanked_fuel):
        self.brand = brand
        self.tank_capacity = tank_capacity
        self.tanked_fuel = tanked_fuel

    def __str__(self):
        return f'New car of brand {self.brand}, with tank full in ' \
            f'{"%.1f" % (self.tanked_fuel / self.tank_capacity * 100)} %'

    def __repr__(self):
        return f'Car at <{id(self)}> of brand {self.brand}, with tank full in' \
            f' {"%.1f" % (self.tanked_fuel / self.tank_capacity * 100)} %'

    def fill_tank(self, limit=None, liters=None):
        """Method for tank your car"""

        if limit is None and liters is None:
            print(f"{self.brand} has been fill with "
                  f"{self.tank_capacity - self.tanked_fuel} liters of fuel")
            self.tanked_fuel = self.tank_capacity
        elif limit is not None and liters is not None:
            raise Exception("You can add only one parameters they are mutually exclusive")
        elif limit is not None:
            if (type(limit) is int or type(limit) is float) and 0 < limit <= 1:
                limit_in_liters = (limit * self.tank_capacity)
                if limit_in_liters > self.tanked_fuel:
                    print(f"{self.brand} has been fill with "
                          f"{limit_in_liters - self.tanked_fuel} liters of fuel")
                    self.tanked_fuel = limit_in_liters

                else:
                    raise Exception(f'Car have more than {limit} fuel, have:'
                                    f'{"%.1f" % (self.tanked_fuel / self.tank_capacity)}')

            else:
                raise Exception('You can add limit only on range 0 to 1')
        elif liters is not None:

            if type(liters) is float or type(liters) is int:
                if liters + self.tanked_fuel > self.tank_capacity:
                    raise Exception(f"{self.brand} have only tank capacity {self.tank_capacity} "
                                    f"liters you can only fill with maximal "
                                    f"{self.tank_capacity - self.tanked_fuel} liters of fuel ")

                elif liters + self.tanked_fuel <= self.tank_capacity:
                    print(f"{self.brand} has been fill with {liters} liters of fuel")
                    self.tanked_fuel += liters
            else:
                raise Exception('Liters can be only integer or float')


class DieselCar(Car):
    def fill_tank(self, *args, **kwargs):
        raise EnvironmentError("Diesel fuel not available due to environmental reasons")


def get_carpool(n_car):
    """Function where you can create specified number of Car objects """
    brand_car = ['Peugeot', 'Volvo', 'Skoda', 'Fiat', 'Ford',
                 'Doge', 'BMW', 'Toyota', 'Mazda', 'Jaguar']
    car_objects = {}
    if n_car <= len(brand_car):

        for x in range(n_car):
            random_tank_capacity = random.randint(40, 70)
            random_tanked_fuel = random.randint(40, random_tank_capacity)
            while True:
                random_car = random.choice(brand_car)
                if random_car not in car_objects:
                    car_objects[random_car] = Car(random_car, random_tank_capacity, random_tanked_fuel)
                    break

        return car_objects

    else:
        raise Exception(f"You can't create more than {len(brand_car)} objects")


car = Car("s", 50,20)

car.fill_tank(limit = 0.3)