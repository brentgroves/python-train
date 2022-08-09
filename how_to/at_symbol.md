https://builtin.com/software-engineering-perspectives/python-symbol
WHEN TO USE THE @ SYMBOL IN PYTHON
The main use case of the symbol @ in Python is decorators. In Python, a decorator is a function that extends the functionality of an existing function or class.
Decorators
The main use case of the symbol @ in Python are decorators. In Python, a decorator extends the functionality of an existing function or class.

For example, this piece of code . . .

def extend_behavior(func):}
    return func

@extend_behavior
def some_func():
     pass
. . . does the exact same as this piece of code:

def extend_behavior(func):
    return func

def some_func():
    Pass

some_func = extend_behavior(some_func)