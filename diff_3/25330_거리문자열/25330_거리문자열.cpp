#include <iostream>
#include <string>
#include <memory>
#include <algorithm>

std::string judge(std::string num)
{
    int now = 0;

    char numeric[10] = {'0','1','2','3','4','5','6','7','8','9'};
    char check[10] = {'0','0','0','0','0','0','0','0','0','0'};
    
    for (int i = 0; i < 10; i++)
    {
        int cnt = std::count(num.begin(), num.end(), numeric[i]);
        if(cnt != 0 && cnt != 2)
            return "no";
    }

    if(num[0] != '0')
    {
        while(now < num.size())
        {
            int val = num[now] - '0';
            if (check[val] == '1')
            {
                now++;
                continue;
            }
            if ((now + val + 1) < num.size() && num[now] == num[now + val + 1])
            {
                now++;
                check[val] = '1';
            }
            else
            {
                return "no";
            }
        }
        return "yes";
    }
    return "no";
}


int main(int argc, char** argv)
{
    int T;
    std::cin >> T;
    auto result = std::make_unique<std::string[]>(T);

    for (int i = 0; i < T; i++)
    {
        std::string num = "0";
        std::cin >> num;

        result[i] = judge(num);
    }


    for (int i = 0; i < T; i++)
        std::cout << result[i] << std::endl;
}