#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>

using namespace std;


int solve(vector<int> num)
{
    int o_sum = 0;
    int save = 0;
    for (int i = 0; i < num.size()-1; i++)
        o_sum += abs(num[i] - num[i + 1]);
    
    for (int i = 1; i < num.size() - 1; i++)
    {
        int o = abs(num[i] - num[i - 1]) + abs(num[i + 1] - num[i]);
        int s = abs(num[i + 1] - num[i - 1]);

        if ((o - s) > save)
            save = o - s;
    }
    return o_sum - save;
}


int main(int argc, char** argv)
{
    int T;
    cin >> T;
    vector<int> result(T);

    for (int i = 0; i < T; i++)
    {
        int N;
        cin >> N;
        vector<int> num(N);
        
        for (int j = 0; j < N; j++)
            cin >> num[j];

        result[i] = solve(num);
    }

    for(int i : result)
        cout << i << endl;
    

}