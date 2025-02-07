#include <iostream>
#include <vector>
#include <string>
#include <cmath>

using namespace std;


string solve(long long S, long long P)
{
    for (long long i = 1; i * i <= P; i++)
    {
        if(P % i == 0)
        {
            long long N = i;
            long long M = P/i;

            if(N + M == S)
            {
                return "Yes";
            }
        }
    }
    return "No";

}

int main()
{
    int TC;
    cin >> TC;
    vector<string> result(TC);

    for (int i = 0; i < TC; i++)
    {
        long long S,P;
        cin >> S >> P;
        
        result[i] = solve(S,P);
    }
    for (string i : result)
        cout << i << endl;
}