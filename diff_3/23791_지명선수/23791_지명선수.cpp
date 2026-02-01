#include <iostream>
#include <vector>
#include <string>
//47:32
using namespace std;

string solve(vector<int> A, vector<int> B)
{
    string r(A.size(), '0');

    for (int i = 0; i < A.size(); i++)
    {
        for (int j = 0; j < A.size(); j++)
        {
            if(r[A[j] - 1] == '0')
            {
                r[A[j] - 1] = 'A';
                break;
            }
        }
        
        for (int z = 0; z < B.size(); z++)
        {
            if(r[B[z] - 1] == '0')
            {
                r[B[z] - 1] = 'B';
                break;
            }
        }
        
        
    }
    
    return r;
}



int main(int argc, char** argv)
{
    int T;
    cin >> T;
    vector<string> result(T);

    for (int i = 0;i < T; i++)
    {   
        int N;
        cin >> N;

        vector<int> A(N);
        vector<int> B(N);

        for (int j = 0; j < N; j++)
            cin >> A[j];
        for (int z = 0; z <N; z++)
            cin >> B[z];

        result[i] = solve(A,B);
    }

    for (string i: result)
        cout << i << endl;



    return 0;
}