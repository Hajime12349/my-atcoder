import sys

sys.setrecursionlimit(999999999)



def main():

    N=int(input())

    #S=input().split()

    #A=list(map(int,input().split()))
    

    A=[]

    B=[]
    max_v=0

    max_idx=0

    ans=0

    for n in range(N):

        a,b=map(int,input().split())

        A.append(a)
        B.append(b)
        diff=b-a

        if max_v<diff:
            max_v=diff
            max_idx=n
    
    #print(A[max_idx])

    for n in range(N):

        if not n==max_idx:

            ans+=A[n]


    ans+=(B[max_idx])
    print(ans)


    pass



if __name__ == "__main__":
    main()

