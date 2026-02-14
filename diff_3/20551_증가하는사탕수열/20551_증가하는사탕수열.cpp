#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int solve(vector<int> box)
{
    int cnt = 0;

    if(box[0] < 1 || box[1] < 2|| box[2] < 3)
        return -1;

    while(true)
    {
        vector<int> sorted = box;
        sort(sorted.begin(), sorted.end());
        if(sorted == box&& sorted[0] != sorted[1] && sorted[1] != sorted[2])
            return cnt;
        
        if(box[1] >= box[2])
        {
            box[1]--;
            cnt++;
        }
        if(box[0] >= box[1])
        {
            box[0]--;
            cnt++;
        }
    }

    return -1;
    

}

int main()
{
    int T; cin >> T;
    vector<int> result(T);
    vector<int> box(3);

    for (int i = 0; i < T; i++)
    {
        cin >> box[0] >> box[1] >> box[2];
        result[i] = solve(box);
    }

    for (int i = 0; i < T;i++)
        cout << "#" << i+1 << " " << result[i] << endl;
}