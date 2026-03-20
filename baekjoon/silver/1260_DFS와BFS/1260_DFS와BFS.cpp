#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;;

void DFS(int cur, vector<vector<int>> graph, vector<bool> &visited)
{
    visited[cur] = true;
    cout << cur << " ";

    for (int next : graph[cur])
    {
        if(!visited[next])
        {
            DFS(next, graph, visited);
        }
    }
}

void BFS(int start, vector<vector<int>> graph, vector<bool> visited)
{
    queue<int> q;

    q.push(start);
    visited[start] = true;
    cout << start << " ";

    while(!q.empty())
    {
        int cur = q.front();
        q.pop();

        for(int next : graph[cur])
        {
            if(!visited[next])
                {
                    cout << next << " ";
                    visited[next] = true;
                    q.push(next);
                }
        }
    }
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int N,M,V = 0;
    cin >> N >> M >> V;
    vector<vector<int>> graph(N+1);
    vector<bool> visited_D(N+1,false);
    vector<bool> visited_B(N+1,false);


    for (int i = 1; i <= M; i++)
    {
        int v1,v2;
        cin >> v1 >> v2;
        graph[v1].push_back(v2);
        graph[v2].push_back(v1);
    }

    for(int i = 1; i <= N; i++)
        sort(graph[i].begin(), graph[i].end());



    
    DFS(V, graph, visited_D);
    cout << endl;
    BFS(V, graph, visited_B);
    cout << endl;
    

    

    return 0;
}