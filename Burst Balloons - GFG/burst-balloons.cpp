//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends


class Solution {
public:

    int solve(int i, int j, vector<int>&nums,vector<vector<int>>&dp){

        if(i > j) return 0;

        if(dp[i][j] != -1) return dp[i][j];

        int maxi = INT_MIN;

        for(int k=i;k<=j;k++){

            int ans = nums[i-1]*nums[k]*nums[j+1] + solve(i, k-1, nums,dp) + solve(k+1, j, nums,dp);

            if(maxi < ans) maxi = ans;

        }  

        return dp[i][j] = maxi;

    }

    int maxCoins(int N, vector<int> &nums) {

        int n = nums.size();

        vector<vector<int>>dp(n+2, vector<int>(n+1, -1));

        nums.push_back(1);

        nums.insert(nums.begin(), 1);

        return solve(1, n, nums,dp);

    }


};


//{ Driver Code Starts.

int main() {
    int t;
    cin >> t;
    while (t--) {
        int N;
        cin>>N;
        
        vector<int> arr(N);
        for(int i=0; i<N; i++)
            cin>>arr[i];

        Solution obj;
        cout << obj.maxCoins(N, arr) << endl;
    }
    return 0;
}
// } Driver Code Ends