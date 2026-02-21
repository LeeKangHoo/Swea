#include <iostream>
#include <vector>
#include <algorithm>
//47
using namespace std;

vector<long long> solve(int N, vector<long long> num)
{
    vector<long long> r;
    for(int i = 0; i < N*2; i++)
    {
        if(num[i] == -1) continue;

        
        long long tmp = (num[i] * 4)/3;
        auto it = find(num.begin(),num.end(),tmp);
        if(it != num.end())
        {
            r.push_back(num[i]);
            *it = -1;
        }
    }
    return r;
}


int main()
{
    int TC;
    cin >> TC;
    
    vector<vector<long long>> result(TC);

    for (int i = 0; i < TC; i++)
    {
        int N;
        cin >> N;
        vector<long long> num(N*2);
        for (int j = 0; j < N*2; j++)
            cin >> num[j];
        result[i] = solve(N,num);
    }

    for (int i = 0; i < TC; i++)
    {
        cout << "#" << i+1 << " ";
        for(int j = 0; j < result[i].size(); j++)
        {
            cout << result[i][j] << " ";
        }
        cout << endl;
            
    }
}