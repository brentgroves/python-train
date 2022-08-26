https://teclado.com/30-days-of-python/python-30-day-21-multiple-files/

Importing adds a name to globals()
If you have a Python file and you type this:

import json

print(globals())
Then that displays the names currently in the global namespace. The module name will be in the global namespace, ready for you to use.

Importing allows us to access elements of the imported module
After importing, we can do something like this to access something inside a module:

import math

print(math.pi)  # 3.14

We've accessed the pi name inside the math module. In this case, that is the value of the mathematical constant, pi.

You can use the as keyword to give the imported module a different name in your code. I don't recommend you do this, although you'll see it done every now and then!

You can also use * to add almost everything from a module to your global namespace. This can "pollute" the global namespace, filling it with variables. Most of the time, it's strongly discouraged.