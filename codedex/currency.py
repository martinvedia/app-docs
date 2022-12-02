# This program cal the value of your money in USD

yuans = float(input("insert yuans: "))
yens = float(input("insert yen: "))
wons = float(input("insert won: "))

result = (yuans * 0.15) + (yens * 0.0073 ) + (wons * 0.00075)
print(result)

