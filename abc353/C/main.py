import sys
sys.setrecursionlimit(999999999)


def main():
    N=int(input())
    #S=input().split()
    A=list(map(int,input().split()))
    
    p=pow(10,8)
    #A=[]
    #for _ in range(N):
    #    A.append(list(map(int,input().split())))
    sum=0
    bef=0
    c=0
    for n in range(1,N):
        v=A[N-n]+A[N-n-1]
        t=n*v+bef
        print(t)
        c+=int(t/p)
        sum+=t
        bef=v+bef
    
    ans=(sum%p)+(c*p)

    print(ans)
    

    pass


if __name__ == "__main__":
    main()
