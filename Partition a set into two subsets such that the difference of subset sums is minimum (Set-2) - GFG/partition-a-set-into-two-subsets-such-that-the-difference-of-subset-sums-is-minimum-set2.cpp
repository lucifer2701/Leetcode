//{ Driver Code Starts
//Initial Template for C++


#include<bits/stdc++.h>
using namespace std;



// } Driver Code Ends
//User function Template for C++

class Solution{

    public:

    void TOWUtil(vector<int>& arr, int n, bool* curr_elements, int no_of_selected_elements,

             bool* soln, int* min_diff, int sum, int curr_sum, int curr_position)

    {

        // checks whether the it is going out of bound

        if (curr_position == n)

            return;

    

        // checks that the numbers of elements left are not less than the

        // number of elements required to form the solution

        if ((n/2 - no_of_selected_elements) > (n - curr_position))

            return;

    

        // consider the cases when current element is not included in the solution

        TOWUtil(arr, n, curr_elements, no_of_selected_elements,

                  soln, min_diff, sum, curr_sum, curr_position+1);

    

        // add the current element to the solution

        no_of_selected_elements++;

        curr_sum = curr_sum + arr[curr_position];

        curr_elements[curr_position] = true;

    

        // checks if a solution is formed

        if (no_of_selected_elements == n/2)

        {

            // checks if the solution formed is better than the best solution so far

            if (abs(sum/2 - curr_sum) < *min_diff)

            {

                *min_diff = abs(sum/2 - curr_sum);

               for (int i = 0; i<n; i++)

                    soln[i] = curr_elements[i];

            }

        }

        else

        {

            // consider the cases where current element is included in the solution

            TOWUtil(arr, n, curr_elements, no_of_selected_elements, soln,

                      min_diff, sum, curr_sum, curr_position+1);

        }

    

        // removes current element before returning to the caller of this function

        curr_elements[curr_position] = false;

    }

     

    // main function that generate an arr

    vector<vector<int>> minDifference(vector<int>&arr, int n)

    {

        // the boolean array that contains the inclusion and exclusion of an element

        // in current set. The number excluded automatically form the other set

        bool* curr_elements = new bool[n];

    

        // The inclusion/exclusion array for final solution

        bool* soln = new bool[n];

    

        int min_diff = INT_MAX;

    

        int sum = 0;

        for (int i=0; i<n; i++)

        {

            sum += arr[i];

            curr_elements[i] =  soln[i] = false;

        }

    

        // Find the solution using recursive function TOWUtil()

        TOWUtil(arr, n, curr_elements, 0, soln, &min_diff, sum, 0, 0);

    

        // Print the solution

        // cout << "The first subset is: ";

        vector<vector<int>> ans;

        vector<int> p;

        for (int i=0; i<n; i++)

        {

            if (soln[i] == true){

                p.push_back(arr[i]);

            }

               

        }

        ans.push_back(p);

        p.clear();

        // cout << "\nThe second subset is: ";

        for (int i=0; i<n; i++)

        {

            if (soln[i] == false){

                p.push_back(arr[i]);

            }

        }

        ans.push_back(p);

        return ans;

    }

};

//{ Driver Code Starts.


int main(){
    int t;
    cin>>t;
    while(t--){
        int n;
        cin>>n;
        vector<int> arr(n);
        for(int i=0;i<n;i++){
            cin>>arr[i];
        }
        
        Solution obj;
        vector<vector<int>> ans = obj.minDifference(arr,n);
        //printing S1 and S2 arrays
        for(int i=0;i<ans.size();i++){
            for(int j=0;j<ans[i].size();j++){
                cout<<ans[i][j]<<" ";
            }
            cout<<endl;
        }
    }
}
// } Driver Code Ends