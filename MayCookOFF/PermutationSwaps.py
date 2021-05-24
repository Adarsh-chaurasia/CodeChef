#AdarshChaurasia
def main():
    for _ in range(int(input())):
        n=int(input())
        a=list(map(int,input().split()))
        p=list(map(int,input().split()))
        b=[0]*n
        
        q=int(input())
        for _ in range(q):
            l=list(map(int,input().split()))
            if l[0]==1:
                for i in range(0,n):
                    b[p[i]-1]=a[i]
            elif l[0]==2:
                b[l[1]-1],b[l[2]-1]=b[l[2]-1],b[l[1]-1]
            elif l[0]==3:
                print(b[l[1]-1])
        


if __name__ == '__main__':
    main()
