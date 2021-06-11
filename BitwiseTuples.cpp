#include <iostream>
using namespace std;
#define mod 1000000007

long long int getPower(long long int a,long long int b){
    long long int res=1;
    
    while(b>0){
        if (b%2==1)
        res=(res*a)%mod;
    a=(a*a)%mod;
    b=b>>1;
        
        
    }
    return res;}
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    long long int t,m,n;
    cin>>t;
    while(t--){
        cin>>n>>m;
        long long int x=getPower(2,n)-1;
        long long int result=getPower(x,m);
        cout<<result<<endl;
    }
	return 0;
}
