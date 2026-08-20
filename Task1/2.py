
# 2.1 Convert 145 to octal using format()
result = format(145, 'o')

print("\n2.1")
print("Octal representation of 145:", result)


# 2.2 Area of circular pond
radius = 84
pi = 3.14

area = pi * radius ** 2

print("\n2.2")
print("Area of pond:", area)

# Bonus: Calculate total water
water_per_square_meter = 1.4

total_water = area * water_per_square_meter

print("Total water:", int(total_water), "liters")


# 2.3 Calculate speed
distance = 490
time_minutes = 7

time_seconds = time_minutes * 60
speed = distance / time_seconds

print("\n2.3")
print("Speed:", int(speed), "m/s")