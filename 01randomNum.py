import random
from collections import Counter

tot = []
# tot2 = []

# pop()이 너무 느려서 그냥 random으로 뽑음...
for x in range(8140000):
# for x in range(1000):
# for x in range(2) :
    num = []
    rotto_no = random.randint(1,45)
    for si in range(6):
    # for i in range(7):
        while rotto_no in num:
            rotto_no = random.randint(1,45)
        num.append(rotto_no)
        # if i == 6 :
        #     tot2.append(rotto_no)
        # else :
        #     tot.append(rotto_no)
        tot.append(rotto_no)
    #print(sorted(num))
    #print(tot)
totCnt = Counter(tot)
# tot2Cnt = Counter(tot2)
# print(totCnt)

# totVal = sorted(totCnt.most_common(7))
totVal = sorted(totCnt.most_common(6))
# print(totVal)
# tot2Val = (tot2Cnt.most_common(1))
# print(tot2Val)
# print(sorted(totVal))
# print(totVal)

returnVal = []

for ret in range(6) :
    returnVal.append(str(totVal[ret])[1:str(totVal[ret]).find(',')])

f = open('./roResult.txt', 'r')

resultList = []

while True:
    line = f.readline()
    if len(line) > 0 : resultList.append(line[0:line.find('+')])
    if not line: break

f.close()

useFlag = True
for re in range(len(resultList)):
    # print(','.join(returnVal))
    # print(resultList[re])
    if ','.join(returnVal) == resultList[re] : 
        useFlag = False 
        useNum = re+1

if useFlag == False : print(str(useNum) +' 회  당첨 내역 입니다.')
else : print(str(returnVal) + ' 번호는 기존 당첨 내역에 없습니다.')


# print(returnVal)
# print(sorted(returnVal))