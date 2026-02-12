#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
#include <tuple>

using namespace std;

int bfs(int N, int M, vector<vector<int>> &map)
{
    queue<tuple<int, int, int>> q;
    int cnt = 0;

    for(int i = 0; i < N; i++)
    {
        for(int j = 0; j < M; j++)
        {
            if(map[i][j] == 1)
                q.push({i,j,0});
        }
    }

    int dx[] = {-1,0,1,0};
    int dy[] = {0,1,0,-1};
    int max_val = 0;

    while(!q.empty())
    {
        tuple<int, int, int> cur = q.front();
        q.pop();
        int cx = get<0>(cur);
        int cy = get<1>(cur);
        int day = get<2>(cur);


        for (int i = 0; i < 4; i++)
        {
            if(cx + dx[i] >= 0 && cx + dx[i] <= N-1 && cy + dy[i] >= 0 && cy + dy[i] <= M-1)
            {
                if(map[cx+dx[i]][cy+dy[i]] == 0)
                {
                    map[cx+dx[i]][cy+dy[i]] = 1;
                    q.push({cx+dx[i], cy+dy[i], day+1});
                    max_val = max(day+1, max_val);
                }
            }
        }
    }

    for(int i = 0; i < N; i++)
    {
        if(find(map[i].begin(),map[i].end(), 0) != map[i].end())
            return -1;
    }

    return max_val;
}

int main()
{
    int N,M;
    cin >> M >> N;
    vector<vector<int>> map(N,(vector<int>(M,0)));


    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < M; j++)
            cin >> map[i][j];
    }

    cout << bfs(N,M,map) << endl;
}