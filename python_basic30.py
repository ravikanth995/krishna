# #Pass Statement #Pass is null statement
# for i in "Python":
#     if i=="h":
#         pass
#         print("THis is pass block")
#     print(i)
# print("Ended")        

# a=4
# b=0
# #Using assert to check for 0
# print("The Value of a/b is :")
# assert b!=0, "divide by 0 error"
# print(a/b)

# batch=[40,26,39,30,25,21]
# #Initializing cut temperature
# cut=26
# #using assert to check for temperature greater than cut 
# for i in batch:
#     assert i>=26, "batch is rejected"
#     print(str(i)+"is 0.K")

def KelvinToFarhenheit(temperature):
    assert (temperature>=0), "Colder than absolute zero"
    return ((temperature-273.16)*1.8)+32
print(KelvinToFarhenheit(273))
print(int(KelvinToFarhenheit(505.78)))  
print(KelvinToFarhenheit(-5))  