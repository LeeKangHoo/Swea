#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
//29
using namespace std;

void bfs(int n, vector<vector<int>> &num, vector<bool> &visited)
{
    queue<int> q;
    q.push(n);
    visited[n] = true;

    while(!q.empty())
    {
        int cur = q.front();
        q.pop();

        for (int i : num[cur])
        {
            if(!visited[i])
            {
                q.push(i);
                visited[i] = true;
            }
        }
    }
    return;
}

int main()
{
    int N,M;
    int cnt = 0;
    cin >> N >> M;
    vector<vector<int>> num(N+1);
    vector<bool> visited(N+1, false);

    for (int i = 0; i < M; i++)
    {
        int u,v;
        cin >> u >> v;
        num[u].push_back(v);
        num[v].push_back(u);
    }

    for(int i = 1; i <= N; i++)
    {
        if(!visited[i])
        {
            bfs(i,num, visited);
            cnt++;
        }
    }
    cout << cnt << endl;
}