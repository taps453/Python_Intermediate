try:
    a = int(input("enter 1st number"))
    b = int(input("enter 2st number"))
    if b==0:
        raise Exception("The value should be greater then 0")
    print(a/b)
except Exception as e:
    print(e)

# Finally always run
finally:
    print(a+b)