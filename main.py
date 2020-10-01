num = int(input("Enter a number: "))

order = len(str(num))
sum = 0
temp = num
while temp > 0:
a = temp % 10
sum = sum + (a ** order)
temp = temp // 10


if(num == sum):
print("The number is Armstrong Number")
else:
print("The number is not Armstrong Number")
