import sys
sys.setrecursionlimit(999999999)


def main():
    N=int(input())
    #S=input().split()
    A=list(map(int,input().split()))
    
    #A=[]
    #for _ in range(N):
    #    A.append(list(map(int,input().split())))
    m=A[0]
    end=False
    for n in range(N):
        if m<A[n]:
            print(n+1)
            end=True
            break
    
    if not end:
        print(-1)

    
    pass


if __name__ == "__main__":
    main()
