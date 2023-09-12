import math
Weight_Earth = 5.97600 * math.pow(10,24) 
#Weight_Moon = 7.347 * math.pow(10,22)  
G = 6.6743 * math.pow(10,-11)

question1 = int(input("enter weight the second planet:"))
question2 = int(input("enter distance before Moon in meters:"))

F = (G * Weight_Earth * question1) / (math.pow(question2, 2))
print(F)

#59_742_000_000_000_000_000_000
#384_400_000 