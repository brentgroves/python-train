https://learnpython.com/blog/python-match-case-statement/

Switch Case in Python
In Python 3.10 and after that, Python will support this by using match in place of switch:

>>> command = 'Hello, World!'
>>> match command:
...     case 'Hello, World!':
...         print('Hello to you too!')
...     case 'Goodbye, World!':
...         print('See you later')
...     case other:
...         print('No match found')
 
Hello to you too!

def number_to_string(argument):
    match argument:
        case 0:
            return "zero"
        case 1:
            return "one"
        case 2:
            return "two"
        case default:
            return "something"
 
 Why Use a match case Statement?
The example above can just as easily be implemented with an if-elif-else statement. In this section, we’ll see two more examples of how using match case can simplify your flow control statements, making them more readable and less prone to errors. 

Say we want to write a script to handle a large number of files. We can write the following function:

>>> def file_handler_v1(command):
...     match command.split():
...         case ['show']:
...             print('List all files and directories: ')
...             # code to list files
...         case ['remove', *files]:
...             print('Removing files: {}'.format(files))
...             # code to remove files
...         case _:
...             print('Command not recognized')
The input is again a string which gets split at white space using command.split(). This returns a list of strings. (By the way, if you are wondering what the difference between lists and arrays is, we explain it in THIS ARTICLE.) The first case is matched when the value  of command is 'show', for which the split() method returns the list ['show'].  Then code to list all files in a particular directory gets executed. Here we just have the code to be executed indicated by comments; in reality, you could use the OS module to implement the required functionality.

The second case is more interesting. Here’s an example:

>>> file_handler_v1('remove file1.txt file2.jpg file3.pdf')
Removing files: ['file1.txt', 'file2.jpg', 'file3.pdf']
The first part of the argument 'remove' is matched after splitting.  Using the starred expression in the case definition captures any number of optional arguments which follow (similar to *args); the files variable gets defined as a list containing all the files to be removed. If you try implementing this with an if-elif-else statement, you’ll use more code to achieve the same result. It will also not be as readable as using a match case statement.

The next level of complexity involves using an or operator (|) and putting an if statement inside the case definition. Take a look at the following function, paying particular attention to the second and third cases:

>>> def file_handler_v2(command):
...     match command.split():
...         case ['show']:
...             print('List all files and directories: ')
...             # code to list files
...         case ['remove' | 'delete', *files] if '--ask' in files:
...             del_files = [f for f in files if len(f.split('.'))>1]
...             print('Please confirm: Removing files: {}'.format(del_files))
...             # code to accept user input, then remove files
...         case ['remove' | 'delete', *files]:
...             print('Removing files: {}'.format(files))
...             # code to remove files
...         case _:
...             print('Command not recognized')
 
if __name__ = "__main__":
    argument = 0
    number_to_string(argument)

What is the replacement of Switch Case in Python?
Unlike every other programming language we have used before, Python does not have a switch or case statement. To get around this fact, we use dictionary mapping.

Method 2: Switch Case implement in Python using if-else
The if-else is another method to implement switch case replacement. It is used to determine whether a specific statement or block of statements will be performed or not, i.e., whether a block of statements will be executed if a specific condition is true or not.

bike = 'Yamaha'
 
if fruit == 'Hero':
    print("letter is Hero")
 
elif fruit == "Suzuki":
    print("letter is Suzuki")
 
elif fruit == "Yamaha":
    print("fruit is Yamaha")
 
else:
    print("Please choose correct answer")

Method 1:  Switch Case implement in Python using Dictionary Mapping
In Python, a dictionary is an unordered collection of data values that can be used to store data values. Unlike other data types, which can only include a single value per element, dictionaries can also contain a key: value pair.
The key value of the dictionary data type functions as cases in a switch statement when we use the dictionary to replace the Switch case statement.


# Function to convert number into string
# Switcher is dictionary data type here
def numbers_to_strings(argument):
    switcher = {
        0: "zero",
        1: "one",
        2: "two",
    }
 
    # get() method of dictionary data type returns
    # value of passed argument if it is present
    # in dictionary otherwise second argument will
    # be assigned as default value of passed argument
    return switcher.get(argument, "nothing")
 
# Driver program
if __name__ == "__main__":
    argument=0
    print (numbers_to_strings(argument))

Method 3: Switch Case implement in Python using Class
In this method, we are using a class to create a switch method inside the python switch class in Python.

class Python_Switch:
    def day(self, month):
 
        default = "Incorrect day"
 
        return getattr(self, 'case_' + str(month), lambda: default)()
 
    def case_1(self):
        return "Jan"
 
    def case_2(self):
        return "Feb"
 
    def case_3(self):
        return "Mar"
 
 
my_switch = Python_Switch()
 
print(my_switch.day(1))
 
print(my_switch.day(3))