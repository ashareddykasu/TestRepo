''' nested If
If conditions inside if
take Aggregate input from user
Program to check grade
'''

numb =  int(input("Enter the marks aggregate"))

''' check if valid agregate is entered
'''

if (numb>0 and numb<100):
    if (numb>=90 and numb<=100) :
        print("grade A++")
    elif (numb>=80 and numb<90):
        print("Grade A+")
    elif (numb>=70 and numb <80) :
        print("Grade A")
    elif (numb>=60 and numb<70) :
        print("Grade B")
    elif numb<40:
        print("Grade F - fail")
		
else :
    print("Invalid Input")