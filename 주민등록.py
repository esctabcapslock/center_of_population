import csv
import csv

def trim(x):
    s=e=0;
    if (x.count(' ')==len(x)): return '';
    for i in range(len(x)):
        if (x[i]==' '): s+=1;
        else: break;
        
    for i in range(1,len(x)+1):
        if (x[-i]==' '): e+=1;
        else: break;
    
    return x[s:-e] if e else x[s:] 

def get_주민등록인구(filename):
    f = open(filename+'.csv','r',encoding='utf-8-sig')
    rdr = csv.reader(f)
    행정기관코드=[];
    행정기관=[]
    총인구수=[]
    세대수=[]
    cnt = 0
    for line in rdr:
        cnt+=1;
        if (cnt<4):
            first=False
            continue;

        행정기관코드.append(line[0])
        행정기관.append(trim(line[1]))
        총인구수.append(int(line[2].replace(',','')) if line[2] else 0)
        세대수.append(int(line[3].replace(',','')) if line[3] else 0)
    
    return 행정기관코드, 행정기관, 총인구수, 세대수
    f.close()

    
def get_행정기관좌표(행정기관코드):
    행정기관좌표=[0]*len(행정기관코드)
    f = open('중심좌표.csv','r',encoding='utf-8-sig')
    rdr = csv.reader(f)
    for line in rdr:
        if (line[0] not in 행정기관코드): continue;
        ind = 행정기관코드.index(line[0])
        행정기관좌표[ind]=[line[2],line[3]]
    f.close()
    return 행정기관좌표;