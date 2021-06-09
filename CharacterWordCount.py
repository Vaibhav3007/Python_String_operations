mystr = input("Enter test string- ")

count = 0
space = 0

for i in mystr:
    if i == " ":
        space = space+1
        continue
    count = count+1



print("Number of characters-",count)
print("Number of words-",space+1)
