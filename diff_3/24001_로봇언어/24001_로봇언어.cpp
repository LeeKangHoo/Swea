#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
// 20
using namespace std;;

int solve(string N)
{
    
    int max_val = 0;
    int cnt = 0;

    for(int i = 0; i < N.size(); i++)
    {
        if(N[i] == 'L')
        {
            cnt += -1;
        }
        else if(N[i] == 'R')
        {
            cnt += 1;
        }
        else
        {
            cnt += -1;
        }
        if (abs(cnt) > max_val)
            max_val = abs(cnt);
    }
    cnt = 0;
    for(int i = 0; i < N.size(); i++) 
    {
        if(N[i] == 'L')
        {
            cnt += -1;
        }
        else if(N[i] == 'R')
        {
            cnt += 1;
        }
        else
        {
            cnt += 1;
        }
        if (abs(cnt) > max_val)
            max_val = abs(cnt);
    }
    return max_val;
}

int main(int argc, char** argv)
{
    int T;
    cin >> T;
    vector<int> result(T);

    for (int i = 0; i < T; i++)
    {
        string N;
        cin >> N;
        result[i] = solve(N);
    }
    for (int i : result)
        cout << i << endl;
}