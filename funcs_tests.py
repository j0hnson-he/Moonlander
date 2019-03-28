#Project 2 LanderFuncs Test Cases
#
#Name: Rohith Dara
#Instructor: S. Einakian
#Section: 01

#at least 3 test cases for each function
import unittest
from landerFuncs import *

class TestCases(unittest.TestCase):
   #first test for updateAcceleration
   def test_updateAcceleration_1(self):
      self.assertEqual(updateAcceleration(1.62,25),6.48)
      self.assertAlmostEqual(updateAcceleration(1.62,30),8.1)
      self.assertAlmostEqual(updateAcceleration(1.62,52),15.228)
   def test_updateAltitude(self):
      self.assertEqual(updateAltitude(50,-3,14),54)
      self.assertEqual(updateAltitude(30,-10,25),32.5)
      self.assertEqual(updateAltitude(100,-5,18),104)
   def test_updateVelocity(self):
      self.assertEqual(updateVelocity(15,18),33)
      self.assertEqual(updateVelocity(14,8),22)
      self.assertEqual(updateVelocity(266,234),500)
   def test_updateFuel(self):
      self.assertEqual(updateFuel(134,4),130)
      self.assertEqual(updateFuel(3,3),0)
      self.assertEqual(updateFuel(17,8),9)
      
 
      

# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

