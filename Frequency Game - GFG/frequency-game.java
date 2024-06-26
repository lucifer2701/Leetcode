//{ Driver Code Starts
// Initial Template for Java

import java.util.*;
import java.io.*;

// Position this line where user code will be pasted.

// Driver class with main function
class GFG {
    // Main function
    public static void main(String[] args)throws IOException {
        BufferedReader in=new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(in.readLine());

        // Iterating over testcases
        while (t-- > 0) {
            int n = Integer.parseInt(in.readLine());
            int arr[] = new int[n];

            String s[]=in.readLine().trim().split(" ");
            for (int i = 0; i < n; i++) arr[i] = Integer.parseInt(s[i]);

            Solution obj = new Solution();
            System.out.println(obj.LargButMinFreq(arr, n));
        }
    }
}
// } Driver Code Ends


// User function Template for Java

// Helper class to find largest number with minimum frequency
class Solution {
    // Function to find largest number with minimum frequency
    public static int LargButMinFreq(int arr[], int n) {
        // Your code here
        HashMap<Integer, Integer> counter = new HashMap<>();
        for (int i = 0; i < n; i++) {
            counter.put(arr[i], counter.getOrDefault(arr[i], 0) + 1);
        }
        
        int minFreq = Integer.MAX_VALUE;
        for (int freq : counter.values()) {
            minFreq = Math.min(minFreq, freq);
        }
        
        int answer = 0;
        for (int num : counter.keySet()) {
            if (counter.get(num) == minFreq) {
                answer = Math.max(answer, num);
            }
        }
        
        return answer;
    }
}