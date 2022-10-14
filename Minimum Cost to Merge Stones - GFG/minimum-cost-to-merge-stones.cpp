//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends
class Solution {
public:

    int dp[40][40];

    int helper(vector<int>& arr, int start, int end, vector<int>& prefix, int k){

        if(end - start <= k - 2){

            return 0;

        }

        if(dp[start][end] != -1){

            return dp[start][end];

        }

        int mini = INT_MAX;

       for(int j = start; j < end; j += k - 1){

            int left = helper(arr, start, j, prefix, k);

            int right = helper(arr, j + 1, end, prefix, k);

            mini = min(mini, left + right);

        }

        if((end - start) % (k - 1) == 0){

            int sum = 0;

            sum += prefix[end];

            if(start > 0){

                sum -= prefix[start - 1];

            }

            mini += sum;

        }

        return dp[start][end] = mini;

    }

    int mergeStones(vector<int> &arr, int n, int k) {

        memset(dp, -1, sizeof(dp));

        if((n - 1) % (k - 1)){

            return -1;

        }

        vector<int> prefix(n, 0);

        prefix[0] = arr[0];

        for(int i = 1; i < n; i++){

            prefix[i] = prefix[i - 1] + arr[i];

        }

        return helper(arr, 0, n - 1, prefix, k);
    }
    };


//{ Driver Code Starts.

int main() {
    int t;
    cin >> t;
    while (t--) {
        int N, K; 
        cin >> N >> K;
        
        vector<int> stones(N);
        
        for(int i=0;i<N;i++) {
            cin>>stones[i];
        }
        
        Solution obj;
        
        cout << obj.mergeStones(stones, N, K) << endl;
        
    }
    return 0;
}
// } Driver Code Ends