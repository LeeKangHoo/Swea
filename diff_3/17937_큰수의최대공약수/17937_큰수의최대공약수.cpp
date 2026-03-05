//28
#include <iostream>
#include <vector>
#include <string>

using namespace std;

string solve(string A, string B)
{
    // long long cur_val;
    // if (A > B) cur_val = A;
    // else if (A < B) cur_val = B;
    // else return A;

    // while (cur_val != 1)
    // {
    //     if (A % cur_val == 0 && B & cur_val == 0) return cur_val;
        
    //     if (cur_val % 2 == 0) 
    //         cur_val /= 2;
    //     else
    //         cur_val /= 3;
    // }
    // return 1;
    if (A == B)
    {
        return A;
    }
    else
    {
        return "1";
    }
}

int main()
{
    int T;
    cin >> T;
    vector<string> result(T);
    for (int i = 0; i < T; i++)
    {
        string A,B;
        cin >> A >> B;
        result[i] = solve(A,B);
    }
    for (int i = 0;i < T; i++)
        cout << "#" << i+1 << " " << result[i] << endl;
}