import unittest

def is_child(age):
    return 0 <= age <= 9

def is_adult(age):
    return 18 < age <= 65

def is_golden(age):
    return 65 < age <= 150

class TestAge(unittest.TestCase):
    def test_child(self):
        for age in range(10):
            with self.subTest(age=age):
                self.assertEqual(is_child(age), True)
                print(f"{age} is considered as a child.")

    def test_adult(self):
        for age in range(19, 66):
            with self.subTest(age=age):
                self.assertEqual(is_adult(age), True)
                print(f"{age} is considered as an adult.")
    
    def test_golden(self):
        for age in range(66, 151):
            with self.subTest(age=age):
                self.assertEqual(is_golden(age), True)
                print(f"{age} is considered as a golden.")

if __name__ == "__main__":
    unittest.main(verbosity=2)
