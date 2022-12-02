# This program show is the PH ingresed is Acid, Base or Neutral
import random

ph = random.randint(1,14)

if ph > 7:
  print("Basic")
elif ph < 7:
  print("Acid")
else:
  print("Neutral")