#AdarshChaurasia

def main():
    x,y = map(int,input().split())
    
    c=1
    while x!=y:
        x=(x-1)+x
        c+=1

    print(c)
main()
