you can't set them permanently because python script is running in a child proces.
import os

print('p - The message is:', os.environ['MESSAGE'])