#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;


int calc(vector<vector<char>> num, int H, int W)
{
    int count = 0;

    if (W == 1 && H == 1)
    {
        switch (num[0][0])
        {
            case '.':
                return 0;

            case '#':
                return 1;

        }
    }

    // 행 검사
    
    for (int i = 0; i < H; i++)
    {
        if (std::find(num[i].begin(), num[i].end(),'.') == num[i].end())
        {
            count ++;
        }
    }
    
    
    // 열 검사
    
    for (int i = 0; i < W; i++)
    {
        int colCount = 0;
        for (int j = 0; j < H; j++)
        {
            if (num[j][i] == '.')
                break;
            colCount++;
        }
        if (colCount == H)
            count++;
    }
    


    
    if ((H + W) == count)
        return min(H,W);

    return count;
}

int main(int argc, char** argv)
{
    int T;
    cin >> T;
    vector<int> result(T);
    for (int t = 0; t < T; t++)
    {
        int H,W =0;
        cin >> H >> W;

        vector<vector<char>> num(H, vector<char>(W,'.'));

        for (int i = 0; i < H; i++)
        {
            for (int j = 0; j < W; j++)
            {
                cin >> num[i][j];
            }            
        }
        result[t] = calc(num,H,W);
    }

    for (int i = 0; i < T; i++)
        cout << result[i] << endl;

}