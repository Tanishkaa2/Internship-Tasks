# 5.1 Roll a six-sided die 20 times

import random

six_count = 0
one_count = 0
two_sixes = 0

previous_roll = 0

print("\n5.1 Dice Rolling")

for i in range(20):

    roll = random.randint(1, 6)

    print("Roll", i + 1, ":", roll)

    if roll == 6:
        six_count += 1

    if roll == 1:
        one_count += 1

    if roll == 6 and previous_roll == 6:
        two_sixes += 1

    previous_roll = roll

print("\nStatistics:")
print("Number of times 6 was rolled:", six_count)
print("Number of times 1 was rolled:", one_count)
print("Number of times two 6s occurred in a row:", two_sixes)

# 5.2 Jumping Jacks Workout

print("\n5.2 Jumping Jacks Workout")

total = 0

for i in range(10):

    total += 10

    print("\nYou completed", total, "jumping jacks.")

    if total == 100:
        print("Congratulations! You completed the workout.")
        break

    tired = input("Are you tired? (yes/no): ").lower()

    if tired == "yes" or tired == "y":

        skip = input(
            "Do you want to skip the remaining sets? (yes/no): "
        ).lower()

        if skip == "yes" or skip == "y":
            print("You completed a total of", total, "jumping jacks.")
            break

    remaining = 100 - total

    print(remaining, "jumping jacks remaining.")