#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
//42
using namespace std;

string solve(int N, int M,int Q, vector<string> &n, vector<string> &m,vector<int> &q)
{
    string r;

    // int test = max(N,M);
    // int max_val = max(N,M);
    // int min_val = min(N,M);
    // int tmp = min_val*(max_val - min_val);


    for (int i = 0; i < Q; i++)
    {
        r += n[(q[i]-1) % N] + m[(q[i]-1) % M] + " ";
    }

    return r;
}


int main()
{
    int T;
    cin >> T;

    vector<string> result(T,"0");
    
    

    for(int i = 0; i < T; i++)
    {
        int N,M;
        cin >> N >> M;

        vector<string> n(N);
        vector<string> m(M);
        
        for(int j = 0; j < N; j++)
            cin >> n[j];
        for(int z = 0; z < M; z++)
            cin >> m[z];

        int Q;
        cin >> Q;
        vector<int> q(Q);
        for(int a = 0; a < Q; a++)
            cin >> q[a];
        result[i] = solve(N,M,Q,n,m,q);
    }
    for (int i = 0; i < T; i++)
        cout << "#" << i+1 << " " << result[i] << endl;
}