//{ Driver Code Starts


#include<bits/stdc++.h>
using namespace std;

// } Driver Code Ends


const int MAX = 1000010;

 

long long iter, was[MAX];

int pa[MAX], pb[MAX];

vector <int> g[MAX];

class Solution {

public:
bool dfs(int v) {

                  was[v] = iter;

                  for (int j : g[v]) {

                    if (pb[j] == -1) {

                      pa[v] = j;

                      pb[j] = v;

                      return true;

                    }

                  }

                  for (int j : g[v]) {

                    if (was[pb[j]] != iter) {

                      if (dfs(pb[j])) {

                        pa[v] = j;

                        pb[j] = v;

                        return true;

                      }

                    }

                  }

                  return false;

                }

                int MaxmimumLength(vector<vector<int>>nums){

                                int n = nums.size();

                                for(int i = 0; i < MAX; i++)

                                    g[i].clear();

                                for(int i = 0; i < n; i++){

                                                for(int j = 0; j < 6; j++){

                                                                g[nums[i][j]].push_back(i);

                                                }

                                }

                for(int i = 0; i < MAX; i++)

                                random_shuffle(g[i].begin(), g[i].end());

                    for (int i = 0; i < MAX; i++) {

                      pa[i] = -1;

                      was[i] = -1;

                    }

                    for (int j = 0; j < n; j++) {

                      pb[j] = -1;

                    }

                    int ans = 0;

                    int rr = 0;

                    iter = 0;

                    for (int ll = 1; ll < MAX; ll++) {

                      rr = max(rr, ll - 1);

                      while (true) {

                        iter++;

                        if (dfs(rr + 1)) {

                          rr++;

                        } else {

                          break;

                        }

                      }

                      ans = max(ans, rr - ll + 1);

                      if (pa[ll] != -1) {

                        pb[pa[ll]] = -1;

                        pa[ll] = -1;

                      }

                                }
ans=ans+1;
ans=ans-1;
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
		vector<vector<int>>nums(n, vector<int>(6, 0));
		for(int i = 0; i < n; i++){
			for(int j = 0; j < 6; j++)
				cin >> nums[i][j];
		}
		Solution obj;
		int ans = obj.MaxmimumLength(nums);
		cout << ans << "\n";
	}
	return 0;
}

// } Driver Code Ends