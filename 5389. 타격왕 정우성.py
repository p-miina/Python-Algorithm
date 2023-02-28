x, y = map(int, input().split())
maxi = 1000000000
res=0
i=0
if x == y:
    print(-1)
else:
    if int(((y+maxi)/(x+maxi))*100)<=int((y/x)*100):
        print(-1)
    else:
        while res <= int((y/x)*100):
            if i == 1000000000:
                print(i)
                break
            if int(((y+maxi//10)/(x+maxi//10))*100)<=int((y/x)*100):
                i+= maxi//10
            else:
                i+=1
            res = int(((y+i)/(x+i))*100)
        print(i)
