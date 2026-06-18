'''st=['an','sf','dg','fd','hf']
for i in st:
    print(i)
  
a=set()
for i in range(10):
    i=int(input("enter no"))
    a.add(i)
print(a)
  
c=('a','sd','gf','df')
for i in c:
    print(i)
  
l=[1,2,3,2,3]
c=0
n=int(input("enter no"))
for i in l:
    if n==i:
        c+=1
print(c)
  
l=[34,3,5,23]
n=max(l)
m=min(l)
print("max",n)
print("min",m)

l=[3,34,2,1,34,6,6]
s=[]
for i in l:
    if i not in s:
        s.append(i)
print(s)


l=[1,2]
l1=[3,4]
k=l+l1
print(k)


text = "Python"
rev = ""
for ch in text:
    rev = ch + rev
print(rev)


a=int(input("enter amount"))
t=int(input("gst"))
g=a+(a*t)/t
print("gst ",g)
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a > b and a > c:
    print("Greatest =", a)
elif b > c:
    print("Greatest =", b)
else:
    print("Greatest =", c)

a=input('a')
b=input('b')
a,b=b,a
print("a",a,"b",b)
   
a=[1,2,3]
b=a
print(b is a)
 
n=input("enter no")
rev=""
for i in n:
    rev=i+rev
print(rev)

n=input("enter no")
r=0
for i in n:
    r=r+int(i)
print(r)

n=int(input("no"))
a=0
b=1
for i in range(n):
    print(a,end="")
    a,b=b,a+b

for i in range(5):
    print(" " * (5 - i) + "*" * (2 * i - 1))
   
st={}
while True:
    print("1.add")
    print("2.view")
    print("3.view")
    print("4.del")
    print("5.exit")
    ch=input("enter choice")
    if ch=="1":
        r=int(input("no"))
        n=input("enter name")
        st[r]=n
    elif ch=="2":
        for r,n in st.items():
            print(r,n)
    elif ch=="3":
        r=int(input("no"))
        if r in st:
            print(st[r])
        else:
            print("nt fnd")
    elif ch=="4":
        r=int(input("no"))
        if r in st:
            del st[r]
            print("del")
        else:
            print("nt fnd")
    else:
        break
    
st = {}

while True:
    print("1.add")
    print("2.view")
    print("3.search")
    print("4.del")
    print("5.exit")

    ch = input("enter choice: ")

    if ch == "1":
        r = int(input("no: "))
        n = input("enter name: ")
        st[r] = n

    elif ch == "2":
        for r, n in st.items():
            print(r, n)

    elif ch == "3":
        r = int(input("no: "))
        if r in st:
            print(st[r])
        else:
            print("nt fnd")

    elif ch == "4":
        r = int(input("no: "))
        if r in st:
            del st[r]
            print("del")
        else:
            print("nt fnd")

    elif ch == "5":
        break

    else:
        print("Invalid choice")
   
             '''
'''
contacts = {}

while True:
    print("\n1.Add Contact")
    print("2.View Contacts")
    print("3.Search")
    print("4.Exit")

    ch = input("Choice: ")

    if ch == "1":
        name = input("Name: ")
        phone = input("Phone: ")
        contacts[name] = phone

    elif ch == "2":
        print(contacts)

    elif ch == "3":
        name = input("Search Name: ")
        print(contacts.get(name, "Not Found"))

    elif ch == "4":
        break
    
ch=0
n=input("cap of ind")
if n.lower()=="delhi":
    ch+=1
n=input("2+2")
if n=='2':
    ch+=1
print(ch)

balance = 1000

while True:
    print("\n1.Deposit")
    print("2.Withdraw")
    print("3.Balance")
    print("4.Exit")

    ch = input("Choice: ")

    if ch == "1":
        amt = float(input("Amount: "))
        balance += amt

    elif ch == "2":
        amt = float(input("Amount: "))
        if amt <= balance:
            balance -= amt

    elif ch == "3":
        print("Balance =", balance)

    elif ch == "4":
        break
   
p="1234"
pi=input("pin")
if pi==p:
    print ("access granted")
else:
    print("rej")
   
    

menu={
    "burger":100,
    "noodles":200,
    "fries":250
}
total=0
item=input("enter item")
if item in menu:
    total=total+menu[item]
print(total)
 
employees = {
    "Anu": 25000,
    "Rahul": 30000
}

for name, salary in employees.items():
    print(name, salary)
    inventory = {
    "Pen": 50,
    "Book": 20
}


for item, qty in inventory.items():
    print(item, qty)
    seats = 10

tickets = int(input("How many tickets? "))

if tickets <= seats:
    seats -= tickets
    print("Booked")
else:
    print("Not Available")

 '''

password = input("Password: ")

if len(password) >= 8:
    print("Strong Password")
else:
    print("Weak Password")