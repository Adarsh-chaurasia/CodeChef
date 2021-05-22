#adarshChaurasia

def main():
    t=int(input())
    for _ in range(t):
        a,b=map(int,input().split())
        arr1=set(map(int,input().split()))
        arr2=set(map(int,input().split()))

        

        print(len(arr1&arr2))
        
main()
