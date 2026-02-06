#include <iostream>
#include <queue>
#include <vector>
#include <string>

using namespace std;

int bfs(vector<string> graph,vector<vector<int>> visited, int end_n, int end_m)
{
    queue<pair<int,int>> q;
    q.push({1,1});
    visited[1][1] = 1;

    while(!q.empty())
    {
        pair<int,int> cur = q.front();
        q.pop();
        

        int x = cur.second;
        int y = cur.first;
        
        if ( x == end_m && y == end_n)
            return visited[y][x];
    


        if(1 <= y - 1 && graph[y-1][x-1] == '1' && visited[y-1][x] == 0)
        {
            q.push({y-1,x});
            visited[y-1][x] = visited[y][x] + 1;
        }
        if(end_n >= y + 1 && graph[y+1][x-1] == '1' && visited[y+1][x] == 0)
        {
            q.push({y+1,x});
            visited[y+1][x] = visited[y][x] + 1;
        }
        if(1 <= x - 1 && graph[y][x - 2] == '1' && visited[y][x-1] == 0)
        {
            q.push({y,x-1});
            visited[y][x-1] = visited[y][x] + 1;
        }
        if(end_m >= x + 1 && graph[y][x] == '1' && visited[y][x+1] == 0)
        {
            q.push({y,x+1});
            visited[y][x+1] = visited[y][x] + 1;
        }
    }
    
    return -1;

}

int main()
{
    int N, M;
    std::cin >> N >> M;
    std::vector<string> graph(N+1);
    std::vector<vector<int>> visited(N+1,vector<int>(M+1,0));
    
    for (int i = 1; i <= N; i++)
    {
        std::cin >> graph[i];
    }

    std::cout << bfs(graph,visited,N,M) << endl;
    return 0;
}