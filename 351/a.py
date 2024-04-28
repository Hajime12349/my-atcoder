import sys
sys.setrecursionlimit(999999999)

#n=int(input())
#s=input().split()
A=list(map(int,input().split()))
B=list(map(int,input().split()))

ap=0
bp=0
for a in A:
    ap+=a
for b in B:
    bp+=b

ans=ap-bp+1

print(ans)


# for _ in range(N):
#     a.append(list(map(int,input().split())))


