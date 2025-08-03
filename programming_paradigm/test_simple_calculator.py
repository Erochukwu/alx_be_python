import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(6, 3), 8)
        self.assertEqual(self.calc.add(15, 8), 23)
        self.assertEqual(self.calc.add(15, three), 18)
        # Add more assertions to thoroughly test the add method.

# Remember to write additional test methods for subtract, multiply, and divide.
