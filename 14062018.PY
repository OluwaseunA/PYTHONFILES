"""
# Please read each carefully and select the correct answers
# If the question invloves writing programs please make these as clear and simple as possible
# """

# # 1. The following program contains an error.  
# # Examine the code carefully, and work out which line is incorrect:

# print("Python was created by Guido van Rossum.")
# print("He's referred to as the BDFL,")
# print("the "Benevolent Dictator For Life"")
# print("and has the final word when it comes to enhancements to Python.")

# # 2. In this program, 2 of the variables will have the same value

# meal1 = "spam" + "eggs" + "beans"
# meal2 = "spam\neggs\nbeans"
# meal3 = "spam, eggs, beans"
# meal4 = """spam eggs beans"""

# print(meal1)
# print(meal2)
# print(meal3)
# print(meal4)

# 3. What will be the output produced by this line?

# print("Terry\tJohn\tGraham\tMichael\tEric\tTerry")

# # 4. What will be the output of this program?

# first_name = "John"
# last_name = "Cleese"
# age = 78

# print(first_name + last_name + age)


# #  What result will this program print?

# a = 45
# b = 15
# c = 3
 
# print(a - b / c)


# """  A banker earns a sum of 5,000 monthly pays tax 
# of 5% of his total salary at th end of the month. Write a program to 
# determine and display how much he will be left with at the end of the month after tax
# Note: Plesse declare all your variables clearly

# """


# # slicing and formatting


# parrot = "Norwegian Blue"

# # slicing methods
# print(parrot[:]) #prints complete string in parrot
# print(parrot[0:6]) #prints Norweg 				it counts from 0 and take away -1
# print(parrot[0:6:2]) #prints Nre {[start:End:step]}
# print(parrot[0::6]) #prints Niu
# print(parrot[:6])	#prints Norweg
# print(parrot[:6:2])	#prints Nre
# print(parrot[::2])	#prints NreinBu


# # string formatting and replacement fields


# first_name = "isaiah"
# last_name = "iyede"
# age = 30
# type_of_food = "amala"

# print("My name is {1} {0} and i am {2} years old and i like {3}".format(first_name, last_name, age, type_of_food))
	#this code prints according to to the podition each variable is placed

MyString = "abcdef"		#-1 stands for f counting backwards
print(-len(MyString)-1) #for determining the length of a string
print(MyString[-1::-1]) #prints my string backwards

# # -len(parrot)-1

print(MyString[-1:-len(MyString)-2:-1]) 

# # conditional flow of programs of python

# a = 12
# b = 5

# if a % b > 3:
# 	print(True)
# elif a % b == 2:
# 	print("This is the correct answer")
# else:
# 	print(False)





























