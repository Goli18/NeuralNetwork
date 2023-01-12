#Input the string “Python” as a list of characters from console, delete at least 2 characters, reverse the resultant string and print it.

# Taking input string from the console
string=input("Enter the string:")

# Creating an empty string list
strList = []

# Fill the list with individual characters
strList[:0] = string

#print the 
print(" string list:", strList)

#deleting atleast two characters
strList.pop(3)
strList.pop(4)

#Reversing the list
strList.reverse()

# create a blank string then iterate through strList
result = ""
for i in strList:
    # appends the list values to the string
    result = result+i
    
# printing the final string
print(result)


