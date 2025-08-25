#Conditional statements
Marks=int(input("Marks:"))
if(Marks>100):
    print("Error")
elif(Marks>=90 and Marks<=100):
    print("O")
elif(Marks>=80 and Marks<90):
    print("A")
elif(Marks>=70 and Marks<80):
    print("B")
elif(Marks>=60 and Marks<70):
    print("C")
else:
    print("F")