#Python Code for symmetric difference for a set

def set_creation():
    
    try:
        
        a= input()
        liz=a.split()
        new_liz=list(map(int,liz))
        a= list(map(str, input().split()))
        return(a)
    
    except:
        a= input()
        liz=a.split()
        return liz
        

a=set(set_creation())
b=set(set_creation())
c=a.difference(b)
d=b.difference(a)
e=c.union(d)
f=[]

for i in e:
    f.append(int(i))
f.sort()
for i in f:
    print(i)
