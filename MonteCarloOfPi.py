"""
Program: Monte Carlo Simulation: Approximation of Pi
Author: Riyam Arabo
Last Modified: 9/11/2018

Purpose:
Getting as close as possible to the pi measurement of 3.14159 by using a rain drop simulation

Method:
1. Visualize that a circle is inside a square and it is touching all of its four sides.
2. Assume that the circle has a radius = 1 and the square has sides equal to 2 (or 2r)
3. Use the following formula to calculate the probability of rain falling inside vs outside the circle
    probability of rain = (area of circle pi*r^2) / (area of square 4r^2)
    We can cancel the r^2 to simplify the equation: p = pi/ 4
    Then we isolate pi on one side of the equation to prove that the rain drops probability can approximate to pi: 4*p = pi
    In the simulation, we will divide number of drops inside the circle (which represent circle's area) by the rain drops inside the square (which represents square's) then we multiply the total by 4 to achieve the top equation
4. The program will simulate rain drops until we reach the approximation of pi = 3.14159
5. The program will rerun the simulations 10 times (rainy days), and calculates the average rain drops needed to reach pi and the average run time
"""
import random
import time

# the values will hold totals to calculate the averages at the end of the program
totalRainDrops = 0
totalRainTime = float(0)

# simulating the raining for "10 days"
for days in range(1, 11):

    # initializing the rain drops inside the circle, the square, and the probability of c/s
    c, s, p = float(0), float(0), float(0)
    rainDrops = 0

    # takes a time stamp of the start each iteration of rain drops
    startTime = time.time()

    #  approximate pi to 5 digits precision
    while p != 3.14159:

        # use x and y coordinates to measure whether the drops fell in or out of the circle
        x, y = random.uniform(0.0, 1.0), random.uniform(0.0, 1.0)

        # each time a rain drops, the number of drops inside the square increases
        s += 1

        # determine whether it falls inside the circle using its formula, if yes, increment it
        if (x**2) + (y**2) <= 1:
            c += 1

        # we calculate the probability and precise it to 5 digits
        p = round((c/s) * 4, 5)

        # how many rain drops needed to approximate pi = 3.14159
        rainDrops += 1

    rainTimePerDay = time.time() - startTime  # calculates how long it took to rain to reach pi = 3.14159
    totalRainTime += rainTimePerDay  # how long did it rain in all simulations
    totalRainDrops += rainDrops  # how many rain drops in all simulations

    print("Rain Day:  " + str(days))
    print("total rain drops for day " + str(days) + ": " + str(rainDrops))
    print("total rain drops in all " + str(days) + " days: " + str(totalRainDrops))

avgRainPerDay = float(totalRainDrops / days)
avgRainTime = totalRainTime / days

print("Average number of rain drops per day: " + str(avgRainPerDay))
print("Total Rain Time: " + str(totalRainTime) + "\nAverage Rain Time per day: " + str(avgRainTime))

