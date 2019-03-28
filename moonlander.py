#Project 2: Lunar Lander Simulator
#
#Name: Rohith Dara
#Instructor: S. Einakian
#Section: 01

from landerFuncs import *

#Run the entire moonlander function to determine final landing safety
# ->
def main():
	showWelcome()
	gravity = 1.62
	velocity = 0.00
	elapsedTime = 0
	velocity = 0.00
	altitude = getAltitude()
	fuelAmount = getFuel()
	fuelRate = 0

	print()
	print("LM state at retrorocket cutoff")

	while altitude > 0.0:
		if fuelAmount > 0:
			displayLMState(elapsedTime,altitude,velocity,fuelAmount,fuelRate)
			print()
			elapsedTime += 1
			currentFuel = fuelAmount
			fuelRate = getFuelRate(currentFuel)
			acceleration = updateAcceleration(gravity, fuelRate)
			altitude = updateAltitude(altitude, velocity, acceleration)
			velocity = updateVelocity(velocity, acceleration)
			fuelAmount = updateFuel(fuelAmount, fuelRate)

		else:
			print(("OUT OF FUEL - Elapsed Time:") + ("%4d"% elapsedTime) + (" Altitude:") + ("%5.2f"% altitude) + (" Velocity:") + ("%5.2f"% velocity))
			fuelRate = 0
			acceleration = updateAcceleration(gravity, fuelRate)
			altitude = updateAltitude(altitude, velocity, acceleration)
			velocity = updateVelocity(velocity, acceleration)
			fuelAmount = updateFuel(fuelAmount,fuelRate)
			elapsedTime += 1
		
	altitude = 0
	print()		
	print("LM state at landing/impact")
	displayLMState(elapsedTime,altitude,velocity,fuelAmount,fuelRate)
	print()
	displayLMLandingStatus(velocity)

   

if __name__ == "__main__":
   main()

