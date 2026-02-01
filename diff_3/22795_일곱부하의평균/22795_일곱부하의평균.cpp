#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;


int solve(vector<int> num)
{
    int n = 1;
    int sum;
    int max_val = *max_element(num.begin(), num.end());
    for (int i = 0; i < 6; i++)
        sum += i;
    while(true)
    {
        double tmp = (sum + (max_val + n))/ 7;
        if (tmp == (int)tmp)
            return max_val + n;
        n++;
    }
    return 0;
}

int main(int argc, char** argv)
{
    int T;
    cin >> T;
    vector<int> result(T);

    for (int i = 0; i < T; i++)
    {
        vector<int> cm(6);
        for (int j = 0; j < 6; j++)
            cin >> cm[j];
        result[i] = solve(cm);
    }

    for (int i : result)
        cout << i << endl;
}