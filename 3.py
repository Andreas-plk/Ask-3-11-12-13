f=open("file_name","r")
p=(f.readlines())
letters='abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ'
sym=[]
for i in range(32,65):
    sym.append(chr(i))
for i in range(123,127):
    sym.append(chr(i))
for i in range(91,97):
    sym.append(chr(i))
#Η λίστα sym περιέχει όλους τους ascii χαρακτήρες εκτός από τα γράμματα και το κενό.
p=' '.join(p)
for c in sym:
    p=p.replace(c," ")
p = ''.join(filter(letters.__contains__, p))
p=p.split(' ')
while "" in p:
    p.remove("")
l=len(p)
i=0
print("\nΑυτά τα ζευγάρια λέξεων έχουν άθροισμα γραμμάτων 20: ")
while i<l-1:
    k=i+1
    while k<l:
            if len(p[i])+len(p[k])==20:
                print(p[i],p[k])
                p.pop(i)
                k-=1
                p.pop(k)
                i-=1
                l-=2
            k+=1
    i+=1
max=len(max(p,key=len))
min=len(min(p,key=len))
sum=0
print("\nΑπομένουν:")
for i in range(min,max+1):
    for j in range(len(p)):
        if len(p[j])==i:
            sum+=1
    if sum!=0:
        print(sum," λέξη/λέξεις με ", i ,"γράμμα/γράμματα")
    sum=0
f.close()
