a,b=map(int,input().split())
m=list(map(int,input().split()))
n=list(map(int,input().split()))
d=[]
count=0
for i in m:
    if i in n and i not in d:
        d.append(i)
        count+=1
print(count)        
