#AdarshChaurasiA
def maraThon(n,a,b,c):
    if n>=42:
        return c
    elif n>=21:
        return b
    elif n>=10:
        return a
    else:
        return 0
def main():
    for _ in range(int(input())):
        D,d,A,B,C=map(int,input().split())
        check=D*d
        
        result=maraThon(check,A,B,C)
        print(result)
if __name__ == '__main__':
    main()
