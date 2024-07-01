import sys
from collections import deque
sys.setrecursionlimit(999999999)
ans=1

def check_valid(i,s,max_i):
    s_len=len(s)
    if(i+1>=s_len):
        return(max_i)
    elif(i-1<0):
        return(max_i)
    else:
        max_i=check(i,s,max(i,max_i))
        return(max_i)

def check(i,s,max_i):
    ths=s[i-1:i+1]
    if ths=="aba":
        tms_s=s[:i-2]+"a"+s[i+2:]
        check_valid(i,tmp_s,max_i)
        check_valid(i-1,tmp_s,max_i)
        check_valid(i+1,tmp_s,max_i)
        ans+=1
    elif ths=="bab":
        tms_s=s[:i-2]+"b"+s[i+2:]
        check_valid(i,tmp_s,max_i)
        check_valid(i-1,tmp_s,max_i)
        check_valid(i+1,tmp_s,max_i)
        ans+=1
    else:
        return(max_i)


def main():
    N=int(input())
    S=input()
    q=deque()

    i=1
    while(i<N):
        max_i=i
        check_valid(i,s,max_i)


    check_valid(1,S)

    print(ans)

if __name__ == "__main__":
    main()
