mystr1 = input("Enter test string 1 - ")
mystr2 = input("Enter test string 2 - ")

new_str1 = mystr1.lower()
new_str2 = mystr2.lower()

if sorted(new_str1) == sorted(new_str2):
    print(mystr1,"&",mystr2,"are anagrams")
else:
    print(mystr1,"&",mystr2,"are not anagrams")
