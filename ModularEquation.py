#Adarsh_chaurasia

def validPairs(n,m):
    l=[]
    for i in range(1,n+1):
        a=i
        b=i+1
        s1=(m%a)%b
        s2=(m%b)%a
        if s1==s2:
            l.append([a,b])

            
    print(l)
    return len(l)
    
                
        



if __name__=="__main__":
    T = int(input())
    while T:
        N , M = map(int,input().split())
        res=validPairs(N,M)
        print(res)
        T-=1
        
