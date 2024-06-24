import sys
sys.setrecursionlimit(999999999)

def main():
    #N=int(input())
    #S=input().split()
    sx,sy=map(int,input().split())
    tx,ty=map(int,input().split())

    cityx=abs(sx-tx)
    cityy=abs(sy-ty)

    costy=cityy

    costx=0
    if((sx+ty)%2==0):
        costx+=cityx/2
        if((tx+ty)%2==1 and sx>tx):
            costx+=1
    elif((sx+ty)%2==1):
        costx+=cityx/2
        if((tx+ty)%2==0 and sx<tx):
            costx+=1

    costx-=(cityy-1)
    ans=max(0,int(costx))+costy

    print(ans)

    #A=list(map(int,input().split()))

    #A=[]
    #for _ in range(N):
    #    A.append(list(map(int,input().split())))
    pass

if __name__ == "__main__":
    main()
