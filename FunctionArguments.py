#Default
# def average(a=4,b=6):
#     print("The average is", (a+b)/2)

# average(7,5)
#there are four type of Argument
#1=Default,2=Keyword,3=Variable length ,4=required.

#Keyword
# def name(a,b,c):
#     print("hello",a,b,c)
# name(c="Nitin",b="Rohit",a="Divyanshu")

#Requied
# def name(a,b,c):
#     print("hello,",a,b,c)
# name("Nitin","Rohit")

#Variable length 

def average(*numbers):
    print(type(numbers))
    sum = 0
    for i in numbers:
        sum = sum + i
    return sum/len(numbers)
#return ko jo pahale mila use le lega.
c=average(5,6,7,8,9)
print(c)


# def name(**name):
#     print(type(name))
#     print("hello,",name["fname"], name["mname"], name["iname"])

# name(mname="buchanan", iname="Barnes", fname="james")