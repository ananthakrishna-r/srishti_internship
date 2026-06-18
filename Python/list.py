a=[]
for i in range(1,11):
    a.append(i)
print(a)


#a=["c","c++","java"]
#a.insert(2,"python")
#print(a)
#a.insert(0,"php")
#a.append("py")
#print(a)
#fr=["apple","orange","mango","guava"]
#fr.remove("apple")
#print(fr)
#fr.pop(-1)
#print(fr)
#fr.pop(3)
#print(fr)
#fr.clear()
#print(fr)
#co=["red","blue","white","yellow"]
#print(co.index("blue"))
no=[10,20,46,10]
#print(no.count(10))
#no.sort()
#print(no)
#no.sort(reverse=True)
#print(no)
#no.reverse()
#print(no)
#n=no.copy()
#n.append(50)
#print(no)
#print(n)

#na=["a","b","c","d"]
#for s in na:
    #print(s)

no=[1,45,634,66,73,1000]
#print(max(no))

#print(min(no))

count=0
#for n in no:
    #if n % 2==0:
        #count+=1
#print("even",count)

no=[34,5,7,24,78]
for g in no:
    if g % 2 !=0:
        count+=1
print("odd",count) 


a=[1,2,3]
b=[4,5,6]
a.extend(b)
print(a)