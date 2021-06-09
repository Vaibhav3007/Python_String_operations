#Unequivocally
#nymph
a = input("Enter character - ")
a1 = a.lower()
count = 0
for i in a1:
    if i in "aeiou":
        count += 1
        
print("Number of vowels is - ",count)
