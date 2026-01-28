#include <iostream>
#include <vector>
#include <algorithm>


using namespace std;

vector<int> calc(vector<int> num)
{
    int max = *max_element(num.begin(), num.end());
    int min = *min_element(num.begin(), num.end());
    if (count(num.begin(), num.end(), max) > 1)
    {
        if (num[0] == num[1])
        {
            num[0] = min;
            num[1] = max;
            num[2] = min;
        }
        else if(num[1] == num[2])
        {
            num[0] = min;
            num[1] = min;
            num[2] = max;
        }
        else
        {
            num[0] = max;
            num[1] = min;
            num[2] = min;
        }
    }
    else
    {
        for (int j = 0; j < 3; j++)
        num[j] = -1;
    }

    return num;
}


int main(int argc, char** argv)
{
    int T;
    cin >> T;

    vector<vector<int>> result(T);

    for ( int i = 0; i < T; i++)
    {
        vector<int> num(3,0);
        for (int j = 0; j < 3 ; j++)
        {
            cin >> num[j];
        }
        result[i] = calc(num);
    }

    for (int i = 0; i < T ; i++)
    {
        cout << result[i][0] << " " << result[i][1] << " " << result[i][2] << endl;
    }
    
}