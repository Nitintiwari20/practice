n = int(input("Enter a number"))
sum = 0
temp = n
while temp > 0:
    sum = sum+((temp%10)**3)
    temp = temp//10
if sum == n:
    print(sum,"is armstrong",)
else:
    print("Number is not armstrong")
