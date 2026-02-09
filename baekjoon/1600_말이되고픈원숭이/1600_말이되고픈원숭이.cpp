#include <iostream>
#include <vector>
#include <queue>
#include <tuple>

using namespace std;


int bfs(int K, int W, int H, vector<vector<int>> &map) {
    queue<tuple<int, int, int>> q;
    q.push({0, 0, K});

    vector<vector<vector<int>>> visited(H, vector<vector<int>>(W, vector<int>(K + 1, 0)));
    visited[0][0][K] = 1;

    const int h_dx[] = {-2, -2, -1, -1, 1, 1, 2, 2};
    const int h_dy[] = {-1, 1, -2, 2, -2, 2, -1, 1};
    const int dx[] = {0, 0, 1, -1};
    const int dy[] = {1, -1, 0, 0};

    while (!q.empty()) {
        auto [cx, cy, ck] = q.front();
        q.pop();

        if (cx == H - 1 && cy == W - 1) {
            return visited[cx][cy][ck] - 1;
        }

        if (ck > 0) {
            for (int i = 0; i < 8; i++) {
                int nx = cx + h_dx[i];
                int ny = cy + h_dy[i];

                if (nx >= 0 && nx < H && ny >= 0 && ny < W) {
                    if (map[nx][ny] == 0 && visited[nx][ny][ck - 1] == 0) {
                        visited[nx][ny][ck - 1] = visited[cx][cy][ck] + 1;
                        q.push({nx, ny, ck - 1});
                    }
                }
            }
        }

        for (int i = 0; i < 4; i++) {
            int nx = cx + dx[i];
            int ny = cy + dy[i];

            if (nx >= 0 && nx < H && ny >= 0 && ny < W) {
                if (map[nx][ny] == 0 && visited[nx][ny][ck] == 0) {
                    visited[nx][ny][ck] = visited[cx][cy][ck] + 1;
                    q.push({nx, ny, ck});
                }
            }
        }
    }

    return -1;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int K, W, H;
    cin >> K >> W >> H;

    vector<vector<int>> map(H, vector<int>(W));

    for (int i = 0; i < H; i++) {
        for (int j = 0; j < W; j++) {
            cin >> map[i][j];
        }
    }

    cout << bfs(K, W, H, map) << endl;

    return 0;
}