#3. Use the if statement conditions to write a program to print the letter grade based on an input class score. Use the grading scheme we are using in this class
marks = int(input("Enter the marks secured: "))

if marks >= 90:
    print("A")
elif marks >= 80 and marks < 90:
    print("B")
elif marks >=70 and marks < 80:
    print("C")
elif marks >=60 and marks < 70:
    print("D")

else:
    print("F")
 
