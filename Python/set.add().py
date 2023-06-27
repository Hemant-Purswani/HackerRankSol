#This is the sample code for set.add(). This code can be used for adding items into the list without adding multiple duplicates.

a=set()
for i in range(int(input())):
    x=input()
    a.add(x)
print(len(a))
