import decimal
a,b = map(int,input().split())
n = int(input())
decimal.getcontext().prec=n+1
print(round(decimal.Decimal(a)/b,n))
