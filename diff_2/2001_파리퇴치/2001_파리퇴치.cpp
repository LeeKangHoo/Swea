#include <iostream>
#include <vector>
#include <algorithm>

int calc(const std::vector<std::vector<int>> &num,int M)
{
    int max = 0;
    for (int y = 0; y <= num.size() - M; y++)
    {
        for (int i = 0; i <= num.size() - M; i++)
        {
            int sum = 0;
            for (int j = i; j < M + i; j++)
            {
                for (int z = y; z < M + y; z++)
                {
                    sum += num[j][z];
                }
            }
            max = std::max(sum,max);
        }
    }

    return max;
}

int main(int argc, char** argv)
{
    int T;
    std::cin >> T;
    int N,M = 0;
    std::vector<int> result(T);
    for (int i = 0; i < T; i++)
    {
        std::cin >> N >> M;
        std::vector<std::vector<int>> num(N,std::vector<int>(N,0));

        for (int z = 0; z < N; z++)
        {
            for (int p = 0; p < N; p++)
                std::cin>>num[z][p];
        }
        result[i] = calc(num,M);
    }

    for (int i = 0; i < T; i++)
        std::cout << "#" << i + 1 << " " << result[i] << std::endl;

    
}