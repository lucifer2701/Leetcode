class Solution {
public:
    bool increasingTriplet(vector<int>& nums) {
        if(nums.size()<3) return false;
        int fmin=INT_MAX,smin=INT_MAX;
        for(int& num :nums){
            if(num<=fmin) fmin=num;
            else if(num<=smin) smin=num;
            else return true;
        }
        return false;
    }
};