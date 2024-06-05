import sys
sys.setrecursionlimit(999999999)


def main():
    N=int(input())
    
    ans=0
    sum=0
    for i in range(100000):
        sum+=pow(2,i)
        if sum>N:
            print(i+1)
            break

    
    
    #S=input().split()
    #A=list(map(int,input().split()))
    
    #A=[]
    #for _ in range(N):
    #    A.append(list(map(int,input().split())))
    pass


if __name__ == "__main__":
    main()
