#ARRAY 
#1. Write a Python program to create an array of 5 integers and display the array items.
#Access individual element through indexes.

"""from array import *
array_num = array('i', [1,3,5,7,9])
for i in array_num:
    print(i)
print("Access first three items individually")
print(array_num[0])
print(array_num[1])
print(array_num[2])"""

#2. Write a Python program to reverse the order of the items in the array

"""from array import *
array_num = array('i', [1, 3, 5, 3, 7, 1, 9, 3])
print("Original array: "+str(array_num))
array_num.reverse()
print("Reverse the order of the items:")
print(str(array_num))"""

#3. Write a Python program to get the number of occurrences of a specified element in an
#array.

"""from array import *
array_num = array('i', [1, 3, 5, 3, 7, 9, 3])
print("Original array: "+str(array_num))
print("Number of occurrences of the number 3 in this array: "+str(array_num.count(3)))"""

#4. Write a Python program to remove the first occurrence of a specified element from an
#array.

"""from array import *
array_num = array('i', [1, 3, 5, 3, 7, 1, 9, 3])
print("Original array: "+str(array_num))
print("Remove the first occurrence of 3 from this array:")
array_num.remove(3)
print("New array: "+str(array_num))"""

#DICTIONARY

#1. Write a Python script to sort (ascending and descending) a dictionary by
#value.

"""import operator
d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
print('Original dictionary : ',d)
sorted_d = sorted(d.items(), key=operator.itemgetter(1))
print('Dictionary in ascending order by value : ',sorted_d)
sorted_d = dict( sorted(d.items(), key=operator.itemgetter(1),reverse=True))
print('Dictionary in descending order by value : ',sorted_d)"""

#2. Write a Python script to add a key to a dictionary

"""d = {0:10, 1:20}
print(d)
d.update({2:30})
print(d)"""

#3. Write a Python script to concatenate following dictionaries to create a new
"""one.
Sample Dictionary :
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}"""

"""dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
dic4 = {}
for d in (dic1, dic2, dic3): dic4.update(d)
print(dic4)"""

#4. Write a Python program to iterate over dictionaries using for loops.

"""d = {'Red': 1, 'Green': 2, 'Blue': 3} 
for color_key, value in d.items():
     print(color_key, 'corresponds to ', d[color_key])"""


#5. Write a Python script to generate and print a dictionary that contains a
#number (between 1 and n) in the form (x, x*x)

"""n=int(input("Input a number "))
d = dict()

for x in range(1,n+1):
    d[x]=x*x

print(d)"""

#6. Write a Python program to remove a key from a dictionary.

"""student_list = {'S  001': ['Math', 'Science'], 'S    002': ['Math', 'English']}
print("Original dictionary: ",student_list)
student_dict = {x.translate({32: None}): y for x, y in student_list.items()}
print("New dictionary: ",student_dict)"""

#7. Write a Python program to print all unique values in a dictionary.
#Sample Data : [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}

"""L = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
print("Original List: ",L)
u_value = set( val for dic in L for val in dic.values())
print("Unique Values: ",u_value)"""

#8. Write a Python program to create a dictionary from a string.
#Note: Track the count of the letters from the string

from collections import defaultdict, Counter
str1 = 'w3resource' 
my_dict = {}
for letter in str1:
    my_dict[letter] = my_dict.get(letter, 0) + 1
print(my_dict)

























