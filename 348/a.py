import sys
sys.setrecursionlimit(999999999)

n=int(input())
#s=input().split()
#a=list(map(int,input().split()))

ans=''
for i in range(n):
    if (i+1)%3==0:
        ans+='x'
    else :
        ans+='o'

print(ans)
