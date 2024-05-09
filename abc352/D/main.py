import sys
sys.setrecursionlimit(999999999)


def main():
    #N=int(input())
    #S=input().split()
    N,K=map(int,input().split())
    P=list(map(int,input().split()))
    P_copy=P.copy()

    B=[0]*(N+1)
    C=[i for i in range(N)]

    count=0
    for p in P:
        #print(a)
        B[p]=count
        count+=1
    #print(B)
    #ans = []
    B_copy=B.copy()
    for i in range(N):
        if P[i] == i+1:
            continue
        idx = B[i+1]
        P[i],P[idx] = P[idx],P[i]
        B[i+1],B[P[idx]]=i,B[i+1]
        C[i],C[idx]=C[idx],C[i]

    min_v=N+1
    #print(P,C)
    for n in range(0,N-(K-1)):
        #print(C[n],C[n+K-1])
        min_k=N
        max_k=0
        for k in range(K):
            min_k=min(min_k,C[n+k])
            max_k=max(max_k,C[n+k])
        diff=abs(max_k-min_k)
        min_v=min(min_v,diff)

    print(min_v)
        


if __name__ == "__main__":
    main()
