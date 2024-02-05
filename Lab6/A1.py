# A1.Generate 100 random numbers between 101 and 200. Count the frequency of numbers in the different ranges
# [101-125,  126-150, 151-175, 176-200]

import random

range_101_125 = 0
range_126_150 = 0
range_151_175 = 0
range_176_200 = 0

for _ in range(100):
    random_number = random.randint(101, 200)

    if 101 <= random_number <= 125:
        range_101_125 += 1
    elif 126 <= random_number <= 150:
        range_126_150 += 1
    elif 151 <= random_number <= 175:
        range_151_175 += 1
    elif 176 <= random_number <= 200:
        range_176_200 += 1

print("Frequency in [101-125]:", range_101_125)
print("Frequency in [126-150]:", range_126_150)
print("Frequency in [151-175]:", range_151_175)
print("Frequency in [176-200]:", range_176_200)
