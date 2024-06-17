import sys
from collections import deque
sys.setrecursionlimit(999999999)


def main():
    #N=int(input())
    #S=input().split()
    n,a=map(int,input().split())
    t=list(map(int,input().split()))
    q=deque([])
    time=0
    idx=0
    left=-1
    ans=[]
    is_end=False

    while True:

        if not is_end:
            if t[idx]<=time:
                #print(t[idx])
                q.append(t[idx])
                if idx==n-1:
                    is_end=True
                idx+=1
            
        #print(left)
        #print(is_end)
        if left==0:
            ans.append(time)
            
        if left<=0 and len(q)!=0:
            tmp=q.popleft()
            #print(tmp)
            left=a
        
        if is_end and len(q)==0 and left<=0:
            break

        
        left-=1
        time+=1
    
    for i in ans:
        print(i)




if __name__ == "__main__":
    main()
