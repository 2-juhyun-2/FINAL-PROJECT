import csv, re
import matplotlib.pyplot as plt


with open('C:\\최종 프로젝트\\finalproject\\FINAL-PROJECT\\myproject\\policy\\views\\MOCK_DATA.csv', 'r', encoding="utf-8") as file:
    datas = csv.reader(file)
    for data in datas:
        print(data)



with open('C:\\최종 프로젝트\\finalproject\\FINAL-PROJECT\\myproject\\policy\\views\\Region_name_0.csv', 'r',encoding="utf-8") as file:
    csv_file = csv.reader(file)
    seoul=0 
    busan=0 
    inchun=0
    daegu=0
    gyungki=0
    chungbuk=0
    chungnam=0
    junbuk=0
    junnam=0
    gang=0
    jeju=0
    na=0
    for line in csv_file:
        if line[1] == '서울특별시':
            seoul +=1
        elif line[1] == '부산광역시':
            busan +=1
        elif line[1] == '인천광역시':
            inchun +=1
        elif line[1] == '대구광역시':
            daegu +=1
        elif line[1] == '경기도':
            gyungki +=1
        elif line[1] == '충청북도':
            chungbuk +=1
        elif line[1] == '충청남도':
            chungnam +=1
        elif line[1] == '전라북도':
            junbuk +=1
        elif line[1] == '전라남도':
            junnam +=1
        elif line[1] == '강원도':
             gang+=1
        elif line[1] == '제주특별자치도':
            jeju +=1
        else:
            na +=1
        value=max(seoul,busan,inchun,daegu,gyungki,chungbuk,chungnam,junbuk,junnam,gang,jeju,na)
print(value)
print(chungbuk)

ratio = [seoul,busan,inchun,daegu,gyungki,chungbuk,chungnam,junbuk,junnam,gang,jeju,na]
labels = ['seoul','busan','inchun','daegu','gyungki','chungbuk','chungnam','junbuk','junnam','gang','jeju','na']

plt.pie(ratio, labels=labels, autopct='%.1f%%')
plt.show()