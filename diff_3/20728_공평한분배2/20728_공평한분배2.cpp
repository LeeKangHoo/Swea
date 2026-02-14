#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int solve(vector<int> pocket, int K)
{
    sort(pocket.begin(), pocket.end());
    int min_val = pocket[pocket.size()-1];
    int tmp = 0;
    for (int i = 0; i <= pocket.size()-K; i++)
    {
        tmp = pocket[i+K-1] - pocket[i];

        if(tmp < min_val)
            min_val = tmp;
    }


    return min_val;
    
}


int main()
{
    int T;
    cin >> T;
    vector<int> result(T);


    for (int i = 0; i < T; i++)
    {
        int N,K;
        cin >> N >> K;

        vector<int> pocket(N);
        for (int j = 0; j < N; j++)
            cin >> pocket[j];

        result[i] = solve(pocket,K);
    }


    for (int i = 0; i < T; i++)
        cout << "#" << i+1 << " " << result[i] << endl;
}