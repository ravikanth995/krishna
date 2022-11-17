def sum_digits(num):
    sum=0
    while(num>0):
        sum=sum+num%10
        num=num//10
    return sum
sum_digits(23)
# num=int(input("Enter a number:"))
print("Sum of digits:", sum)