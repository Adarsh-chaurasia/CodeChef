#AdarshChaurasia

def main():
    x=int(input())
    
    #500rs --> 1000 ch pack
    #5 rs --> 5 choclate pack
    
    bigpack=x//500
    x=x-500*bigpack
    smallpack=x//5
    print(bigpack,smallpack)
    finalcost=1000*bigpack+5*smallpack
    
    print(finalcost)
    
main()
