# This program show you the response for a question based on Magic Ball 8 game
import random

question = input("What is you question?:" )
resp = random.randint(1,8)

print(question)

if resp == 0:
    print("Very doubtful.")
elif resp == 1:
    print("Yes - definitely.")
elif resp == 2:
    print("It is decidedly so.")
elif resp == 3:
    print("Without a doubt.")
elif resp == 4:
    print("Reply hazy, try again.")
elif resp == 5:
    print("Ask again later.")
elif resp == 6:
    print("Better not tell you now.")
elif resp == 7:
    print("My sources say no.")
elif resp == 8:    
  print("Outlook not so good.")
else:
  # The random funtion generated a number are not between 0 and 8
  print("Error! The answer generated is invalid")




