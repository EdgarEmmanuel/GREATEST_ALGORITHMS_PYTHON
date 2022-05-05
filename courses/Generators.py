"""
In fact, yield is the key to generators. When Python sees yield in a function, it takes
that function and wraps it up in an object not unlike the one in our previous example.
Think of the yield statement as similar to the return statement; it exits the function
and returns a line. Unlike return , however, when the function is called again (via
next() ), it will start where it left off―on the line after the yield statement―instead
of at the beginning of the function
"""

import sys

inname, outname = sys.argv[1:3]


def warnings_filter(insequence):
    for l in insequence:
        if 'WARNING' in l:
            yield l.replace('\tWARNING', '')


with open(inname) as infile:
    with open(outname, "w") as outfile:
        filters = warnings_filter(infile)
        for l in filters:
            outfile.write(l)

"""
In this example, there is no line after the yield
statement, so it jumps to the next iteration of the for loop. Since the yield statement
is inside an if statement, it only yields lines that contain WARNING
"""
