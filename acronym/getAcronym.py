from bs4 import BeautifulSoup
import requests


baseUrl="http://www.noslang.com/dictionary/"
page=list(map(chr, range(97, 123)))
completeList=[]
f=open("acronyn.txt",'w')
e=open("error.txt",'w')
for i in page:
    print i
    url=baseUrl+i
    r  = requests.get(url)
    data = r.text
    soup = BeautifulSoup(data)
    if i!='j' and i!='t':
        acr = soup.findAll('strong')
        acr=[i.string for i in acr]
        abr = soup.findAll('dd')
        abr=[i.string for i in abr]
        size=len(abr)
        for i in range(size):
            try:
                print str(acr[i])+'\t'+str(abr[i])
                f.write(str(acr[i])+'\t'+str(abr[i])+'\n');
            except:
                print str(acr[i])
                e.write(str(acr[i])+'\n');
    else:
        comb=soup.findAll('abbr')
        print comb
        comb=[ (str(i.string),str(i['title'])) for i in comb ]
        for i in comb:
            try:
                print str(i[0])+'\t'+str(i[0])
                f.write(str(i[0])+'\t'+str(i[0])+'\n');
            except:
                print str(i[0])
                e.write(str(i[0])+'\n');
