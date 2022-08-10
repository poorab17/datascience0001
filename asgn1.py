"""
#1. Write a Python program which accepts the user's first and last name and prints them in
#reverse order with a space between them.

fname = input("Input your First Name : ")
lname = input("Input your Last Name : ")
print ("Hello  " + lname + " " + fname)"""

"""2. Write a Python program which accepts a sequence of comma-separated numbers from the
user and generates a list and a tuple with those numbers.
Sample data : 3, 5, 7, 23
Output :
List : ['3', ' 5', ' 7', ' 23']
Tuple : ('3', ' 5', ' 7', ' 23')

lst=['3','5','7','23']
print(lst)
tpl=('3','5','7','23')
print(tpl)"""

#3.Write a Python program to display the first and last colours from the following list.
#color_list = ["Red","Green","White" ,"Black"]

#color_list = ["Red","Green","White" ,"Black"]
#print(color_list[0] , color_list[-1])


"""4. Write a Python program to print the documents (syntax, description etc.) of Python built-in
function(s).
Sample function : abs()
Expected Result : mat
abs(number) -> number
Return the absolute value of the argument."""
 
#5. Write a Python program to print the calendar of a given month and year.
#Note : Use 'calendar' module.
#import calendar
#year=int(input("year: "))
#month=int(input("month: "))
#print(calendar.month(year,month))

#6. Write a Python program to calculate number of days between two dates.
#Sample dates : (2014, 7, 2), (2014, 7, 11)
#Expected output : 9 days

"""from datetime import date
f_date = date(2014, 7, 2)
l_date = date(2014, 7, 11)
delta = l_date - f_date
print(delta.days)"""

#7. Write a Python program to check whether a specified value is contained in a group of values.
#Test Data :
#3 -> [1, 5, 8, 3] : True
#-1 -> [1, 5, 8, 3] : False

"""def is_group_member(group_data, n):
   for value in group_data:
       if n == value:
           return True
   return False
print(is_group_member([1, 5, 8, 3], 3))
print(is_group_member([5, 8, 3], -1))"""

#8.Write a Python program to create a histogram from a given list of integers.

"""def histogram( items ):
    for n in items:
        output = ''
        times = n
        while( times > 0 ):
          output += '*'
          times = times - 1
        print(output)

histogram([2, 3, 6, 5])"""

#9. Write a Python program to concatenate all elements in a list into a string and return it.

"""def concatenate_list_data(list):
    result= ''
    for element in list:
        result += str(element)
    return result

print(concatenate_list_data([1, 5, 12, 2]))"""

#10. Write a Python program to print out a set containing all the colors from color_list_1 which are
#not present in color_list_2.
#Test Data :
#color_list_1 = set(["White", "Black", "Red"])
#color_list_2 = set(["Red", "Green"])
#Expected Output :{'Black', 'White'}

"""color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
print("Original set elements:")
print(color_list_1)
print(color_list_2)
print("\nDifferenct of color_list_1 and color_list_2:")
print(color_list_1.difference(color_list_2))
print("\nDifferenct of color_list_2 and color_list_1:")
print(color_list_2.difference(color_list_1))"""


#11. Write a Python program to check whether a file exists.

"""import os.path
print(os.path.isfile('main.txt'))
print(os.path.isfile('main.py'))

import os.path
print(os.path.exists('main.txt'))
print(os.path.exists('main.py'))

my_file = open('main.py')
try:
   my_file.close()
   print("File found!")
except FileNotFoundError:
   print("File not found!")"""

#12.Write a python program to call an external command in Python.

"""from subprocess import call
call(["ls", "-l"])

import os
print(os.system('ls -l'))

import psutil
print(psutil.cpu_count())"""

#13. Write a Python program to find out the number of CPUs using.

"""import multiprocessing
print(multiprocessing.cpu_count())"""

#14.Write a Python program to list all files in a directory in Python.

"""# import OS module
import os
 
# Get the list of all files and directories
path = "C://Users//DEEPAK//Documents//Datascience"
dir_list = os.listdir(path)
 
print("Files and directories in '", path, "' :")
 
# prints all files
print(dir_list)"""

#15. Write a python program to access environment variables.

