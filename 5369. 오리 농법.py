n = int(input())

farm = []
for _ in range(n):
    f = list(map(int, input().split()))
    farm.append(f)
    
row = []
for i in range(n):
    if 1 in farm[i]:
        continue
    else:
        row.append(i)
        
for j in range(n):
    cp = 0
    for z in range(n):
        if farm[z][j]==1:
            cp = 1
            break
    if cp ==0:
        for r in row:
            farm[r]=[0]*n
        for x in range(n):
            farm[x][j]=0
 
 
cnt=0
for i in farm:
    cnt+=i.count(2)
               
print(cnt)
