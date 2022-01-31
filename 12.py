from urllib.request import Request, urlopen
import ast

req = Request('https://drand.cloudflare.com/public/latest', headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0'})
data = urlopen(req).read()
mydata=data.decode('utf-8')
mydata=ast.literal_eval(mydata)
round=mydata['round']
num=''
for i in range(round-100,round+1):
    url="https://drand.cloudflare.com/public/%s" % i
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0'})
    data2 = urlopen(req).read()
    mydata2=data.decode('utf-8')
    mydata2=ast.literal_eval(mydata2)
    num=num+mydata2['randomness']
bin=bin(int(num,16))
max1=0
max0=0
len1=0
len0=0
for i in bin:
    if i=="1":
        len0=0
        len1+=1
        if len1>max1:
            max1=len1
    if i=="0":
        len1=0
        len0+=1
        if len0>max0:
            max0=len0
print("Η μεγαλύτερη ακολουθία με συνεχόμενα μηδενικά είναι:",max0)
print("Η μεγαλύτερη ακολουθία με συνεχόμενες μονάδες είναι:",max1)
