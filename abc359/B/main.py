import sys
sys.setrecursionlimit(999999999)


def main():
    N=int(input())
    #S=input().split()
    A=list(map(int,input().split()))
    
    ans=0
    if len(A)>2:
        for i in range(2,N*2):
            if(A[i]==A[i-2]):
                ans+=1
        
    print(ans)



if __name__ == "__main__":
    main()
