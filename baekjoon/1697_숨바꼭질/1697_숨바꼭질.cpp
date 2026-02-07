#include <iostream>
#include <vector>
#include <queue>

using namespace std;
//48
int bfs(int N, int K,vector<int> &visited)
{
    queue<int> q;
    q.push(N);
    
    while(!q.empty())
    {
        int cur = q.front();
        q.pop();
        if (cur == K)
            return visited[cur];
        if(cur <= K && visited[cur+1] == 0)
        {
            q.push(cur+1);
            visited[cur+1] += visited[cur] + 1;
        }
        if(cur > 0 &&visited[cur-1] == 0)
        {
            q.push(cur-1);
            visited[cur-1] += visited[cur] + 1;
        }
    
        if(cur <= K && visited[cur*2] == 0)
        {
            q.push(cur*2);
            visited[cur*2] += visited[cur] + 1;
        }
    }
    return -1;
}

int main()
{
    int N, K;
    cin >> N >> K;
    vector<int> coord(200001,0);
    vector<int> visited(200001,0);
    

    cout << bfs(N,K,visited) << endl;

}