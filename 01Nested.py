num=int(input("enter a number:"))
print("your value is:",num)
if(0>num):
    print("negative")
elif(0<num):
    if(num<=10):
        print("number is 0 to 10")
    elif(num<=20):
        print("Number is 10 to 20")
    else:
        print("number is grater them 20")
else:
    print("number is zero")


