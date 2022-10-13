//{ Driver Code Starts
/* Driver program to test above function */

#include<bits/stdc++.h>
using namespace std;

// } Driver Code Ends
//Back-end complete function Template for C++

class Solution{
    public:
    vector<int> findLeastGreater(vector<int>&v, int n) {
        set<int>record;
        record.insert(v[n-1]);
        vector<int>res(1,-1);
        for(int i=n-2;i>=0;i--){
            record.insert(v[i]);
            auto up=record.upper_bound(v[i]);
            if(up==record.end())
                res.push_back(-1);
            else
                res.push_back(*up);
        }
        reverse(res.begin(),res.end());
        return res;
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
	    vector<int>arr(n);
	    for(int i = 0 ; i < n; i++){
	        cin >> arr[i];
	    }
	    Solution ob;
	    vector<int> ans = ob.findLeastGreater(arr, n);
	    for(auto it : ans){
	        cout << it << " ";
	    }
	    cout <<endl;
	}
	return 0;
}

// } Driver Code Ends