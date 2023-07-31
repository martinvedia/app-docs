# This program decide which house are you in HP schools bases on a questions
# This questions are solved by numbers to show the options

Gryffindor = 0
Ravenclaw = 0
Hufflepuff = 0
Slytherin = 0
q1_response = 0
q2_response = 0
q3_response = 0
q4_response = 0


# Question 1
while q1_response != 1 and q1_response != 2:
    print("Q1) Do you like Dawn or Dusk?")
    print("    1) Dawn")
    print("    2) Dusk")

    q1_response = int(input("Enter you Q1 answer: "))

    if q1_response != 1 and q1_response != 2:
        print ("Invalid input")

# Question 2
while q2_response != 1 and q2_response != 2 and q2_response != 3 and q2_response != 4:
    print("Q2) When I’m dead, I want people to remember me as:")
    print("    1) The Good")
    print("    2) The Great")
    print("    3) The Wise")
    print("    4) The Bold")

    q2_response = int(input("Enter you Q2 answer: "))

    if q2_response != 1 and q2_response != 2 and q2_response != 3 and q2_response != 4:
        print ("Invalid input")

# Question 3
while q3_response != 1 and q3_response != 2 and q3_response != 3 and q3_response != 4:
    print("Q3) Which kind of instrument most pleases your ear?")
    print("    1) The violin")
    print("    2) The trumpet")
    print("    3) The piano")
    print("    4) The drum")

    q3_response = int(input("Enter you Q3 answer: "))

    if q3_response != 1 and q3_response != 2 and q3_response != 3 and q3_response != 4:
        print ("Invalid input")


# Question 1 response calc:
if q1_response == 1:
    Gryffindor = Gryffindor + 1
    Ravenclaw = Ravenclaw + 1
elif q1_response == 2:
    Hufflepuff = Hufflepuff + 1
    Slytherin = Slytherin + 1
else:
    print("Invalid input")


Gryffindor = Gryffindor + 1
Ravenclaw = Ravenclaw + 1
Hufflepuff = Hufflepuff + 1
Slytherin = Slytherin + 1

# Question 2 response calc:
if q2_response == 1:
    Hufflepuff = Hufflepuff + 1
elif q2_response == 2:
    Slytherin = Slytherin + 1
elif q2_response == 3:
    Ravenclaw = Ravenclaw + 1
elif q2_response == 4:
    Gryffindor = Gryffindor + 1
else:
    print("Invalid input")


# Question 3 response calc:
if q3_response == 1:
    Slytherin = Slytherin + 1
elif q3_response == 2:
    Hufflepuff = Hufflepuff + 1
elif q3_response == 3:
    Ravenclaw = Ravenclaw + 1
elif q3_response == 4:
    Gryffindor = Gryffindor + 1
else:
    print("Invalid input")

print("Your house is: ")
if  Slytherin >= Hufflepuff and Slytherin >= Ravenclaw and Slytherin >= Gryffindor:
    print("Slytherin")
elif Hufflepuff >= Slytherin and Hufflepuff >= Ravenclaw and Hufflepuff >= Gryffindor:
    print("Hufflepuff")
elif Ravenclaw >= Slytherin and Ravenclaw >= Slytherin and Ravenclaw >= Gryffindor:
    print("Ravenclaw")
else: 
    print("Gryffindor")