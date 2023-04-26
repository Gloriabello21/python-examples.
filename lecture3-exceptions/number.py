#ejemplo:1
x = int(input("what's x? "))
print(f"x is {x}")

#ejemplo2
try:
     x = int(input("what's"))
     print(f"x is{x}") 
except ValueError:
     print("x is not an integer")

#ejemplo3
try:
     x = int(input("what's"))
except ValueError:
     print("x is not an integer")

print(f"x is {x}")

#ejemplo4
try:
     x = int(input("what's"))
except ValueError:
     print("x is not an integer")
else: 
     print(f"x is {x}")     

#ejemplo:5
while True: 
    try: x = int(input("what's x?"))
    except ValueError:
     print("x is not an integer")
    else:
         break
print(f"x is {x}")

#ejemplo:6
while True: 
    try: 
       x = int(input("what's x?"))
       break
    except ValueError:
     print("x is not an integer")
    
print(f"x is {x}")


#ejemplo:7
def main():
     x = get_int()
     print(f"x is {x}")

def get_int():
   while True:
     try:  
           x = int(input("what's x? "))
     except ValueError:
        print("x is not an integer")
     else:
         break
   return x 
   

main()

#ejemplo:8
def main():
     x = get_int()
     print(f"x is {x}")

def get_int():
   while True:
     try: 
           return int(input("what's x?")) 
     except ValueError:
         pass

main()

#ejemplo9
def main():
     x = get_int("what's x? ")
     print(f"x is {x}")

def get_int(prompt):
   while True:
     try: 
           return int(input(prompt)) 
     except ValueError:
         pass

main()     

