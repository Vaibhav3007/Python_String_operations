mystr = input("Enter test string- ")
new_str = ""
n = len(mystr)

for i in range(n):
    if i%2 == 0:
       new_str = new_str + mystr[i]

print("Original string-",mystr)
print("Odd characters removed-",new_str)
