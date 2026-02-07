#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

void dfs(int start, int cur, int cnt, int sum, int N, vector<vector<int>> &cost, vector<bool> &visited,vector<int> &result)
{
    if (cnt == N) {
        if (cost[cur][start] != 0) {
            result.push_back(sum + cost[cur][start]);
        }
        return;
    }

    for (int next = 0; next < N; next++) {
        if (!visited[next] && cost[cur][next] != 0) {
            visited[next] = true;
            dfs(start, next, cnt + 1, sum + cost[cur][next], N, cost, visited, result);
            visited[next] = false;
        }
    }
}

int main()
{
    int N;
    if (!(cin >> N)) return 0;

    vector<vector<int>> cost(N, vector<int>(N, 0));
    vector<int> result;
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++)
            cin >> cost[i][j];
    }

    
    vector<bool> visited(N,false);
    visited[0] = true;
    dfs(0,0,1,0,N,cost,visited,result);

    cout << *min_element(result.begin(), result.end()) << endl;

    return 0;
}