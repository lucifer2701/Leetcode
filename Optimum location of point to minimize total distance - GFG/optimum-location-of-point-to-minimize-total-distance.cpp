//{ Driver Code Starts
/* Driver program to test above function */

#include<bits/stdc++.h>
using namespace std;

// } Driver Code Ends
//User function Template for C++
class Solution{

    public:

    double findOptimumCost(tuple<int,int,int> t, vector<pair<int,int>> v, int n){

        int a = get<0>(t), b = get<1>(t), c = get<2>(t);

       

        auto y_cor = [&](double x){

            return ((-1*c) + (-1*a*x))/b;

        };

   

        auto f = [&](double x){

            double y = y_cor(x);

            double ans = 0;

            for(int i=0; i<n; i++){

                ans += sqrt((x-v[i].first)*(x-v[i].first) + (y-v[i].second)*(y-v[i].second));

            }

            return ans;

        };

   

        double l = -1e5, r = 1e5, eps = 1e-4;          

        while (r - l > eps) {

            double m1 = l + (r - l) / 3;

            double m2 = r - (r - l) / 3;

            double f1 = f(m1);     

            double f2 = f(m2);

            if (f1 >= f2)

                l = m1;

            else

                r = m2;

        }

           

        return f(l);

    }

};

//{ Driver Code Starts.
int main()
{
	int t;
	cin>>t;
	while(t--)
	{
	    tuple<int,int,int>line;
	    int a, b, c;
	    cin >> a >> b >> c;
	    line = make_tuple(a, b, c);
	    int n;
	    cin >> n;
	    vector<pair<int,int>>points;
	    for(int i = 0 ; i < n; i++){
	        int x, y;
	        cin >> x >> y;
	        points.push_back({x, y});
	    }

	    Solution ob;
	    double ans = ob.findOptimumCost(line, points, n);

	    cout << fixed << setprecision(2) << ans << endl;
	}
	return 0;
}

// } Driver Code Ends