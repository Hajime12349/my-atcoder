import sys
sys.setrecursionlimit(999999999)


def main():
    #N=int(input())
    #S=input().split()
    N,M=map(int,input().split())
    H=list(map(int,input().split()))
    
    ans=-1
    for n in range(N):
        M-=H[n]
        if M<0:
            ans=n
            break
    if(ans==-1):
        print(N)
    else:
        print(ans)
    
    # pass


if __name__ == "__main__":
    main()
