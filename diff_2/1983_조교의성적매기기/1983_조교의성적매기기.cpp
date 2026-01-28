#include <iostream>
#include <algorithm>
#include <vector>
#include <string>

std::string calc(const std::vector<std::vector<int>> &num,int K)
{
    std::string grade[10] = {"A+","A0","A-","B+","B0","B-","C+","C0","C-","D0"};
    std::vector<double> sum(num.size());
    std::vector<int> idx(num.size());
    
    for (int i = 0; i < num.size(); i++)
    {
        idx[i] = i;
        sum[i] = (num[i][0] * 0.35)+(num[i][1]*0.45)+(num[i][2]*0.2);
    }

    std::sort(idx.begin(), idx.end(), [&](int a, int b)
{
    return sum[a] > sum[b];
});
    
    int target = std::find(idx.begin(), idx.end(), K - 1) - idx.begin();

    return grade[target/(num.size()/10)];
    
}

int main(int argc, char** argv)
{
    int T;
    std::cin>>T;
    std::vector<std::string> result(T);
    // unique_ptr<int> result(int[T]);
    int N,K = 0;
    for (int t = 0; t < T; t++)
    {
        std::cin >> N >> K;
        std::vector<std::vector<int>> num(N,std::vector<int>(N,0));   
        for (int i = 0; i < N; i++)
        {
            for (int j = 0; j < 3; j++)
            {
                std::cin>>num[i][j];
            }
        }
        result[t] = calc(num,K);
    }

    for (int i = 0; i < T; i++)
        std::cout << "#" << i + 1 << " " << result[i] << std::endl;
}