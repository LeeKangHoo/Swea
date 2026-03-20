#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
#include <tuple>

using namespace std;

int dfs(int x, int y,int R, int C, vector<vector<char>> &mapp, vector<char> &visited,int cnt, int &max_val)
{
    max_val = max(cnt,max_val);

    int dx[] = {1,0,-1,0};
    int dy[] = {0,1,0,-1};

    for(int i = 0; i < 4; i++)
    {
        int nx = x+dx[i];
        int ny = y+dy[i];
        
        if(0 <= nx && nx < R && 0 <= ny && ny < C)
        {
            if(find(visited.begin(),visited.end(), mapp[nx][ny]) == visited.end())
            {
                visited.push_back(mapp[nx][ny]);
                
                dfs(nx,ny,R,C,mapp,visited,cnt+1,max_val);
                visited.pop_back();
            }
        }
        
    }
    return 0;

}

int main()
{
    int R,C;
    cin >> R >> C;
    vector<vector<char>> mapp(R,vector<char>(C,'0'));

    vector<char> visited;
    int max_val = 0;


    for (int i = 0; i < R; i++)
    {
        for (int j = 0; j < C; j++)
        {
            cin >> mapp[i][j];
        }
    }
    visited.push_back(mapp[0][0]);
    dfs(0,0,R,C,mapp,visited,1,max_val);
    cout << max_val << endl;
}