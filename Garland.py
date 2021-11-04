for i in range(int(input())):
    s=input()
    if len(s)%2!=0 :
        print("no")
    elif s.count('R')!=s.count('G'):
        print("no")
    else:
        c=0
        for i in range(1,len(s)):
            if (s[i]==s[i-1]):
                c=c+1
        if c<=2:
            print("yes")
        else:
            print("no")
