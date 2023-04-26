#ejemplo1
import sys

print("hello, my name is", sys.argv[1])

#ejemplo2
import sys

print("hello, my name is", sys.argv[0])

#ejemplo3
import sys

try:
    print("Hello, my name is", sys.argv[1])
except IndexError:
    print("Toofew arguments")

#ejemplo4
import sys

if len(sys.argv) < 2:
     print("Too few arguments")
elif len(sys.argv) > 2:
    print("Too many arguments")
else:
    print("hello, my name is", sys.argv[1])  

#ejemplo5
import sys 
if len(sys.argv) < 2:
    sys.exit("Too few arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many arguments")

print("hello, my name is",sys.argv[1])        