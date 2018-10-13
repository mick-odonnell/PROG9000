# Euclidean Distance Calculator

x1 = int(input("Please enter x1"))
y1 = int(input("Please enter y1"))
x2 = int(input("Please enter x2"))
y2 = int(input("Please enter y2"))

dist = ((x2 - x1)**2 - (y2 - y1)**2)**0.5

print("The Euclidean Distance between points ("
      , x1, ",", y1, ") and (", x2, ",", y2, ") is", dist)