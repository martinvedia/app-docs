# For multiples of 3, print "Fizz" instead of the number.
# For multiples of 5, print "Buzz" instead of the number.
# Here's the tricky part: For multiples of 3 and 5, print "FizzBuzz".


for x in range(1, 101, 1):
    if ((x % 3) ==0) and ((x % 5) == 0):
            print ("FizzBuzz")
    elif (x % 3) == 0:
            print("Fizz")
    elif (x % 5) == 0:
        print("Buzz")
    else:
        print (x)


    