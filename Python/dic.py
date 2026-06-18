'''
st={
    'name':'ananthu',
    'age':21,
    'course':'ai ml'
}
st['pl']='ktm'
print(st)

st.update({'age':22})
print(st)

st.pop('age')
print(st)

print(st.keys())

print(st.values())

print(st.items())

print('name' in st)

st1=st.copy()
print(st1)

print(st1.clear())
'''
'''
t='hello'
f={}
for ch in t:
    f[ch]=f.get(ch,0)+1
print(f)    

t1='python is python'
f={}
for word in t1.split():
    f[word]=f.get(word,0)+1
print(f)

m={'a':5,'b':6,'c':7}
print(max(m))

d={'a':1}
d1={'b':2}
d.update(d1)
print(d)
'''
'''
a=['a','b','c']
b=[1,2,3]
c=dict(zip(a,b))
print(c)
'''
'''
e={
    1:{
        'name':'a','salary':10000    },
    2:{'name':'b','salary':12000}
}
print(e)

d={'a':6,'b':3,'c':10}
for f,v in d.items():
    if v > 5:
        print(f)

sq={}
for i in range(1,11):
    sq[i]=i*i
print(sq)

s={'a':1200,'b':200,'c':500}
print(dict(sorted(s.items(),key=lambda x:x[1],reverse=True)))


a=['ab','amc','gcnb']
d={}
for n in a:
    d[n]=len(n)
print(d)
'''

#minipro
contact={'A':123456789}
contact.update({'B':987654321})
print(contact)
print(contact.get('A'))

product={'A':30,'B':40,'C':60,'D':10}
total=sum(product.values())
print("total bill",total)

lib={
    1:'ab',2:'sf',3:'sdf'
}
print(lib)
print(lib.get(1))


p='python i easy python is powerful'
count={}
for n in p.split():
    count[n]=count.get(n,0)+1
print(count)

stu={'eng':89,'mal':97,'cs':100,'maths':87}
tt=sum(stu.values())
av=tt/len(stu)
print("total",total,"avg",av)