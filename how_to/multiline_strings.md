https://www.techbeamers.com/python-multiline-string/

"""Learn Python
Programming"""

  im2 =string.replace('''
  delete from DailyMetrics.daily_shift_report
  WHERE pcn = ? and report_date = ?
  ''', '\n', ' ')

# String containing newline characters
line_str = "I'm learning Python.\nI refer to TechBeamers.com tutorials.\nIt is the most popular site for Python programmers."

# String containing newline characters
line_str = "I'm learning Python.\nI refer to TechBeamers.com tutorials.\nIt is the most popular site for Python programmers."
print("Long string with newlines: \n" + line_str)

# Creating a multiline string
multiline_str = """I'm learning Python.
I refer to TechBeamers.com tutorials.
It is the most popular site for Python programmers."""
print("Multiline string: \n" + multiline_str)

This method retains the newline ‘\n’ in the generated string. If you want to remove the ‘\n’, then use the strip()/replace() function.

# Python multiline string example using brackets
multiline_str = ("I'm learning Python. "
"I refer to TechBeamers.com tutorials. "
"It is the most popular site for Python programmers.")
print(multiline_str)

# Python multiline string with newlines example using brackets
multiline_str = ("I'm learning Python.\n"
"I refer to TechBeamers.com tutorials.\n"
"It is the most popular site for Python programmers.")
print(multiline_str)
# Python multiline string example using backslash
multiline_str = "I'm learning Python. " \
"I refer to TechBeamers.com tutorials. " \
"It is the most popular site for Python programmers."
print(multiline_str)

# Python multiline string example using backslash and newlines
multiline_str = "I'm learning Python.\n" \
"I refer to TechBeamers.com tutorials.\n" \
"It is the most popular site for Python programmers."
print(multiline_str)

# Python multiline string example using string join()
multiline_str = ' '.join(("I'm learning Python.",
                          "I refer to TechBeamers.com tutorials.",
                          "It is the most popular site for Python programmers."))
print(multiline_str)

