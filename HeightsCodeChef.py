# cook your dish here
try:
    for _ in range(int(input())):
        N = int(input())
        arr=list(map(int,input().split()))
        res_Arr = [0]*N
        for i in range(len(arr)-1):
            if(arr[i]==arr[i+1]):
                res_Arr[i],res_Arr[i+1]=1,1
                i+=1
            else:
                res_Arr[i],res_Arr[i+1]=0,0
    print(res_Arr)
except:
    print("error")
