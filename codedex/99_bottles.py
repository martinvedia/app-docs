# This program show the song of "99 bottles"

for x in range (100):
        bottles = 99 - x
        print(bottles, "bottles of beer on the wall")
        print(bottles, "bottles of beer")
        print("Take one down, pass it around")


# Another option

for x in range (99, 0, -1):
        print(x, "bottles of beer on the wall")
        print(x, "bottles of beer")
        print("Take one down, pass it around")
        print(x-1, "bottles of beer on the wall")

# End