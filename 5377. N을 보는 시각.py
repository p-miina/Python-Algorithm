h = [str(i) for i in range(24)]
m = [str(i) for i in range(60)]
s = [str(i) for i in range(60)]

n = int(input())
cnt = 0
for hour in h:
    for mn in m:
        for sec in s:
            time = hour+mn+sec
            if str(n) in time:
                cnt+=1
                
print(cnt)
