#Data Types-: Data types are classifications that define the kind of data a variable can hold, influencing how it's stored and manipulated.
# in built function "type()" it tells the data type of any variable...

#types of data type in Pyhton:-
#Numeric  Data type
#   1=> integer 
x = 10
y = -3
print(type(x))#int
print(type(y))#int

#Decimal 
pi = 3.14
gravity = -9.8
print(type(pi))#float
print(type(gravity))#float

#Complex - imagnary number like as well as in mathematics...
#0 + 0j => always "j" it is an inbuilt
z = 2 + 3j
print(z.real) # here get real number..
print(z.imag) # here get imaginary number..
print(type(z))#complex


#   2 => Boolean
#true or false
is_active = True
is_logged_in = False
print(type(is_active)) #bool
print(type(is_logged_in)) #bool


#   3 => String 
#text data
name = "Alice"
greeting = 'Hello'
message = name + " says " + greeting
print(type(name))
print(type(greeting))
print(type(message))
print(message)


#    4 => Sequence 
#List - Ordered,changeable
fruits = ["apple", "banana", "cherry"]
fruits.append("orange") #using append it will store end of the list...
print(fruits)
print(type(fruits))#list
#tuple - Ordered,unchangeable
color = ("red","green","blue")
print(color[1])
print(color)
print(type(color))#tuple
#range - sequence of numbers
numbers = range(5)#here use inbuilt function which is "range()"
print(numbers)
print(list(numbers))
print(type(numbers))


#   5 => Mapping 
#dict - Key-value pairs
person = {"name":"Bob","age":30}
print(person)
print(person["name"])
print(type(person))#dict


#    6 => Set
#set - Unordered, no duplicates
unique_numbers = {1,2,3,4,5,4,3,2,6,7,0,0}
print(unique_numbers)
print(type(unique_numbers))
#frozenset - Immutable set
frozen = frozenset([1,2,3])
print(frozen)
print(type(frozen))


#    7 => None
#NoneType - No value
nothing = None
print(nothing) #None
print(type(nothing)) 
 