strng1 = input("Enter 1st string to be tested ")
strng2 = input("Enter 2nd string to be tested ")

count1 = 0
for i in strng1:
    count1 += 1

count2 = 0
for j in strng2:
    count2 += 1

if count1 > count2:
    print(strng1)
else:
    print(strng2)
