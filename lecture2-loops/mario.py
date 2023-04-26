#ejemplo1
print("#")
print("#")
print("#")


#ejemplo2
for _ in range(3):
    print("#")

#ejemplo3
def main():
    print_column(3)

def print_column(height):
    for _ in range(height):
        print("#")


        main()

#ejemplo4
def main():
    print_column(3)


def print_column(height):
    print("#\n" * height, end="")
    

#ejemplo5
def main():
    print_row(4)


def print_row(width):
    print("?" * width)

main()

#ejemplo6
def print_square(size):

    #for each row in squre
    for i in range(size):

      #for each brick in row
      for j in range(size):
          
          #print brick
          print("#", end="")

#ejemplo7
def main ():
    print_square(3)

def print_square(size):
    for i in range(size):
        print("#" * size)

main()

#ejemplo8
def main ():
    print_square(3)

def print_square(size):
    for i in range(size):
             print_row(size)

def print_row(width):
    print("#" * width)








