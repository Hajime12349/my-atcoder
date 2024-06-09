import sys
sys.setrecursionlimit(999999999)


def main():
    S=input()
    
    len_s=len(S)
    lower = sum(map(str.islower, S))
    
    if int(len_s/2)<lower:
        print(S.lower())
    else:
        print(S.upper())
    
    #pass


if __name__ == "__main__":
    main()
