#include <iostream>
#include <string>
#include <vector>
#include <algorithm>


using namespace std;

string solve(string S, string E)
{
    while(S.length() != E.length())
    {
        if(E[E.length()-1] == 'X')
        {
            E.pop_back();
            continue;
        }
            
        if(E[E.length()-1] == 'Y')
        {
            E.pop_back();
            reverse(E.begin(),E.end());
            continue;
        }
    }

    if(S == E)
        return "Yes";
    else
        return "No";

}

int main()
{
    int T;
    cin >> T;
    vector<string> result(T);

    for (int i = 0; i < T; i++)
    {
        string v1,v2;
        cin >> v1 >> v2;

        result[i] = solve(v1,v2);
    }

    for (int i = 0; i < T; i++)
        cout << "#" << i+1 << " "<< result[i] << endl;
}