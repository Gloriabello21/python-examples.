#ejemplo1:
def main():
    height= int(input("Height:"))
    pyramidn(height)

def pyramidn(n):
    for i in range(n):
        print("#" * (i + 1))

if __name__ == "__main__":
    main()        



