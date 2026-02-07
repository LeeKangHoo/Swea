#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
//57
using namespace std;

void bfs(int x, int y, vector<vector<int>> &num, vector<vector<bool>> &visited,int rain)
{
    queue<pair<int,int>> q;
    q.push({x,y});
    visited[x][y] = true;
    int N = num.size();

    while(!q.empty())
        {
            pair<int, int> cur = q.front();
            q.pop();
            int cx = cur.first;
            int cy = cur.second;

            
            if( 0 < cx && num[cx -1][cy] - rain > 0 && !visited[cx-1][cy])
            {
                visited[cx-1][cy] = true;
                q.push({cx-1,cy});
            }
                
            if( N-1 > cx && num[cx + 1][cy] - rain > 0 && !visited[cx+1][cy])
            {
                visited[cx+1][cy] = true;
                q.push({cx+1,cy});
            }

            if( 0 < cy && num[cx][cy-1] - rain > 0 && !visited[cx][cy-1])
            {
                visited[cx][cy-1] = true;
                q.push({cx,cy-1});
            }

            if( N-1 > cy && num[cx][cy+1] - rain > 0 && !visited[cx][cy+1])
            {
                visited[cx][cy+1] = true;
                q.push({cx,cy+1});
            }
        }
    
    
    return;

}

int main()
{
    int N;
    
    cin >> N;

    vector<vector<int>> num(N,vector<int>(N,0));
    vector<int> result;
    result.push_back(0);

    for (int i = 0; i < N; i++)
    {
        for( int j = 0; j < N; j++)
            cin >> num[i][j];
    }


    int rain = 0;
    for ( int i = 0; i < N; i++)
    {
        if(*max_element(num[i].begin(), num[i].end()) > rain)
            rain = *max_element(num[i].begin(), num[i].end());
    }

    for (int r = 0; r < rain; r++)
    {
        vector<vector<bool>> visited(N,vector<bool>(N,false));
        int cnt = 0;
        for (int i = 0; i < N; i++)
        {
            for(int j = 0; j < N; j++)
            {
               if (!visited[i][j] && num[i][j] - r> 0)
               {
                bfs(i,j,num,visited,r);
                cnt++;
               }
            }
        }
        result.push_back(cnt);
    }
    

    cout << *max_element(result.begin(),result.end()) << endl;
}