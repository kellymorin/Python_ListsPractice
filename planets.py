planet_list = ["Mercury", "Mars"]


# Use append() to add Jupiter and Saturn at the end of the list.
planet_list.append("Jupiter")
planet_list.append("Neptune")
print(planet_list)
# Use the extend() method to add another list of the last two planets in our solar system to the end of the list.
planet_list.extend(["Saturn", "Uranus"])
print(planet_list)
# Use insert() to add Earth, and Venus in the correct order.
other_planets = ["Earth", "Venus"]
for planet in other_planets:
  planet_list.insert(1, planet)
print(planet_list)
# Use append() again to add Pluto to the end of the list.
planet_list.append("Pluto")
print(planet_list)
# Now that all the planets are in the list, slice the list in order to get the rocky planets into a new list called rocky_planets.
rocky_planets = planet_list[slice(0, 4)]
print(rocky_planets)
# Being good amateur astronomers, we know that Pluto is now a dwarf planet, so use the del operation to remove it from the end of planet_list.
del planet_list[8]
print(planet_list)

# Challenge: Iterating over planets
# Create another list containing tuples. Each tuple will hold the name of a spacecraft that we have launched, and the names of the planet(s) that it has visited, or landed on. (e.g. ('Cassini', 'Saturn')).
satellites_and_planets = [("Europa Mission", "Jupiter"), ("Galileo", "Jupiter"), ("Hubble", "Mars"), ("InSight", "Mars"), ("Messenger", "Mercury"),("Hubble", "Neptune")]
# Iterate over your list of planets, and inside that loop, iterate over the list of tuples. Print, for each planet, which satellites have visited it.
for planet in planet_list:
    mission_match = list()
    for mission in satellites_and_planets:
        if mission[1] == planet:
            mission_match.append(mission[0])
    mission_details = (" & ").join(mission_match)
    if len(mission_details) != 0:
        print(f"{planet} was visited by {mission_details}")
