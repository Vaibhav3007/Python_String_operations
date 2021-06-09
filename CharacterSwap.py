mystr = input("Enter test string- ")

n = len(mystr)
swap = mystr[-1]+mystr[1:n-1]+mystr[0]

print(mystr,swap,sep = " --> ")

