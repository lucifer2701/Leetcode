//{ Driver Code Starts
#include<bits/stdc++.h>
using namespace std;


// } Driver Code Ends

 
class AutoCompleteSystem {

public:

    typedef pair<string, int> psi;

    struct comp {

        bool operator() (const pair<string, int> &a, const pair<string, int> & b){

            if(a.second == b.second)

                return a.first < b.first;

            return a.second > b.second;

        }

    };

 

    struct node {

        node* links[27];

        set<pair<string, int>, comp> st;

        int end;

        node() {

            for(int i = 0; i < 27; i++)

                links[i] = nullptr;

            end = 0;

        }

    };

   

    node* root = new node;

    string out = "";

     void add(string &word, int times) {

        node* t = root;

        for(auto x : word) {

            if(x == ' ') {

                if(!t->links[26])

                    t->links[26] = new node;

                t = t->links[26];

                t->st.insert({word, times});

                continue;

            }

            if(!t->links[x - 'a'])

                t->links[x - 'a'] = new node;

            t = t->links[x - 'a'];

            t->st.insert({word, times});

        }

        t->end += times;

    }

    AutoCompleteSystem(vector<string>& sentences, vector<int>& times) {

        for(int i = 0; i < times.size(); i++)

            add(sentences[i], times[i]);

    }

 

   

    int getCnt(string &word) {

        node* t = root;

        for(auto x : word) {

            if(x == ' ') {

                if(!t->links[26]) return 0;

                t = t->links[26];

                continue;

            }

            if(!t->links[x - 'a']) return 0;

            t = t->links[x - 'a'];

        }

        return t->end;

    }

    void erase_nd_update(string &word, int cnt) {

        node* t = root;

        for(auto x : word) {

            if(x == ' ') {

                t = t->links[26];

                auto itr = t->st.find({word, cnt});

                t->st.erase(*itr);

                t->st.insert({word, cnt + 1});

                continue;

            }

            else

                t = t->links[x - 'a'];

            auto itr = t->st.find({word, cnt});

            t->st.erase(*itr);

            t->st.insert({word, cnt + 1});

        }

        t->end++;

    }

 

    vector<string> input(char c) {

        // write code to return the top 3 suggestions when the current character in the stream is c

        // c == '#' means , the current query is complete and you may save the entire query into

        // historical data

       

        if(c == '#') {

            int cnt = getCnt(out);

            if(cnt == 0) add(out, 1);

            else

                erase_nd_update(out, cnt);

            out = "";

            return {};

        }

       

        node* t = root;

        out += c;

       

        for(int i = 0; i < out.size(); i++) {

            if(out[i] == ' ') {

                if(!t->links[26]) return {};

                t = t->links[26];

                continue;

            }

            if(!t->links[out[i] - 'a']) return {};

            t = t->links[out[i] - 'a'];

        }

       

        vector<string> dummy;

        int k = 3;

        for(auto x : t->st) {

            dummy.push_back(x.first);

            k--;

            if(k == 0) break;

        }

        return dummy;
    }};

//{ Driver Code Starts.

int main() {

    int t;
	cin >> t;
    cin.ignore();
    while(t--) {
		int n;
		cin>>n;
        cin.ignore();
        vector<string> sentences(n);
		vector<int> times(n);
		for (int i = 0; i < n; ++i){
            
			getline(cin,sentences[i]);
			cin>>times[i];
            cin.ignore();
		}
		AutoCompleteSystem *obj = new AutoCompleteSystem(sentences,times);
		int q;
		cin>>q;
        cin.ignore();

		for (int i = 0; i < q; ++i){
			string query;
			getline(cin,query);
            string qq = "";
            for(auto &x:query){
			    qq+=x;
                vector<string> suggestions = obj->input(x);
                if(x=='#')
                    continue;
                cout<<"Typed : \""<<qq<<"\" , Suggestions: \n";
				for(auto &y:suggestions){
					cout<<y<<"\n";
				}
			}
		}
	}
	return 0;
}




// } Driver Code Ends