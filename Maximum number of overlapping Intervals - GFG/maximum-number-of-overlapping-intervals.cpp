//{ Driver Code Starts
/* Driver program to test above function */

#include<bits/stdc++.h>
using namespace std;

// } Driver Code Ends
//User function Template for C++


class Solution{
   public:
   int overlap(vector<pair<int,int>>intervals, int n){
       vector<int> v(100005);

 /* making vector of this size as constraints in the problem are wrong as specified as 4*1000 however its not the same */
       for(auto &i:intervals)
       {
           v[i.first]++;
           v[i.second+1]--;
       }
       int ans=0;
       for(int i=1;i<v.size();i++)
       {
               v[i]+=v[i-1];
       }
       return *max_element(v.begin(),v.end());
   }
};

//{ Driver Code Starts.
int main()
{
	int t;
	cin>>t;
	while(t--)
	{
	    int n;
	    cin >> n;
	    vector<pair<int,int>>intervals;
	    for(int i = 0; i < n; i++){
	        int a, b;
	        cin >> a >> b;
	        intervals.push_back({a, b});
	    }
	    Solution ob;
	    int ans = ob.overlap(intervals, n);
	    cout << ans <<endl;
	}
	return 0;
}

// } Driver Code Ends