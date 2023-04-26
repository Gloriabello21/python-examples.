#ej:1 
print("meow")
print("meow")
print("meow")

#ej:2
i = 3
while i != 0:
    print("meow")
    i = i - 1
    i = 3

#ej:3
i = 0
while i <= 3:
    print("meow")
    i = i + 1

#ej:4
i = 0
while i < 3:
    print("meow")
    i = i + 1

#ej:5
i = 0
while i < 3:
    print("meow")
    i += 1
    
#ej:6
for i in [0, 1, 2]:
    print("meow")

#ej:7
for i in range(3):
    print("meow")
    
#ej:8
for _ in range(3):
    print("meow")

#ej:9
print("meow\n" * 3, end="")

#ej:10
while True:
    n = int(input("what's n? "))
    if n > 0:
        break
    for _ in range(n):
     print("meow")

#ej:11
def main():
    meow(3)
    def meow(n):
     for _ in range(n):
        print("meow")
        main()
