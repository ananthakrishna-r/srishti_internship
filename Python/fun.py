'''
def wel():
    print("welcome")
wel()

def n(na):
    return "hello"+ na
print(n('anan'))

def e(t):
    return  t==""
print(e(''))

def c(t):
    count=0
    for i in t:
        count+=1
    print(count)
c("pyth")

def c(t):
    print(t.upper())
c('cvbsn')

def c(t):
    print(t.lower())
c('VCBH')
 

def c(t):
    return t[::-1]
print(c("hhgg"))

def c(t):
    return t==t[::-1]
print(c("ghg"))

def f(t):
    c=0
    for ch in t:
        if ch in 'aeiouAEIOU':
            c+=1
    return c
print(f("ahAIEsj"))

def g(t):
    return t.replace(" ","")
print(g("hel l o"))

def t(s):
    for c in s:
        print(c)
t([1,2])

def t(s):
    c=0
    for ch in s:
        c+=1
    return c
print(t([1,2,34,5]))

def t(s):
    d=[]
    for ch in s:
        if ch not in d:
            d.append(ch)
    return d
print(t([1,2,3,3,4]))


def t(s,d):
    if d  in s:
        return d
print(t([1,2,3,3,4],4))

def t(s):
    return s[0]
print(t([1,23,4]))

def t(s):
    return s[-1]
print(t([1,23,4]))

def t(s,a):
    c=0
    for ch in s:
        if ch==a:
            c+=1
    return c
print(t([1,2,3,4,4,4,5],4))

def t(s,a):
    return s+a
print(t([1,2],[3,4]))

def t(s):
    odd=[]
    eveb=[]
    for ch in s:
        if ch%2==0:
            eveb.append(ch)
        else:
            odd.append(ch)
    return eveb,odd
print(t([2,3,5,6,8]))


def t(s):
    for i in range(len(s)):
        for j in range(i+1,len(s)):
            if s[i]>s[j]:
                s[i],s[j]=s[j],s[i]
    return s
print(t([1,4,6,3,2,8]))

def t(S):
    for key in S:
        print(key)
print(t({1:'er',2:'sf'}))

def t(s):
    for v in s.values():
        print(v)
print(t({1:'sd',2:'gd',3:'fef'}))


def t(s,d):
    return d in s
print(t({1:'a'},1))

def t(s):
    c=0
    for f in s:
        c+=1
    return c
print(t({1:'a',2:'b'}))

def t(s,k,v):
    s[k]=v
    return s
print(t({1:'s'},2,'b'))


def t(s,k,v):
    s[k]=v
    return s
print(t({1:'s'},1,'b'))

def t(s,k):
    del s[k]
    return s
print(t({1:'s',2:'b'},2))
'''

def longest_key(d):
    longest = ""
    for key in d:
        if len(key) > len(longest):
            longest = key
    return longest

print(longest_key({"name": 1, "address": 2}))