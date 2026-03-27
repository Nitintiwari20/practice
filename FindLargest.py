a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
c = int(input("Enter third number:"))
d = int(input("Enter forth number:"))

if(a >= b and a >= c and a >= d):
    print("a is largest",a)
    
elif(b >= c and b >= d):
    print("b is largest",b)
    
elif(c >= d):
    print("c is largest",c)

else:
    print("d is largest",d)