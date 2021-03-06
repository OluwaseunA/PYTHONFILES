# In Dictionary each key is separated from its value by a colon (:), the items are separated by commas, and the whole thing is enclosed in curly braces. An empty dictionary without any items is written with just two curly braces, like this: {}.
#
# Keys are unique within a dictionary while values may not be. The values of a dictionary can be of any type, but the keys must be of an immutable data type such as strings, numbers, or tuples.
#
# Accessing Values in Dictionary
# To access dictionary elements, you can use the familiar square brackets along with the key to obtain its value. Following is a simple example −
#
# #!/usr/bin/python
#
# dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
# print (dict['Name'])
# print (dict['Age'])
# print (dict['Class'])
# print ("dict['Age']: ", dict['Age'])
# When the above code is executed, it produces the following result −
#
# dict['Name']:  Zara
# dict['Age']:  7
# If we attempt to access a data item with a key, which is not part of the dictionary, we get an error as follows −
#
# #!/usr/bin/python
#
# dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
# print "dict['Alice']: ", dict['Alice']
# When the above code is executed, it produces the following result −
#
# dict['Alice']:
# Traceback (most recent call last):
#    File "test.py", line 4, in <module>
#       print "dict['Alice']: ", dict['Alice'];
# KeyError: 'Alice'
# Updating Dictionary
# You can update a dictionary by adding a new entry or a key-value pair, modifying an existing entry, or deleting an existing entry as shown below in the simple example −
#
# #!/usr/bin/python
#
# dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
# dict['Age'] = 8; # update existing entry
# dict['School'] = "DPS School"; # Add new entry
#
# print("dict['Age']: ", dict['Age'])
# print ("dict['School']: ", dict['School'])
# When the above code is executed, it produces the following result −
#
# dict['Age']:  8
# dict['School']:  DPS School
# Delete Dictionary Elements
# You can either remove individual dictionary elements or clear the entire contents of a dictionary. You can also delete entire dictionary in a single operation.
#
# To explicitly remove an entire dictionary, just use the del statement. Following is a simple example −
#
# #!/usr/bin/python
#
# dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
# del dict['Name']; # remove entry with key 'Name'
# dict.clear();     # remove all entries in dict
# del dict ;        # delete entire dictionary
#
# print "dict['Age']: ", dict['Age']
# print "dict['School']: ", dict['School']
# This produces the following result. Note that an exception is raised because after del dict dictionary does not exist any more −
#
# dict['Age']:
# Traceback (most recent call last):
#    File "test.py", line 8, in <module>
#       print "dict['Age']: ", dict['Age'];
# TypeError: 'type' object is unsubscriptable
# Note − del() method is discussed in subsequent section.
#
# Properties of Dictionary Keys
# Dictionary values have no restrictions. They can be any arbitrary Python object, either standard objects or user-defined objects. However, same is not true for the keys.
#
# There are two important points to remember about dictionary keys −
#
# (a) More than one entry per key not allowed. Which means no duplicate key is allowed. When duplicate keys encountered during assignment, the last assignment wins. For example −
#
# #!/usr/bin/python
#
# dict = {'Name': 'Zara', 'Age': 7, 'Name': 'Manni'}
# print "dict['Name']: ", dict['Name']
# When the above code is executed, it produces the following result −
#
# dict['Name']:  Manni
# (b) Keys must be immutable. Which means you can use strings, numbers or tuples as dictionary keys but something like ['key'] is not allowed. Following is a simple example −
#
# #!/usr/bin/python
#
# dict = {['Name']: 'Zara', 'Age': 7}
# print "dict['Name']: ", dict['Name']
# When the above code is executed, it produces the following result −
#
# Traceback (most recent call last):
#    File "test.py", line 3, in <module>
#       dict = {['Name']: 'Zara', 'Age': 7};
# TypeError: list objects are unhashable

# dict1={'Name': 'Zara', 'Age':7, 'class': 'First'}
# print(dict1['Name'])
# dict1['school']="Univelcity"
# print(dict1)


dict1 = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
# dict1['Age'] = 8 # updating values
# dict1['School'] = "Univelsity" # adding key, value pair
# print(dict1)

# for i in dict1:
#     print(f'{i}-{dict1[i]}')
#
#
# print(dict1.keys())
# print(dict1.values())

# if 'Name' in dict1.keys():
#     print(dict1['Name'])


print(dict1.get('Name'))
print('Name' in dict1)

#
# list9=['1','2','3','4','5','6']
# print(dict(enumerate([list9])))


