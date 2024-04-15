def get_vowels(String):
    return [each for each in String if each in "aeiou"]
get_vowels("animal") # [a, i, a]
get_vowels("sky") # []
get_vowels("football") # [o, o, a]

def capitalize(String):
    return String.title()
capitalize("shop") # [Shop]
capitalize("python programming") # [Python Programming]
capitalize("how are you!") # [How Are You!]

n=5
string="Hello World "
print(string * n)  #Hello World Hello World Hello World Hello World Hello World

def merge(dic1,dic2):
    dic3=dic1.copy()
    dic3.update(dic2)
    return dic3
dic1={1:"hello", 2:"world"}
dic2={3:"Python", 4:"Programming"}
merge(dic1,dic2) # {1: 'hello', 2: 'world', 3: 'Python', 4: 'Programming'}

import time
start_time= time.time()
def fun():
    a=2
    b=3
    c=a+b
end_time= time.time()
fun()
timetaken = end_time - start_time
print("Your program takes: ", timetaken) # 0.0345

a=3
b=4
a, b = b, a
print(a, b) # a= 4, b =3


def check_duplicate(lst):
    return len(lst) != len(set(lst))
check_duplicate([1,2,3,4,5,4,6]) # True
check_duplicate([1,2,3]) # False
check_duplicate([1,2,3,4,9]) # False

def Filtering(lst):
    return list(filter(None,lst))
lst=[None,1,3,0,"",5,7]
Filtering(lst) #[1, 3, 5, 7]

def ByteSize(string):
    return len(string.encode("utf8"))
ByteSize("Python") #6
ByteSize("Data") #4

import sys
var1="Python"
var2=100
var3=True
print(sys.getsizeof(var1)) #55
print(sys.getsizeof(var2)) #28
print(sys.getsizeof(var3)) #28

from collections import Counter
def anagrams(str1, str2):
    return Counter(str1) == Counter(str2)
anagrams("abc1", "1bac") # True

my_list = ["leaf", "cherry", "fish"]
my_list1 = ["D","C","B","A"]
my_list2 = [1,2,3,4,5]

my_list.sort() # ['cherry', 'fish', 'leaf']
my_list1.sort() # ['A', 'B', 'C', 'D']
print(sorted(my_list2, reverse=True)) # [5, 4, 3, 2, 1]

orders = {
 'pizza': 200,
 'burger': 56,
 'pepsi': 25,
    'Coffee': 14
}
sorted_dic= sorted(orders.items(), key=lambda x: x[1])
print(sorted_dic)  # [('Coffee', 14), ('pepsi', 25), ('burger', 56), ('pizza', 200)]

my_list = ["Python", "JavaScript", "C++", "Java", "C#", "Dart"]
#method 1
print(my_list[-1])  # Dart
#method 2
print(my_list.pop()) # Dart

my_list1=["Python","JavaScript","C++"]
my_list2=["Java", "Flutter", "Swift"]
#example 1
"My favourite Programming Languages are" , ", ".join(my_list1)) # My favourite Programming Languages are Python, JavaScript, C++
print(", ".join(my_list2))  # Java, Flutter, Swift

def palindrome(data):
    return data == data[::-1]
    
palindrome("level") #True
palindrome("madaa") #False

from random import shuffle
my_list1=[1,2,3,4,5,6]
my_list2=["A","B","C","D"]
shuffle(my_list1) # [4, 6, 1, 3, 2, 5]
shuffle(my_list2) # ['A', 'D', 'B', 'C']

str1 ="Python Programming"
str2 ="IM A PROGRAMMER"
print(str1.upper()) #PYTHON PROGRAMMING
print(str2.lower()) #im a programmer

programmers = ["I'm an expert Python Programmer",
               "I'm an expert Javascript Programmer",
               "I'm a professional Python Programmer"
               "I'm a beginner C++ Programmer"
]
#method 1
for p in programmers:
    if p.find("Python"):
        print(p)
#method 2
for p in programmers:
    if "Python" in p:
        print(p)
