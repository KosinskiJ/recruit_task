import unittest

from zadanie2 import Car, get_carpool, DieselCar


test_car = Car('Test', 100, 70)
test_diesel_car = DieselCar('Test_diesel', 100, 10)
brand_car = ['Peugeot', 'Volvo', 'Skoda', 'Fiat', 'Ford',
             'Doge', 'BMW', 'Toyota', 'Mazda', 'Jaguar']


class TestZadanie2(unittest.TestCase):

    def test_fill_tank_over_limit(self):
        with self.assertRaises(Exception) as context:
            test_car.fill_tank(limit = 1.1)
        self.assertTrue(
            'You can add limit only on range 0 to 1'
            in str(context.exception)
        )

    def test_fill_tank_to_many_parameters(self):
        with self.assertRaises(Exception) as context:
            test_car.fill_tank(limit = 0.5, liters = 10)
        self.assertTrue(
            "You can add only one parameters they are mutually exclusive"
            in str(context.exception)
        )

    def test_fill_tank_under_limit(self):
        with self.assertRaises(Exception) as context:
            limit = 0.5
            test_car.fill_tank(limit = limit)
        self.assertTrue(
            f'Car have more than {limit} fuel, have:'
            f'{"%.1f" % (test_car.tanked_fuel / test_car.tank_capacity)}'
            in str(context.exception)
        )

    def test_fill_tank_liters_type(self):
        with self.assertRaises(Exception) as context:
            test_car.fill_tank(liters = 'ss')
        self.assertTrue(
            'Liters can be only integer or float'
            in str(context.exception)
        )

    def test_fill_tank_to_many_liters(self):
        with self.assertRaises(Exception) as context:
            test_car.fill_tank(liters = 100)
        self.assertTrue(
            f"{test_car.brand} have only tank capacity {test_car.tank_capacity} "
            f"liters you can only fill with maximal "
            f"{test_car.tank_capacity - test_car.tanked_fuel} liters of fuel "
            in str(context.exception)
        )

    def test_fill_tank_diesel_car(self):
        with self.assertRaises(EnvironmentError):
            test_diesel_car.fill_tank(liters = 100)

    def test_to_many_car(self):
        with self.assertRaises(Exception) as context:
            get_carpool(len(brand_car) + 1)
        self.assertTrue(
            f"You can't create more than {len(brand_car)} objects"
            in str(context.exception)
        )


