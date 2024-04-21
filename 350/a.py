import sys
sys.setrecursionlimit(999999999)

s=input()
#s_n=s[3:]
s_n=int(s[3:])

if s_n>0 and s_n<350 and s_n!=316:
    print("Yes")
else:
    print("No")


