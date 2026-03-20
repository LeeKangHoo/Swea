#include <iostream>
#include <vector>
#include <queue>

using namespace std;

int bfs(int N, vector<vector<int>> &num, vector<bool> &visited)
{
    queue<int> q;
    q.push(N);
    int cnt = 0;

    visited[N] = true;

    while(!q.empty())
    {
        int cur = q.front();
        q.pop();

        for(int i: num[cur])
        {
            if(!visited[i])
            {
                q.push(i);
                visited[i] = true;
                cnt++;
            }
        }
    }
    return cnt;

}


int main()
{
    int N,M;
    cin >> N >> M;
    vector<vector<int>> num(N+1);
    vector<bool> visited(N+1,false);


    for (int i = 0; i < M; i++)
    {
        int tmp1, tmp2;
        cin >> tmp1 >> tmp2;
        num[tmp1].push_back(tmp2);
        num[tmp2].push_back(tmp1);
    }

    cout << bfs(1,num,visited) << endl;
}