import sys
import string
sys.setrecursionlimit(999999999)

def append_dict(ans_dict,ch,multi):
    if ch in ans_dict:
        ans_dict[ch]+=multi

def search_str(ans_dict,S,multi):
    i=0
    L=len(S)

    while(i<L):
        #print(S[i])
        roop_count=0
        if S[i].isdecimal():
            current_num=0
            n=[]
            for j in range(i,L):
                if S[j].isdecimal():
                    n.append(int(S[j]))
                else:
                    break
            #print(n)
            for j in range(len(n)):
                current_num+=n[j]
                current_num*=10
            current_num=int(current_num/10)
            
            i+=len(n)-1

            current_str=[]
            #print(S[i])
            if S[i+1]=="(":
                backet=1
                count=1
                for j in range(i+2,L):
                    count+=1
                    if S[j]=="(":
                        backet+=1
                    if S[j]==")":
                        backet-=1
                        if backet==0:
                            break
                    current_str.append(S[j])
                roop_count+=count
            else:
                current_str.append(S[i+1])
                roop_count+=1

            #print(current_num,current_str)
            #print(roop_count)
            search_str(ans_dict,current_str,current_num*multi)


        else:
            for j in range(i,L):
                if S[j].isdecimal():
                    break
                else:
                    append_dict(ans_dict,S[j],multi)
                    #print(S[j])
                    roop_count+=1
            roop_count-=1

        i+=roop_count
        i+=1


def main():
    S=list(input())
    ans_dict={}
    for s in string.ascii_lowercase:
        ans_dict[s]=0
    
    search_str(ans_dict,S,1)

    for k,v in zip(ans_dict.keys(),ans_dict.values()):
        print(k,v)

    pass


if __name__ == "__main__":
    main()
