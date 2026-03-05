//34
#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

float solve(float a, float b, float c)
{
    float tmp = (a+c)/2;
    float r = abs(b - tmp);
    return r;
}



int main()
{
    int T;
    cin >> T;

    for(int i = 0; i < T; i++)
    {
        float a,b,c;
        cin >> a >> b >> c;
        // cout << "#" << i+1 << " "  << solve(a,b,c) << endl; 
        printf("#%d %.1f\n", i + 1, solve(a,b,c));
    }
}