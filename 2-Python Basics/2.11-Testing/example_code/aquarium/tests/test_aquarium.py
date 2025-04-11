import unittest
from main import FishTank


class TestAddFishToTank(unittest.TestCase):
    
    def setUp(self):
        print("Running before each method...")
        self.tank = FishTank("A")
        self.fish_list = ["Tuna", "Bream", "Red Snapper", "Hake"]
        
    def tearDown(self):
        print("Runs after each method...")
    
    def test_add_fish_to_tank_success(self):
        result = self.tank.add_fish_to_tank(self.fish_list)
        expected_res = {self.tank.tank_name: ["Tuna", "Bream", "Red Snapper", "Hake"]}
        self.assertDictEqual(result, expected_res)
        
    def test_add_fish_to_tank_exception(self):
        too_many_fish = ["shark"] * 25
        with self.assertRaises(ValueError) as exc_context:
            self.tank.add_fish_to_tank(too_many_fish)
        self.assertEqual(str(exc_context.exception), "A maximum of 10 fish per tank")


class TestFillWithWater(unittest.TestCase):
    
    def setUp(self):
        self.tank = FishTank("A")
    
    def test_tank_is_empty_by_default(self):
        self.assertFalse(self.tank.has_water)
    
    def test_tank_is_full(self):
        self.tank.fill_with_water()
        self.assertTrue(self.tank.has_water) 