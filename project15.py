try:
    x=int(input("Enter your age:"))
    print(x)
except ValueError:
    print("Error!")
    print("Enter a number:")
    x=int(input("enter your age:"))
    print(x)
    print("you're %s"%x)
