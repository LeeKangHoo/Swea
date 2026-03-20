#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int calc(int A, int P)
{
    int sum = 0;

    while ( A > 0)
    {
        int tmp = 1;
        for ( int i = 0; i < P; i++)
            tmp *= A % 10;
        sum += tmp;
        A /= 10;
    }
    return sum;
}

int dfs(int A, int P,vector<int> &visited)
{
    while(true)
    {
        
        if(find(visited.begin(),visited.end(),A) != visited.end())
        {
            return find(visited.begin(),visited.end(),A) - visited.begin();
        }
        visited.push_back(A);
        A = calc(A,P);
    }
}


int main()
{
    int A,P;
    cin >> A >> P;
    vector<int> visited;
    
    cout << dfs(A,P,visited) << endl;
}