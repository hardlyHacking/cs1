# lab4_checkpoint.py
# CS 1 Lab Assignment #3 checkpoint by THC.
# Reads in a file of information about world cities, stores each line
# into a City object, and then writes out the string representation of
# each City object into a file.
# Each line of the input file has the following fields, separated by commas:
#    1. A two-letter country code.
#    2. The name of the city.
#    3. A two-character region code.  The characters might be numeric,
#        alphabetical, or a combination.
#    4. The city's population, an integer.
#    5. The city's latitude, in degrees, a float.
#    6. The city's longitude, in degrees, a float.
# The format of the output file has the following fields, separated by commas:
#    1. The name of the city.
#    2. The city's population, an integer.
#    3. The city's latitude, in degrees, a float.
#    4. The city's longitude, in degrees, a float.

from city import City
from string import lower

# Load a csv file and return a list of City objects.
def load_cities(filename):
    cities = []     # start with an empty list
    f = open(filename, 'r') # get ready to read

    for line in f:  # read each line
        fields = line.strip().split(',')    # separate its contents
        cities.append(City(fields[0], fields[1], fields[2], int(fields[3]),
                      float(fields[4]), float(fields[5])))

    f.close()   # done with the file
    return cities

# Write information about City objects to a file.
def write_cities(cities, filename):
    outfile = open(filename, "w")   # get ready to write
    i = 0
    while i < len(cities):
        outfile.write(str(cities[i]) + "\n")    # write the next City object
        i += 1

    outfile.close()     # done writing   

cities = load_cities("world_cities.txt")
write_cities(cities, "cities_out.txt")
