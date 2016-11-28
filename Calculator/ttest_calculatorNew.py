import unittest

from trevcalc import Calculator

class MyTest(unittest.TestCase):
    def test_add(self):
        self.assertEqual(Calculator().add(5,15),20)
        self.assertEqual(Calculator().add(-5,15),10)
        self.assertEqual(Calculator().add(0,15),15)
    def test_sub(self):
        self.assertEqual(Calculator().sub(5,3),2)
        self.assertEqual(Calculator().sub(-5,3),-8)
        self.assertEqual(Calculator().sub(5,-3),8)
    def test_mul(self):
        self.assertEqual(Calculator().mul(8,7),56)
        self.assertEqual(Calculator().mul(0,7),0)
        self.assertEqual(Calculator().mul(-8,7),-56)
    def test_div(self):
        self.assertEqual(Calculator().div(256,16),16)
        self.assertEqual(Calculator().div(256,-16),-16)   
        self.assertEqual(Calculator().div(0,16),0)
    def test_squared(self):
        self.assertEqual(Calculator().squared(4),16)
        self.assertEqual(Calculator().squared(0),0)
        self.assertEqual(Calculator().squared(1),1)
    def test_square_root(self):
        self.assertEqual(Calculator().square_root(25),5)
        self.assertEqual(Calculator().square_root(256),16)
        self.assertEqual(Calculator().square_root(1),1)
    def test_exponentiate(self):
        self.assertEqual(Calculator().exponentiate(2,3),8)
        self.assertEqual(Calculator().exponentiate(2,4),16)
        self.assertEqual(Calculator().exponentiate(0,3),0)
    def test_cube(self):
        self.assertEqual(Calculator().cube(5),125)
        self.assertEqual(Calculator().cube(0),0)
        self.assertEqual(Calculator().cube(15),3375)
    def test_cube_root(self):
        self.assertEqual(Calculator().cube_root(-125),-5)
        self.assertEqual(Calculator().cube_root(875),9)
        self.assertEqual(Calculator().cube_root(0),0)
    def test_factorial(self):
        self.assertEqual(Calculator().factorial(5),120)
        self.assertEqual(Calculator().factorial(7),5040)
        self.assertEqual(Calculator().factorial(0),1)
        self.assertEqual(Calculator().factorial(-12),None)
    def test_sin(self):
        self.assertEqual(Calculator().sin(5),0.0872)
        self.assertEqual(Calculator().sin(0),0)
        self.assertEqual(Calculator().sin(-2),-0.0349)
    def test_cos(self):
        self.assertEqual(Calculator().cos(2),0.9994)
        self.assertEqual(Calculator().cos(0),1)
        self.assertEqual(Calculator().cos(-1),0.9998)
        
if __name__ == '__main__':
    unittest.main()