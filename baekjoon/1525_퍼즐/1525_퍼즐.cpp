#include <iostream>
#include <vector>
#include <queue>
#include <tuple>
#include <map>
#include <string>
#include <algorithm>

using namespace std;

int bfs(vector<string> mapp)
{
    queue<pair<vector<string>, pair<int, int>>> q;
    map<vector<string>, int> dist;
    int start_x, start_y;
    for(int i = 0; i < 3; i++)
    {
        if(mapp[i].find('0') != string::npos)
        {
            start_x = i;
            start_y = mapp[i].find('0');
        }
    }
    q.push({mapp, {start_x, start_y}});
    dist[mapp] = 0;
    vector<string> answer = {"123", "456", "780"};

    int dx[] = {-1,0,1,0};
    int dy[] = {0,1,0,-1};

    while(!q.empty())
    {
        vector<string> cur_map = q.front().first;
        int cx = q.front().second.first;
        int cy = q.front().second.second;
        int d = dist[cur_map];
        q.pop();

        if(cur_map == answer)
            return dist[cur_map];

        for(int i = 0; i < 4; i++)
        {
            int nx = cx+dx[i];
            int ny = cy+dy[i];
            if(nx >= 0 && nx < 3 && ny >= 0 && ny < 3)
            {
                vector<string> next_map = cur_map;
                swap(next_map[cx][cy], next_map[nx][ny]);
                if(dist.find(next_map) == dist.end())
                {
                    q.push({next_map, {nx,ny}});
                    dist[next_map] = d + 1;
                }
            }
        }
    }
    return -1;
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    vector<string> mapp(3, "");
    int temp;

    for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < 3; j++)
        {
            cin >> temp;
            mapp[i] += to_string(temp);
        }
    }

    cout << bfs(mapp) << endl;
}