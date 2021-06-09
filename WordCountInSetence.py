#strng = input("Enter string ")


lst = [x for x in input("Enter string ").split(" ")]
search = input("Enter search string ")

print(search,"occurs",lst.count(search),"times")
