from urllib.request import Request, urlopen
import ast

req = Request('https://drand.cloudflare.com/public/latest', headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0'})
data = urlopen(req).read()
mydata=data.decode('utf-8')
mydata=ast.literal_eval(mydata)
num=mydata['randomness']
num_list=[]
b=[]
for i in range(0,len(num),2):
    b.append(num[i])
    b.append(num[i+1])
    b=''.join(b)
    b=int(b,16)
    b=b%80
    num_list.append(b)
    b=[]
l=len(num_list)
i=0
while i<l:
    k=0
    while k<l:
        if i!=k:
            if num_list[i]==num_list[k]:
                num_list.pop(k)
                l-=1
        k+=1
    i+=1
url="https://api.opap.gr/draws/v3.0/1100/last-result-and-active"
kino=urlopen(url).read()
kino=kino.decode('utf-8')
kino=ast.literal_eval(kino)
winning_num=(kino['last']['winningNumbers']['list'])
sum=0
print("Οι αριθμοί που θα κληρονόνουσαν στην τελευταία κλήρωση του ΚΙΝΟ είναι οι:")
for i in num_list:
    for k in winning_num:
        if i==k:
            print(i)
            sum+=1
print("Συνολικά",sum,"αριθμοί.")
