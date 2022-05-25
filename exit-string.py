#!python
import sys

print(f"Name of the script      : {sys.argv[0]=}")
print(f"Arguments of the script : {sys.argv[1:]=}")

  
arg1 = sys.argv[1]

# check and print type num variable
print(type(arg1)) 
  
# convert the num into string 
age = int(arg1)
  
# print type of converted_num
print(type(age))  
  
if age < 18:
    # exits the program
    sys.exit("Age less than 18")    
else:
    print("Age is not less than 18")