from urllib.request import Request, urlopen
import ast
import math

req = Request('https://drand.cloudflare.com/public/latest', headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0'})
data = urlopen(req).read()
mydata=data.decode('utf-8')
mydata=ast.literal_eval(mydata)
round=mydata['round']
num=''
for i in range(round-20,round+1):
    url="https://drand.cloudflare.com/public/%s" % i
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0'})
    data2 = urlopen(req).read()
    mydata2=data.decode('utf-8')
    mydata2=ast.literal_eval(mydata2)
    num=num+mydata2['randomness']
sum=0
hex="0123456789abcdef"
for i in hex:
    if i in num:
        chance=num.count(i)/len(num)
        sum=sum+(chance*math.log(chance,2))
sum=-sum
print("Η εντροπία ισούται με:",sum)
