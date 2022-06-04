https://techvidvan.com/tutorials/python-sequences/#:~:text=In%20Python%20programming%2C%20sequences%20are,byte%20arrays%2C%20and%20range%20objects.

Python Sequences
In Python programming, sequences are a generic term for an ordered set which means that the order in which we input the items will be the same when we access them.

Python supports six different types of sequences. These are strings, lists, tuples, byte sequences, byte arrays, and range objects. We will discuss each of them.

Types of Python Sequences
Python Strings
Strings are a group of characters written inside a single or double-quotes. Python does not have a character type so a single character inside quotes is also considered as a string.

Code:

name = “TechVidvan”
type(name)

Strings are immutable in nature so we can reassign a variable to a new string but we can’t make any changes in the string.

Code:

city= ‘China’
print(city[2])
city[2] = ‘a’
Output:

Traceback (most recent call last):
  File “<stdin>”, line 3, in <module>
TypeError: ‘str’ object does not support item assignment

Python Lists
Python lists are similar to an array but they allow us to create a heterogeneous collection of items inside a list. A list can contain numbers, strings, lists, tuples, dictionaries, objects, etc.

Lists are declared by using square brackets around comma-separated items.

Syntax:

list1 = [1,2,3,4]
list2 = [‘red’, ‘green’, ‘blue’]
list3 = [‘hello’, 100, 3.14, [1,2,3] ]
Lists are mutable which makes it easier to change and we can quickly modify a list by directly accessing it.

Code:

list = [10,20,30,40]
list[1] = 100
print( list)
Output:

[10, 100, 30, 40]

Python Tuples
Tuples are also a sequence of Python objects. A tuple is created by separating items with a comma. They can be optionally put inside the parenthesis () but it is necessary to put parenthesis in an empty tuple.

A single item tuple should use a comma in the end.

Code:

tup = ()
print( type(tup) )
tup = (1,2,3,4,5)
tup = ( “78 Street”, 3.8, 9826 )
print(tup)
Output:

<class ‘tuple’>
(’78 Street’, 3.8, 9826)
Tuples are also immutable like strings so we can only reassign the variable but we cannot change, add or remove elements from the tuple.

Code:

tup = (1,2,3,4,5)
tup[2] = 10
Output:

Traceback (most recent call last):
  File “<stdin>”, line 2, in <module>
TypeError: ‘tuple’ object does not support item assignment

Bytes Sequences in Python
The bytes() function in Python is used to return an immutable bytes sequence. Since they are immutable, we cannot modify them.

If you want a mutable byte sequence, then it is better to use byte arrays. This is how we can create a byte of a given integer size.

Code:

size = 10
b = bytes(size)
print( b )
Output:

b’\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00′
Iterables can be converted into bytes.

Code:

print( bytes([4,2,1]) )
Output:

b’\x04\x02\x01′
For strings, we have to provide the encoding in the second parameter.

Code:

bytes(“Hey”, ‘utf=8’)
Output:

b’Hey’
Byte Arrays in Python
Byte arrays are similar to bytes sequence. The only difference here is that byte arrays are mutable while bytes sequences are immutable. So, it also returns the bytes object the same way.

Code:

print( bytearray(4) )
print( bytearray([1, 2, 3, 4]) )
print( bytearray(‘Hola!’, ‘utf-8’))
Output:

bytearray(b’\x00\x00\x00\x00′)
bytearray(b’\x01\x02\x03\x04′)
bytearray(b’Hola!’)
Since byte arrays are mutable, let’s try changing a byte from the array.

Code:

a = bytearray([1,3,4,5])
print(a)
a[2] = 2
print(a)
Output:

bytearray(b’\x01\x03\x04\x05′)
bytearray(b’\x01\x03\x02\x05′)

ython range() objects
range() is a built-in function in Python that returns us a range object. The range object is nothing but a sequence of integers. It generates the integers within the specified start and stop range.

Let’s see this with an example.

Code:

num = range(10)
print( type(num) )
Output:

<class ‘range’>
Since range object generates integers, we can access them by iterating using a for loop.

Code:

for i in range(5):
  print(i)
Output:

0
1
2
3
4
The first argument is the starting range, the second argument is the stopping range and the third argument tells how many steps to take.

Code:

for i in range(4,16,2):
  print()
Output:

4
6
8
10
12
14
Operations on Python Sequences
