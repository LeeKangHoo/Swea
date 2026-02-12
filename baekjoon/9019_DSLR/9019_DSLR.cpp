#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <queue>
#include <tuple>

using namespace std;

std::string bfs(int A, int B)
{
    queue<pair<int, string>> q;
    bool visited[10000] = {false, };
    q.push({A, ""});
    visited[A] = true;

    while(!q.empty())
    {
        pair<int, string> cur = q.front();
        int cn = cur.first;
        string cc = cur.second;
        q.pop();
        
        if (cn == B)
            return cc;

        // D
        int next = (cn * 2) % 10000;
        if(!visited[next])
        {
            visited[next] = true;
            q.push({next, cc + 'D'});
        }
        
        // S
        next = (cn == 0) ? 9999 : cn - 1;
        if(!visited[next])
        {
            visited[next] = true;
            q.push({next, cc + 'S'});
        }
        
        // L
        next = (cn % 1000) * 10 + (cn / 1000);
        if(!visited[next])
        {
            visited[next] = true;
            q.push({next, cc + 'L'});
        }

        // R
        next = (cn / 10) + (cn % 10) * 1000;
        if(!visited[next])
        {
            visited[next] = true;
            q.push({next, cc + 'R'});
        }
    }
    return "";
}

int main()
{
    int T;
    std::cin >> T;
    vector<std::string> result(T);
    

    for (int i = 0;i < T; i++)
    {
        int A,B;
        std::cin >> A >> B;

        result[i] = bfs(A,B);
    }

    for (std::string r : result)
        std::cout << r << std::endl;
}