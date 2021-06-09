strng = input("Enter string to be tested ")

count_l = 0
count_u = 0
for i in strng:
    if i.islower() == True:
        count_l += 1
    else:
        count_u += 1
    
print("Lower case letters-",count_l)
print("Upper case letters-",count_u)
