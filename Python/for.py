"""
for n in range(1,11):
    print(n)

for n in range(10,0,-1):
    print(n)
   
for i in range(1,50):
    if i%2==0:
        print(i)

for i in range(1,50):
    if i%2!=0:
        print(i)
        
for i in range(1,11):
    print(i**2)

for i in range(1,11):
    print(i**3)

n=0
for i in range(1,101):
    n+=i
    print(n)
       
n=0
for i in range(1,101):
    if i%2==0:
        n+=i
        print(n)
        
n=0
for i in range(1,101):
    if i%2!=0:
        n+=i
        print(n)
         
a=int(input("no"))
for i in range(1,11):
    n=a*i
    print(a,"x",i,"=",n)
    """
#list
'''
l=[1,2,3,4,5]
for i in l:
    print(i)

l=[1,2,3,4,5]
s=0
for i in l:
    s+=i
print(s)

    
l=[1,2,3,4,5]
n=l[0]
for i in l:
    if i>n:
        n=i
print(n)

l=[1,2,3,4,5]
n=l[0]
for i in l:
    if i<n:
        n=i
print(n)


l=[1,2,3,4,5]
c=0
for i in l:
    c+=1
print(c)

l=[1,2,3,4,5]
c=0
for i in l:
    if i%2==0:
        c+=1
print(c)

l=[1,2,3,4,5]
c=0
for i in l:
    if i%2!=0:
        c+=1
print(c)

l=[1,2,3,4,5]
c=0
t=0
for i in l:
    c+=1
    t+=i
print(t/c)

l=[1,-2,3,-4,5,-9,-8]
c=0
for i in l:
    if i>0:
        c+=1
print(c)
'''
l=[1,-2,3,-4,5,-9,-8]
c=0
for i in l:
    if i<0:
        c+=1
print(c)
