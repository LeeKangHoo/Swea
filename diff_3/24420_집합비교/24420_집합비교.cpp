#include <iostream>
#include <vector>
#include <algorithm>
//19:52
using namespace std;

char solve(vector<int> A, vector<int> B)
{
    if(A.size() == B.size())
    {
        for (int i = 0; i < A.size(); i++)
        {
            if(find(B.begin(), B.end(), A[i]) == B.end())
                return '?';
        }
        return '=';
    }
    
    if ( A.size() > B.size())
    {
        for (int i = 0; i < B.size(); i++)
        {
            if(find(A.begin(), A.end(), B[i]) == A.end())
            return '?';
        }
        return '>';
    }
    
    if ( A.size() < B.size())
    {
        for (int i = 0; i < A.size(); i++)
        {
            if(find(B.begin(), B.end(), A[i]) == B.end())
            return '?';
        }
        return '<';
    }
    return '?';
}


int main(int argc, char** argv)
{
    int T; 
    cin >> T;
    vector<char> result(T);
    

    for (int i = 0; i < T; i++)
    {

        int N,M = 0;
        cin >> N >> M;
        vector<int> A(N);
        vector<int> B(M);

        for (int j = 0; j < N; j++)
            cin >> A[j];
        for (int z = 0; z < M; z++)
            cin >> B[z];

        result[i] = solve(A,B);
    }

    for (char i : result)
        cout << i << endl;
}