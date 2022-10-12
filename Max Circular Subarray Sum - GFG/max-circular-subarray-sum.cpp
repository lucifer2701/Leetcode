//{ Driver Code Starts
#include<bits/stdc++.h>
using namespace std;


// } Driver Code Ends
class Solution{
    public:
    // arr: input array
    // num: size of array
    //Function to find maximum circular subarray sum.
    int circularSubarraySum(int arr[], int num){
        
        // your code here
        int curr=0,curr1=0,maxi=arr[0],mini=arr[0],sum=0;
        for(int i=0;i<num;i++){
              curr=max(curr+arr[i],arr[i]);
               maxi=max(curr,maxi);
             curr1=min(curr1+arr[i],arr[i]);
            mini=min(mini,curr1);
            sum+=arr[i];
        }
        if(mini==sum){
            return maxi;
        }
        return max(maxi,sum-mini);
    }
};

//{ Driver Code Starts.

int main()
 {
	int T;
	
	//testcases
	cin>> T;
	
	while (T--)
	{
	    int num;
	    
	    //size of array
	    cin>>num;
	    int arr[num];
	    
	    //inserting elements
	    for(int i = 0; i<num; i++)
	        cin>>arr[i];
	        
	    Solution ob;
	    //calling function
	    cout << ob.circularSubarraySum(arr, num) << endl;
	    
	}
	
	return 0;
}
// } Driver Code Ends