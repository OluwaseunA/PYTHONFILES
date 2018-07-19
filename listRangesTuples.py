import csv
flightsFile = open("flights.csv")
reader = csv.reader(flightsFile)
for item in reader:
    origin, destination, duration = item
    print(f"Origin: {origin}, destination: {destination}, duration: {duration}")


#list is defined as a homogenous group of items although
#in practice homogenity is not actually enforced

#to create
# list_1 = [] #list literal
# list_2 = list()  #list function

# #to create a list of string and items to it
# list_1.append("eggs")
# list_1.append("spam")
# list_1.append("milk")
# list_1.append("bacon")
# list_1.append("cheese")
# list_1.append("butter")
#
# list_1=['egg','spam','milk']
# print(len(list_1))#to get the length of a list
# print(list_1[0])#to get an item in a list
# print(list_1.index('spam'))#to get the position of an item in a list
# for item in list_1: # to iterate through a list
#     print('The item position is {} and the item is {}'.format(list_1.index(item),item))
#
# list_2.append(2)
# list_2.append(4)
# list_2.append(6)
# list_2.append(8)
# list_2.append(10)
#
# list_2=[2,4,6,8,10]


# list_3=list(range(1,10,2))
# list_4=list(range(2,10,2))
# #print(list_3)
# numbers = list_2 + list_3
# numbers.sort() # arranges the list in ascending order
# print(numbers)


# print(list_1)
# print(list_2)



menu = [
            ['egg','butter','bacon'],
            ['egg','cheese','bacon','beef'],
            ['egg','spam','spam','bacon'],
            ['egg','spam','spam','spam','spam','bacon','cheese'],
            ['egg','spam'],
            ['egg','egg','bacon','cheese'],
        ]

# for meal in menu:
#     if 'spam' in meal:
#         continue
#     else:
#         print(meal)
#     for ingredient in meal:
#         print(ingredient)

# for meal in menu:
#     if 'spam' in meal:
#         print(meal)
#     else:
#         continue

# for meal in menu:
#     if 'bacon' in meal:
#         continue
#     else:
#         print(meal)

#list equality
# if list_2 == list_3:
#     print(True)
# else:
#     print(False)
#
# if list_2 > list_4:
#     print(True)
# else:
#     print(False)

#CREATING A DYNAMIC LIST
# sevens  = list()#list of numbers that are multiples of 7
# eights = []#list of numbes that are multiples of 8
#
# first_100_number = list(range(1, 101))
# # print(first_100_number)

# for num in first_100_number:
#     if num % 7 == 0:
#         sevens.append(num)
#     elif num % 8 == 0:
#         eights.append(num)
#     else:
#         continue
# print(sevens)
# print(eights)

#Challenges
#create a list of all even numbers from 2 - 50
# create a list of all odd numbers from 1-50
# iterate through the list of even numbers and find their sum
# iterate through the list of odd numbers and find their sum
# (HINT: do research on the internet for this)
# from the menu list above write a program to print out list without 'bacon'

# list_1 = list(range(2,51,2))
# list_2 = list(range(1,50,2))
# sum=0
#
# for i in list_1:
#     sum += i
# print(sum)
#
# for i in list_2:
#     sum+=i
# print(sum)

#it can be done this way too
# sum_even_numbers_list = sum(list_1)
# print(sum_even_numbers_list)


# list_1= ["eggs","spam","milk","bacon","cheese","butter"]
# # for item in list_1:
# #     print(f"The item position is{list_1.index(item)}and the item name is {item}")
#
# list_1[4] = "Peanut Butter"
# del list_1[4]
# print(list_1)
#
# print(list_1.
# list_1.sort()
# list_1.reverse() # to print in descending order
# print(list_1)

"""Challenge is to sort a list and print the reverse order
Class challenge: create a list ten books you know, sort them in their correct order
loop through the books and print put the book name and index
"""
#
# Books=["The gods","time","The secret of wealth","Word","Dont ask why",
#        "Think Big","Forcados","Oliver Twist","Earth","Yellow Sun"]
# Books.sort()
# print(Books)
# for i in Books:
#     print(f"The Book {i} ranks {Books.index(i)} on the list")
#
# first_100_numbers = list(range(1, 101))
#
# for num in first_100_numbers:
#     if









#TUPLES
# tuple_1 =[]
# tuple_1 = tuple()
#
# tuple_3 = (
#     ("olamide","who you epp",2016)
#     ("tiwa savage", "badd", 2014)
#     ("davido","fia",2017),
#     ("kiss Daniel","no do",2018)
# )
# for item in tuple_3:
#     name, title, year = item #this is known as UNPACKING
#     print(f"Artist: {name}, Song title: {title}, Year: {year} ")
#
#
# name, title, year = ("olamide","badoo",2016)
# print(name)
# print(year)
