#include <iostream>
#include <vector>
#include <string>
#include <queue>
#include <algorithm>
using namespace std;

int bfs(int x, int y,int N,vector<string> &num,vector<vector<bool>> &visited)
{
    queue<pair<int,int>> q;
    int cnt = 1;
    q.push({x,y});
    visited[x][y] = true;


    while(!q.empty())
    {
        pair<int, int> cur = q.front();
        int cx = cur.first;
        int cy = cur.second;
        q.pop();
        
        if(cx > 0 && num[cx-1][cy] == '1' && !visited[cx-1][cy])
            {
                visited[cx-1][cy] = true;
                cnt++;
                q.push({cx-1,cy});
            }
        if(cx < N-1 && num[cx+1][cy] == '1' && !visited[cx+1][cy])
            {
                visited[cx+1][cy] = true;
                cnt++;
                q.push({cx+1,cy});
            }
        if(cy > 0 && num[cx][cy-1] == '1' && !visited[cx][cy-1])
            {
                visited[cx][cy-1] = true;
                cnt++;
                q.push({cx,cy-1});
            }
        if(cy < N-1 && num[cx][cy+1] == '1' && !visited[cx][cy+1])
            {
                visited[cx][cy+1] = true;
                cnt++;
                q.push({cx,cy+1});
            }
    }
    return cnt;
}


int main(int argc, char** argv)
{
    int N;
    cin >> N;
    vector<string> num(N);
    vector<vector<bool>> visited(N,(vector<bool>(N,false)));
    vector<int> result;
    int cnt = 0;

    for (int i = 0; i < N; i++)
    {        
        cin >> num[i];
    }

    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
        {
            if(num[i][j] == '1' && !visited[i][j])
            {
                result.push_back(bfs(i,j,N,num,visited));
                cnt ++;
            }
        }
    }
    
    sort(result.begin(), result.end());
    cout << cnt << endl;
    for(int i : result)
        cout << i << endl;
}

