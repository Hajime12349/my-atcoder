import sys
sys.setrecursionlimit(999999999)


def make_pattern(N):
    
    if N==0:
        return ["#"]
    
    white_pattern=[]
    pattern=make_pattern(N-1)
    new_pattern=[]
    
    for i in range(3):
        for j in range(pow(3,N-1)):
            tmp_text=""
            
            for k in range(3):
                if i==1 and k==1:
                    white_text=""
                    if N==1:
                        white_text="."
                    else:
                        for p in range(pow(3,(N-1))):
                            white_text+="." 
                    tmp_text+=white_text
                else:
                    tmp_text+=pattern[j]
            new_pattern.append(tmp_text)
                
    return new_pattern

def print_lst(lst,now):
    if len(lst)==1:
        print(lst[0],end="")

    for i in range(3):
        print_lst(lst[now+i],now+i)
    

def main():
    N=int(input())

    ans=make_pattern(N)
    
    for a in ans:
        print(a)
    

    #S=input().split()
    #A=list(map(int,input().split()))
    
    #A=[]
    #for _ in range(N):
    #    A.append(list(map(int,input().split())))
    pass


if __name__ == "__main__":
    main()
