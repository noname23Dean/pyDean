import requests
from bs4 import BeautifulSoup
import array
import resources

baseUrl = 'https://www.dhlottery.co.kr/gameResult.do?method=byWin&drwNo='
html = requests.get(baseUrl).text

soup = BeautifulSoup(html, 'html.parser')

result = str(soup.find("meta", {"id": "desc", "name": "description"})['content'])

nowNum = int(result[result.find(" ")+1:result.find("회")])
lastNum = result[result.find(" ", result.find("당첨번호"))+1:result.find(".")]
# print(result)
# totResult = []

rofile = open("./roResult.txt", 'r')
roCnt = rofile.read().count("\n")+1
rofile.close()

f = open("./roResult.txt", 'a')

if roCnt != 1 : 
    f.write('\n') 

# for i in range(1,10) :
for i in range(roCnt+1,nowNum) :
    
    crawUrl = baseUrl + str(i)
    # print(crawUrl)
    crawHtml = requests.get(crawUrl).text

    crawSoup = BeautifulSoup(crawHtml, 'html.parser')

    crawResult = str(crawSoup.find("meta", {"id": "desc", "name": "description"})['content'])

    # print(crawResult[crawResult.find(" ", crawResult.find("당첨번호"))+1:crawResult.find(".")])

    # totResult.append(crawResult[crawResult.find(" ", crawResult.find("당첨번호"))+1:crawResult.find(".")])
    f.write(crawResult[crawResult.find(" ", crawResult.find("당첨번호"))+1:crawResult.find(".")])
    f.write('\n')

f.write(lastNum)
f.close()
# print(resources.getrusage(resources.RUSAGE_SELF).ru_maxrss)