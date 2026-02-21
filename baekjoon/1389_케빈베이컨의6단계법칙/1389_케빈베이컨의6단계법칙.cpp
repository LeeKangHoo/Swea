#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
//1:1
using namespace std;


int solve(int N, int M, vector<vector<int>> &graph, int cnt)
{
    vector<int> r(N+1);
    for (int j = 1; j <= N; j++)
    {
        int tmp = 0;
        for (int i = 1; i <= N; i++)
        {
            queue<int> q;
            vector<int> visited(N+1);
            q.push(j);
            if(i == j)
                continue;

            while(!q.empty())
            {
                int cur = q.front();
                q.pop();

                if(cur == i && visited[cur] != 0)
                    break;

                for (int next : graph[cur])
                {
                    if(visited[next] == 0)
                    {
                        visited[next] = visited[cur] + 1;
                        q.push(next);
                    } 
                }
            }
            tmp += visited[i];
        }
        r[j] = tmp;
    }
    r[0] = *max_element(r.begin(),r.end()) + 1;
    return min_element(r.begin(),r.end()) - r.begin();

}


int main()
{
    int N,M; cin >> N >> M;
    vector<vector<int>> graph(N+1);
    int cnt = 0;

    for (int i = 1; i <= M; i++)
    {
        int v1,v2; cin >> v1 >> v2;
        graph[v1].push_back(v2);
        graph[v2].push_back(v1);
    }

    cout << solve(N,M,graph,cnt) <<endl;


}