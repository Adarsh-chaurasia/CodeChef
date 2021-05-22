#Adarsh Chaurasia

def main():
    t = int(input())
    for _ in range(t):
        list1=[]
    
        n , b=map(int,input().split())
        for i in range(n):
            x=[]
            x=list(map(int,input().split()))
            if x[2]<=b:
                list1.append(x[0]*x[1])
                
                
        if list1:
            print(max(list1))
        else:
            print("no tablet")
            
main()
