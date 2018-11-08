# a while loop evaluates a condtion and runs only if that condition remains True

# it's usually necessary to set the intitial state of the condition

count = 0

top = int(input("Please enter the number of times you want to run the loop:"))

while count < top:
    print("The condition is met, this is loop ", count + 1)
    count += 1
    
print("The condition is now False")
