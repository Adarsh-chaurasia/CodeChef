#adarshChaurasia
def solve(D,d,P,Q):
    n = (D//d)+1
    r = (d*(n*(2*P+(n-1)*Q))//2) + (D-n*d)*(P+(n-1)*Q)
    return r
    
def main():
    for _ in range(int(input())):
        D,d,P,Q = map(int,input().split())
        res=0
        res = solve(D,d,P,Q)
        
        print(res)
        
        
main()
