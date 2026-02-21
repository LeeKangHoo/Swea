#include <iostream>
#include <vector>
//26
using namespace std;

int dfs(int start, int a, int b, vector<vector<int>> &graph, vector<bool> &visited,int cnt)
{
    if (start == b)
        return cnt;
    visited[start] = true;

    for (int i : graph[start])
    {
        if(!visited[i])
        {
            int result = dfs(i,a,b,graph,visited,cnt+1);
            if(result != -1)
                return result; 
        }
    }


    return -1;
}


int main()
{
    int n; cin >> n;
    int a, b; cin >> a >> b;
    int m; cin >> m;

    vector<vector<int>> graph(n+1);
    vector<bool> visited(n+1);
    int cnt = 0;
    

    for (int i = 1; i <= m; i++)
    {
        int v1,v2;
        cin >> v1 >> v2;
        graph[v1].push_back(v2);
        graph[v2].push_back(v1);  
    }
    cout << dfs(a,a,b,graph,visited,cnt) << endl;
}