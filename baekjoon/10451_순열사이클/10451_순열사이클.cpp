#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

void dfs(int cur,const vector<vector<int>> &graph, vector<bool> &visited,int &cnt)
{
    visited[cur] = true;
    

    for (int next : graph[cur])
    {
        if(!visited[next])
        {
            dfs(next,graph,visited,cnt);
        }
        
        
    }

}

int main()
{
    int T;
    cin >> T;
    vector<int> result(T);
    
    
    for (int i = 0; i < T; i++)
    {
        int N;
        int cnt = 0;
        cin >> N;
        vector<vector<int>> graph(N+1);
        vector<bool> visited(N+1);
        vector<int> num(N+1);
        int tmp = 0;
        for (int j = 1; j <= N; j++)
        {
            cin >> tmp;
            graph[j].push_back(tmp);
        }
            

        // sort(num.begin(),num.end(),num);
        // for (int x = 1; x <= N; x++)
        //     graph[x] = num[x]
        for (int z = 1; z <= N; z++)
        {
            if(!visited[z])
            {
                dfs(z,graph,visited,cnt);
                cnt++;
            }
            
        }

        
        result[i] = cnt;
    }
    for (int i : result)
        cout << i << endl;
}