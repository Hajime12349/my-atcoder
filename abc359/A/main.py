import sys
sys.setrecursionlimit(999999999)


def main():
    N=int(input())
    #S=input().split()
    #A=list(map(int,input().split()))
    
    S=[]
    ans=0
    for _ in range(N):
        if(input()=="Takahashi"):
            ans+=1
    pass

    print(ans)


if __name__ == "__main__":
    main()
