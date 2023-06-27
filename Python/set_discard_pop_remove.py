# code for set.discard(), remove() and pop()

a=int(input())
s=set(list(map(int, input().split())))
c=int(input())
for i in range(c):
    
    d=input().split()
    if d[0]=="pop":
        s.pop()
    if d[0]=='remove':
        s.remove(int(d[1]))
    if d[0]=='discard':
        s.discard(int(d[1]))
    

sum_s=0
for i in s:
    sum_s+=i   
print(sum_s)
