//{ Driver Code Starts


#include<bits/stdc++.h>
using namespace std;

// } Driver Code Ends

#define ip pair<int,int>
class ST{
    public:
    ip *tree;
    ST(int n){
        tree = new ip[4*n+1];
    }
    
    void build(int node,int start,int end,vector<int> &a){
        if(start==end){
            tree[node] = {1,1};
            return;
        }
        int mid = (end+start)>>1, lc=(node<<1), rc = lc|1;
        build(lc,start,mid,a);
        build(rc,mid+1,end,a);
        tree[node] = {0,0};
        if(a[mid-1]<=a[mid+1-1])
            tree[node].first = tree[lc].first+tree[rc].first;
        if(a[mid-1]>=a[mid+1-1])
            tree[node].second = tree[lc].second+tree[rc].second;
    }
    
    ip query(int node,int start,int end,int l,int r,vector<int> &a){
        if(l>end || r<start)
            return {0,0};
        if(l<=start && r>=end)
            return tree[node];
        int mid = (end+start)>>1, lc=(node<<1), rc = lc|1;
        ip le = query(lc,start,mid,l,r,a), ri = query(rc,mid+1,end,l,r,a),ans;
        if(l<=mid && r>=mid+1){
            if(a[mid-1]<=a[mid+1-1])
                ans.first = le.first+ri.first;
            if(a[mid-1]>=a[mid+1-1])
                ans.second = le.second+ri.second;
        }
        else if(r<=mid)
            ans=le;
        else if(l>=mid+1)
            ans=ri;
        return ans;
    }
    
    void update(int node,int start,int end,int ind,int val,vector<int> &a){
        if(start==end)
            return;
        int mid = (end+start)>>1, lc=(node<<1), rc = lc|1;
        if(ind<=mid){
            update(lc,start,mid,ind,val,a);
            tree[node] = {0,0};
            if(a[mid-1]<=a[mid+1-1])
                tree[node].first = tree[lc].first+tree[rc].first;
            if(a[mid-1]>=a[mid+1-1])
                tree[node].second = tree[lc].second+tree[rc].second;
        }
        else{
            update(rc,mid+1,end,ind,val,a);
            tree[node] = {0,0};
            if(a[mid-1]<a[mid+1-1])
                tree[node].first = tree[lc].first+tree[rc].first;
            if(a[mid-1]>=a[mid+1-1])
                tree[node].second = tree[lc].second+tree[rc].second;
        }
            
    }
};

class Solution {
public:
  vector<int>solveQueries(vector<int> nums, vector<vector<int>>Q){
    int n=nums.size();
    ST st(n);
    st.build(1,1,n,nums);
    vector<int> ans;
    int inc,dec;
    for(auto q: Q){
        if(q[0]==1){
            nums[q[1]-1]=q[2];
            st.update(1,1,n,q[1],q[2],nums);
        }
        else{
            tie(inc,dec) = st.query(1,1,n,q[1],q[2],nums);
            if(inc==dec)
                ans.push_back(-1);
            else if(inc==q[2]-q[1]+1)
                ans.push_back(0);
            else if(dec==q[2]-q[1]+1)
                ans.push_back(1);
            else
                ans.push_back(-1);
        }
    }
    return ans;
  }

};


//{ Driver Code Starts.
int main(){
	int tc;
	cin >> tc;
	while(tc--){
		int n;
		cin >> n;
		vector<int>nums(n);
		for(int i = 0; i < n; i++)cin >> nums[i];
		int q;
		cin >> q;
		vector<vector<int>>Queries;
		for(int i = 0; i < q; i++){
			int x, y, z;
			cin >> x >> y >> z;
			Queries.push_back({x,y,z});
		}
		Solution obj;
		vector<int>ans = obj.solveQueries(nums, Queries);
		for(auto i: ans)cout << i << "\n";
	}
	return 0;
}
// } Driver Code Ends