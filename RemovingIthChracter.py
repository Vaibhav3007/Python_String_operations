my_str = input("Enter the string- ")
print(my_str)
index = int(input("Enter the index to remove- "))
print(my_str[:index-1],my_str[index:],sep = "")
