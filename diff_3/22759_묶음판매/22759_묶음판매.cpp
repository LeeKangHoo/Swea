#include <iostream>
#include <vector>
#include <string>


using namespace std;

string solve(int L, int R)
{
    if (2 * L >= R + 1)
        return "yes";
    return "no";
}

int main()
{
    int T;
    cin >> T;
    vector<string> result(T);

    for (int i = 0; i < T; i++)
    {
        int L,R;
        cin >> L >> R;

        result[i] = solve(L,R);
    }

    for (string i : result)
        cout << i << endl;
}