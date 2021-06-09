mystr = input("Enter test string- ")
n = len(mystr)
new = ""
for i in range(-1,-(n+1),-1):
    new = new+mystr[i]
print(new)

if mystr.lower() == new.lower():
    print("Palindrome")
else:
    print("Not-Palindrome")
