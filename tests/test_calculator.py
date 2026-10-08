import unittest

from calculator import calculate


class CalculateTests(unittest.TestCase):
    def test_basic_operations(self):
        self.assertEqual(calculate("add", 2, 3), 5)
        self.assertEqual(calculate("subtract", 5, 3), 2)
        self.assertEqual(calculate("multiply", 2, 3), 6)
        self.assertEqual(calculate("divide", 6, 3), 2)

    def test_division_by_zero(self):
        with self.assertRaisesRegex(ValueError, "Cannot divide by zero"):
            calculate("divide", 1, 0)

    def test_unknown_operation(self):
        with self.assertRaisesRegex(ValueError, "Unknown operation"):
            calculate("power", 2, 3)


if __name__ == "__main__":
    unittest.main()
