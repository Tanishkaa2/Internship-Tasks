justice_league = [
    "Superman",
    "Batman",
    "Wonder Woman",
    "Flash",
    "Aquaman",
    "Green Lantern"
]

# 3.1 Calculate number of members
print("\n3.1")
print("Justice League:", justice_league)
print("Number of members:", len(justice_league))


# 3.2 Add Batgirl and Nightwing
justice_league.append("Batgirl")
justice_league.append("Nightwing")

print("\n3.2")
print("After adding Batgirl and Nightwing:")
print(justice_league)


# 3.3 Move Wonder Woman to the beginning
justice_league.remove("Wonder Woman")
justice_league.insert(0, "Wonder Woman")
print("\n3.3")
print("After moving Wonder Woman to the beginning:")
print(justice_league)


# 3.4 Move Green Lantern between Aquaman and Flash
justice_league.remove("Green Lantern")

aquaman_index = justice_league.index("Aquaman")
justice_league.insert(aquaman_index + 1, "Green Lantern")

print("\n3.4")
print("After moving Green Lantern between Aquaman and Flash:")
print(justice_league)


# 3.5 Replace the existing list
justice_league = [
    "Cyborg",
    "Shazam",
    "Hawkgirl",
    "Martian Manhunter",
    "Green Arrow"
]

print("\n3.5")
print("New Justice League:")
print(justice_league)


# 3.6 Sort alphabetic
justice_league.sort()

print("\n3.6")
print("Sorted Justice League:")
print(justice_league)

print("New leader:", justice_league[0])