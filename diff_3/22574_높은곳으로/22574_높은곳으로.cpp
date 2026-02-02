#include <iostream>
#include <vector>

//

int solve(int N, int P)
{
    int current = 0;
    int tmp = 0;
    for (int i = 1; i <= N; i++)
    {
        if(current + i == P)
        {
            tmp += -1;
        }
        current += i;
    }
    return current + tmp;
}



int main()
{
    int T;
    std::cin >> T;
    std::vector<int> result(T);

    for (int i = 0; i < T; i++)
    {
        int N,P = 0;
        std::cin >> N >> P;

        result[i] = solve(N,P);
    }
    for (int i : result)
        std::cout << i << std::endl;
}