#AdarshChaurasia
def main():
    t=int(input())
    for _ in range(t):
        size=int(input())
        array=list(map(int,input().split()))
        counter=[0]*1001
        for i in range(size):
            counter[array[i]]+=1 
        area=1
        done=False
        flag=False
        for i in range(1000,-1,-1):
            if flag is not True:
                if counter[i] >= 2:
                    area = area * i
                    flag = True
                    counter[i] -= 2
        
            if flag:
                if counter[i] >= 2:
                    area = area * i
                    done = True
                    break
          
            
                
        if done:
            print(area)
            
        else: 
            print(-1)
            
            
main()
