import sys
sys.setrecursionlimit(999999999)

n=int(input())
a=list(map(int,input().split()))

sum=0
for ai in a:
    sum+=ai

print(sum*-1)