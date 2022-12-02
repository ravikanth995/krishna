# import math
# print(math.sqrt(225))

# import math
# print(math.sqrt(16))

# import math
# print(math.sqrt(289))

# import math
# print(math.sqrt(361))

# import math
# print(math.sqrt(900))

# import math
# print(math.sqrt(525))

# import math
# print(math.sqrt(625))

# num=float(input("Enter a number:"))
# num_sqrt=num**0.5
# print("The Square root of %.0f is: %.0f"%(num, num_sqrt))

# num=float(input("Enter a Number:"))
# num_sqrt=num**0.5
# print("The Square root of %.1f number is %.2f"%(num,num_sqrt))

# num=float(input("Enter Number of Square root you want:"))
# num_sqrt=num**0.5
# print("Square root of %.3f is: %.3f"%(num,num_sqrt))

# num=float(input("Enter Number:"))
# num_sqrt=num**0.5
# print("Square of the %.3f is: %.3f"%(num,num_sqrt))

# num=float(input("Enter the Number:"))
# num_sqrt=num**0.5
# print("Square of %.2f is %.3f"%(num,num_sqrt))

# num=float(input("Enter Number:"))
# num_sqrt=num**0.5
# print("Square of %.2f is: %.3f"%(num,num_sqrt))

# num=float(input("Enter Number:"))
# num_sqrt=num**0.5
# print("Square of %.2f is: %.3f"%(num,num_sqrt))

# num=float(input("Enter Number:"))
# num_sqrt=num**0.5
# print("Square root of %.0f is: %.3f"%(num,num_sqrt))

# num=float(input("Enter  Number:"))
# num_sqrt=num**0.5
# print("Square root of %.0f is: %.3f"%(num,num_sqrt))

# num=float(input("Enter Number:"))
# num_sqrt=num**0.5
# print("Square root of %.0f is : %.3f"%(num,num_sqrt))

# num=float(input("Enter Number:"))
# num_sqrt=num**0.5
# print("Square root of %.0f is: %.2f"%(num,num_sqrt))

# num=float(input("Enter Number of Days:"))
# num_sqrt=num**0.5
# print("Square root of %.0f is:%.2f"%(num,num_sqrt))

# num=float(input("Enter Number:"))
# num_sqrt=num**0.5
# print("Square root of %.0f is:%.2f"%(num,num_sqrt)


def twoSum(self, nums, target):
        # two point
        nums_index = [(v, index) for index, v in enumerate(nums)]
        nums_index.sort()
        begin, end = 0, len(nums) - 1
        while begin < end:
            curr = nums_index[begin][0] + nums_index[end][0]
            if curr == target:
                return [nums_index[begin][1], nums_index[end][1]]
            elif curr < target:
                begin += 1
            else:
                end -= 1

twoSum(1,2,3,4,5,6,7,target=15)       