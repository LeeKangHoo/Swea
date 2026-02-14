#include <iostream>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;

int solve(int K, string num)
{
    while(K > 0)
    {
        if(num == "o..")
        {
            num = ".o.";
            K--;
            continue;
        }
        if(num == ".o.")
        {
            num = "o..";
            K--;
            continue;
        }
            
        if(num == "..o")
        {
            num = ".o.";
            K--;
            continue;
        }
    }
    for(int i = 0; i < 3; i++)
    {
        if (num[i] == 'o')
            return i;
    }
    return -1;
}

int main()
{
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);
    int T;
    cin >> T;
    vector<int> result(T);
    string num;

    for (int i = 0; i < T; i++)
    {
        int K;
        cin >> num >> K;
        result[i] = solve(K,num);
    }


    for (int i = 0; i < T; i++)
        cout << "#" << i+1 << " " << result[i] << endl; 
}