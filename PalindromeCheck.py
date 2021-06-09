strng = input("Enter string ")

strng_rev = ""

for i in range(len(strng)-1,-1,-1):
    strng_rev = strng_rev + strng[i]

if strng.lower() == strng_rev.lower():
    print("Palindrome")
else:
    print("Not Palindrome")
