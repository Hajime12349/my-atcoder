import sys
from bisect import bisect_left
from collections import deque
sys.setrecursionlimit(999999999)

def merge_sort(data):
    if len(data) <= 1:
        return data

    mid = len(data) // 2

    left = merge_sort(data[:mid])
    right = merge_sort(data[mid:])

    return merge(left, right)

def merge(left, right):
    result = []
    i, j = 0, 0

    while (i < len(left)) and (j < len(right)):
        if left[i] <= right[j]:
            result.append(left[i])   
            i += 1
        else:
            result.append(right[j])  
            j += 1

    if i < len(left):
        result.extend(left[i:]) 
    if j < len(right):
        result.extend(right[j:])

    return result


def main():
    #N=int(input())
    #S=input().split()
    N,M=map(int,input().split())
    A=list(map(int,input().split()))
    B=list(map(int,input().split()))
    is_possible=False

    A=merge_sort(A)

    B=deque(merge_sort(B))

    ans=0
    
    #print(A,B)

    now=-1
    for a in A:
        if now==-1:
            if len(B)==0:
                break
            else:
                now=B.popleft()
        
        if now<=a:
            #print(a)
            ans+=a
            now=-1

    
    if len(B)==0 and now==-1:
        is_possible=True

    if is_possible:
        print(ans)
    else:
        print(-1)
    
    pass


if __name__ == "__main__":
    main()
