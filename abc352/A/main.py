import sys
sys.setrecursionlimit(999999999)


def main():
    #N=int(input())
    #S=input().split()
    N,X,Y,Z=map(int,input().split())
    
    #A=[]
    #for _ in range(N):
    #    A.append(list(map(int,input().split())))
    ans="No"
    if X<Y and Z>X and Y>Z:    
        ans="Yes"
    elif X>Y and Z<X and Y<Z:
        ans="Yes"

    print(ans)

    pass


if __name__ == "__main__":
    main()
