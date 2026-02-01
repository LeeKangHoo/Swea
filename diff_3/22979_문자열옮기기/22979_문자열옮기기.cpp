#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <cmath>
//26:11
using namespace std;


string solve(string s, int K, int* num)
{
    for (int i = 0; i < K; i++)
    {
        int step = abs(num[i]) % s.length();
        if (num[i] > 0)
        {
            rotate(s.begin(), s.begin() + step, s.end());
        }
        else if(num[i] < 0)
        {
            rotate(s.rbegin(), s.rbegin() + step, s.rend());
        }
        else 
        {
            continue;
        }
    }
    return s;
}

int main(int argc,char** argv)
{
    int T;
    cin >> T;
    vector<string> result(T);
    
    for (int i = 0; i < T; i++)
    {
        string S;
        cin >> S;
        int K = 0;
        cin >> K;
        int num[K];
    
        for (int j = 0; j < K;j++ ) 
            cin >> num[j];

        result[i] = solve(S,K,num);
    }

    for (string i : result)
        cout << i << endl;
}