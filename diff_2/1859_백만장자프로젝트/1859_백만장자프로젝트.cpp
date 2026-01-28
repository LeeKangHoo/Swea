#include <iostream>
#include <vector>
#include <algorithm>

long predict(std::vector<int> price)
{
    // int min = 10001;
    // int max = 0;
    // for (int i = 0; i < price.size(); i++)
    // {
    //     if (min > price[i]) min = price[i];
    //     if (max < pritce[i]) max = price[i];
    // }
    
    auto now = price.begin();
    long money = 0;
    int buy_count = 0;

    while (now < price.end())
    {
        auto max_it = std::max_element(now, price.end());
        

        while(max_it > now)
        {
            money -= *now;
            buy_count++;
            now++;
        }
        money += buy_count * *max_it;
        buy_count = 0;
        now++;
    }
    return money;

}

int main(int argc, char** argv)
{
    int T;
    std::cin >> T;
    std::vector<long> result(T);

    for (int i = 0; i < T; i++)
    {
        int day;
        std::cin >> day;
        std::vector<int> price(day);
        for (int j = 0; j < day; j++)
        {
            std::cin >> price[j];
        }

        result.at(i) = predict(price);
        

    }
    for (int i = 0; i < T; i++)
        std::cout << "#" << i+1 << " " << result[i] << std::endl;

}