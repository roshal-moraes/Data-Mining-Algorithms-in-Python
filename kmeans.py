import csv
import random
import math

num=list()
n=list()
cluster=list()
clust=list()
fir=1
ct=0
iter=1
with open('kdata.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        
        if fir==1:
            fir=2
            continue
        i=int(row[0])
        j=int(row[1])
        num.append([i,j])
l=len(num)
k=int(input("Enter number of clusters:"))
k1=k
m=list()
nt=0
print(num)
while k!=0:
    i=random.randint(0,l)%l
    mean=num[i]
    if mean in m:
        continue
    m.append(mean)
    cluster.append([[0,0]])
    k-=1
m1=m.copy()
while(1):
    print("Iteration = "+str(iter))
    iter+=1
    for j in num:
        n.clear()
        for k in m:
            e=math.sqrt((j[0]-k[0])**2+(j[1]-k[0])**2)
            n.append(e)
        mi=min(n)
        cluster[n.index(mi)].append(j)
    for e in range(0,k1):
        print("Mean for cluster "+str(e)+"="+str(m[e]))
    print("x y cluster")
    for e in range(0,k1):
        
        for cl in cluster[e]:
            if(cl!=[0,0]):
                print(cl[0],cl[1],e)

    m.clear()
    for a in range(0,k1):
        
        s1=0
        s2=0

        le=len(cluster[a])
        for b in cluster[a]:
            s1=s1+b[0]
            s2=s2+b[1]
        s1=s1/(le-1)
        s2=s2/(le-1)
        m.append([s1,s2])

    if(m==m1):
            break
    
    clust=cluster
    cluster.clear()
    m1=m.copy()
    for i in range(0,k1):
        cluster.append([[0,0]])
