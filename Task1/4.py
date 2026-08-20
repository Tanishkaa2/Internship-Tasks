#4.1 BMI Calculator

print("\n4.1 BMI Calculator")

height = float(input("Enter height in meters: "))
weight = float(input("Enter weight in kilograms: "))

bmi = weight / (height ** 2)

print("BMI:", bmi)

if bmi >= 30:
    print("Obesity")
elif bmi >= 25:
    print("Overweight")
elif bmi >= 18.5:
    print("Normal")
else:
    print("Underweight")
    # 4.2 Determine country from city

print("\n4.2 City and Country")

Australia = ["Sydney", "Melbourne", "Brisbane", "Perth"]
UAE = ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"]
India = ["Mumbai", "Bangalore", "Chennai", "Delhi"]

city = input("Enter a city name: ")

if city in Australia:
    print(city, "is in Australia")
elif city in UAE:
    print(city, "is in UAE")
elif city in India:
    print(city, "is in India")
else:
    print("City not found")


# 4.3 Check if two cities belong to the same country

print("\n4.3 Check Same Country")

city1 = input("Enter the first city: ")
city2 = input("Enter the second city: ")

country1 = None
country2 = None

if city1 in Australia:
    country1 = "Australia"
elif city1 in UAE:
    country1 = "UAE"
elif city1 in India:
    country1 = "India"

if city2 in Australia:
    country2 = "Australia"
elif city2 in UAE:
    country2 = "UAE"
elif city2 in India:
    country2 = "India"

if country1 is None or country2 is None:
    print("One or both cities were not found.")
elif country1 == country2:
    print("Both cities are in", country1)
else:
    print("They don't belong to the same country")