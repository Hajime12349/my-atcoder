import sys
sys.setrecursionlimit(999999999)


def main():
    #N=int(input())
    #S=input().split()
    N,M=map(int,input().split())
    A=list(map(int,input().split()))
    X=[]
    for _ in range(N):
        X.append(list(map(int,input().split())))
    
    ans=[0]*M

    for row in X:
        for i in range(M):
            ans[i]+=row[i]
    
    ans_str="Yes"
    #print(ans)
    for i in range(M):
        if (ans[i]<A[i]):
            ans_str="No"
            break
    
    print(ans_str)

    pass


if __name__ == "__main__":
    main()
