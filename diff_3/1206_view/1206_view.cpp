#include <iostream>
#include <vector>
#include <algorithm>
//53
using namespace std;


int solve(vector<vector<bool>> &mapp,int N)
{
    int cnt = 0;
    int check_list[] = {2,1,-1,-2};
    for (int i = 2; i < N-2; i++)
    {
        auto end_it = find(mapp[i].rbegin(),mapp[i].rend(), true);
        if (end_it == mapp[i].rend())
            continue;
        int end_idx = distance(mapp[i].begin(), end_it.base()) -1;

        for (int j = 0; j <= end_idx; j++)
        {
            bool flag = true;
            for (int z = 0; z < 4; z++)
            {
                if (mapp[i+check_list[z]][j]) flag = false;
            }

            if (flag) cnt++;

        }
    }
    return cnt;

}


int main()
{
    vector<int> result(10);

    for (int i = 0;i < 10; i++)
    {
        int N;
        cin >> N;
        vector<vector<bool>> mapp(N,vector<bool>(256,false));
        for (int j = 0; j < N; j++)
        {
            int tmp;
            cin >> tmp;
            fill(mapp[j].begin(),mapp[j].begin() + tmp, true);
        }
        result[i] = solve(mapp,N);
    }

    for (int i = 0; i < 10; i++)
    {
        cout << "#" << i+1 << " " << result[i] << endl;
    }



}