"""import os
for data in os.environ:
   print(data)
   print('-'*15)
   print(os.environ[data])
   print('='*30)"""

#16. Write a Python program to get the current username

"""import getpass
print(getpass.getuser())"""

#17. Write a program to get execution time for a Python method

"""import time
def sum_of_n_numbers(n):
    start_time = time.time()
    s = 0
    for i in range(1,n+1):
        s = s + i
    end_time = time.time()
    return s,end_time-start_time

n = 5
print("\nTime to sum of 1 to ",n," and required time to calculate is :",sum_of_n_numbers(n))"""

#18. Write a Python program to get an absolute file path.

"""def absolute_file_path(path_fname):
        import os
        return os.path.abspath('path_fname')        
print("Absolute file path: ",absolute_file_path("test.txt"))"""

#19. Write a Python program to get file creation and modification date/times.

"""import os.path, time
print("Last modified: %s" % time.ctime(os.path.getmtime("test.txt")))
print("Created: %s" % time.ctime(os.path.getctime("test.txt")))"""

#19. Write a Python program to get file creation and modification date/times.

"""import os.path, time
print("Last modified: %s" % time.ctime(os.path.getmtime("test.txt")))
print("Created: %s" % time.ctime(os.path.getctime("test.txt")))"""

#20. Write a Python program to sort three integers without using conditional statements and
#loops.

"""x = int(input("Input first number: "))
y = int(input("Input second number: "))
z = int(input("Input third number: "))

a1 = min(x, y, z)
a3 = max(x, y, z)
a2 = (x + y + z) - a1 - a3
print("Numbers in sorted order: ", a1, a2, a3)"""

#21. Write a Python program to sort files by date

"""import glob
import os

files = glob.glob("*.txt")
files.sort(key=os.path.getmtime)
print("\n".join(files))"""

#22. Write a Python program to get the command-line arguments (name of the script, the number
#of arguments, arguments) passed to a script.

"""import sys
print("This is the name/path of the script:"),sys.argv[0]
print("Number of arguments:",len(sys.argv))
print("Argument List:",str(sys.argv))"""

#23. Write a Python program to find the available built-in modules.

"""import sys
import textwrap
module_name = ', '.join(sorted(sys.builtin_module_names))
print(textwrap.fill(module_name, width=70))"""

#24. Write a Python program to get the size of an object in bytes.

"""import sys
 
# Getting size using getsizeof() method and lately
# printing the same.
a = sys.getsizeof(12)
print(a)
 
b = sys.getsizeof('geeks')
print(b)
 
c = sys.getsizeof(('g', 'e', 'e', 'k', 's'))
print(c)
 
d = sys.getsizeof(['g', 'e', 'e', 'k', 's'])
print(d)
 
e = sys.getsizeof({1, 2, 3, 4})
print(e)
 
f = sys.getsizeof({1: 'a', 2: 'b', 3: 'c', 4: 'd'})
print(f)"""


#25. Write a Python program to get the current value of the recursion limit.

"""import sys
print()
print("Current value of the recursion limit:")
print(sys.getrecursionlimit())
print()"""

#26. Write a Python program to count the number occurrence of a specific character in a string.

"""# initializing string 
test_str = "deepak"
  
# using count() to get count 
# counting e 
counter = test_str.count('e')
  
# printing result 
print ("Count of e in GeeksforGeeks is : "
                           +  str(counter))"""

#27. Write a Python program to get the system time.

"""import datetime
now = datetime.datetime.now()
print ("Current date and time : ")
print (now.strftime("%Y-%m-%d %H:%M:%S"))"""

#28. Write a Python program to clear the screen or terminal.

"""import os
import time
# for windows
# os.system('cls')
os.system("ls")
time.sleep(2)
# Ubuntu version 10.10
os.system('clear')"""


#29. Write a Python program to get the name of the host on which the routine is running.

"""import socket
host_name = socket.gethostname()
print("Host name:", host_name)"""

#30. Write a Python program to access and print a URL's content to the console.

"""from http.client import HTTPConnection
conn = HTTPConnection("example.com")
conn.request("GET", "/")  
result = conn.getresponse()
# retrieves the entire contents.  
contents = result.read() 
print(contents)"""




