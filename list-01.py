# list are mutable.

marks= [3,5,6,"Nitin","harry","vaibhav"]
# print(marks)
# print(type)
# print(marks[0])
# print(marks[1])
# print(marks[2])

# print(marks[-3])#negative index
# print(marks[len(marks)-3])#positive index
# print(marks[6-3])#positive index
# print(marks[3])#positive index

if "Nitin" in marks:
    print("yes")
else:
    print("no")

#same thing applies for strings as well!
# if "Ni" in "Nitin":
#     print("yes")
# else:
#     print("No")

# print(marks)
# print(marks[1:-1])
# print(marks[1:6])
# print(marks[1:6:2])

#list comprehension
# lst=[i*i for i in range(10)]
# print(lst)
# lst=[i*i for i in range(10) if i%2==0]
# print(lst)