# For every function write purpose statement and signature
# Project 2 - Moonlander Functions
#
# Author: Rohith Dara
# Instructor: S. Einakian
# Section: 01

#Show the necessary Welcome message when the program starts
#none->none
def showWelcome():
   print ("Welcome aboard the Lunar Module Flight Simulator")
   print ()
   print ("   To begin you must specify the LM's initial altitude")
   print ("   and fuel level.  To simulate the actual LM use") 
   print ("   values of 1300 meters and 500 liters, respectively.")
   print ()
   print ("   Good luck and may the force be with you!")
   print ()

#Ask the user to input the amount of fuel and store it
#none->int
def getFuel():
   initial_fuel = int(input("Enter the initial amount of fuel on board the LM (in liters): "))
   while initial_fuel <= 0:
      print ("ERROR: Amount of fuel must be positive, please try again")
      initial_fuel = int(input("Enter the initial amount of fuel on board the LM (in liters): "))
   return initial_fuel

#Ask the user to input the initial altitude and store it
#none->int
def getAltitude():
   initial_alt = int(input("Enter the initial altitude of the LM (in meters): "))
   while initial_alt < 1 or initial_alt > 9999:
      print ("ERROR: Altitude must be between 1 and 9999, inclusive, please try again")
      initial_alt = int(input("Enter the initial altitude of the LM (in meters): "))
   return initial_alt

#Read the the specified variables and output them with a formatted short descriptor 
#int,int,int,float,float->str,int,str,int,str,int,str,float,str,float
def displayLMState(elapsedTime, altitude, velocity, fuelAmount, fuelRate):
   print(("%13s"% "Elapsed Time: ") + ("%4d"% elapsedTime) + (" s"))
   print(("%14s"% "Fuel: ") + ("%4d"% fuelAmount) + (" l"))
   print(("%14s"% "Rate: ") + ("%4d"% fuelRate) + (" l/s"))
   print(("%14s"% "Altitude: ") + ("%4.2f"% altitude) + (" m"))
   print(("%14s"% "Velocity: ") + ("%5.2f"% velocity) + (" m/s"))

#Ask the user to input their desired fuel rate and store it while making sure that it is less than the current fuel
#int->int
def getFuelRate(currentFuel):
   fuelRate = int(input("Enter fuel rate (0-9, 0=freefall, 5=constant velocity, 9=max thrust): "))
   while fuelRate > 9 or fuelRate < 0:
      print ("ERROR: Fuel rate must be between 0 and 9, inclusive")
      print ()
      fuelRate = int(input("Enter fuel rate (0-9, 0=freefall, 5=constant velocity, 9=max thrust): "))
   if fuelRate > currentFuel:
      fuelRate = currentFuel
   return fuelRate

#Take in the gravity and fuel rate and output the acceleration
#float,int->float
def updateAcceleration(gravity, fuelRate):
   acceleration = gravity*((fuelRate/5)-1)
   return acceleration

#Take in the current altitude, velocity, and acceleration and output the new altitude
#float,float,float->float
def updateAltitude(altitude, velocity, acceleration):
   newAltitude = altitude + velocity + (acceleration/2)
   return newAltitude

#Take in the current velocity and acceleration and output the new velocity
#float,float->float
def updateVelocity(velocity, acceleration):
   newVelocity = velocity + acceleration
   return newVelocity

#Take in the current fuel amount and fuel rate and output the new fuel amount
#int,int->int
def updateFuel(fuelAmount, fuelRate):
   newfuelAmount = fuelAmount - fuelRate
   return newfuelAmount

#Output a different text depending on the value of the velocity
#float->str
def displayLMLandingStatus(velocity):
   if -1 <= velocity <= 0:
      print ("Status at landing - The eagle has landed!")
   elif -10 < velocity < -1:
      print ("Status at landing - Enjoy your oxygen while it lasts!")
   elif velocity <= -10:
      print ("Status at landing - Ouch - that hurt!")

