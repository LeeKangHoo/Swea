#include <iostream>
#include <vector>
#include <algorithm>

double calc(std::vector<int> num)
{
    std::sort(num.begin(), num.end());

    double r = 0;
    for (int i = 1; i < num.size() - 1; i++)
    {
        r += num[i];
    }
    return r / (num.size()-2);

}

int main(int argc,char** argv)
{
    int T;
    std::cin>> T;
    std::vector<double> result(T);

    for (int i = 0; i < T; i++)
    {
        std::vector<int> num(10);

        for (int j = 0; j < 10; j++ )
            std::cin >> num.at(j);

        result.at(i) = calc(num);
    }

    for (int i = 0; i < T; i++)
        std::cout << "#" << i+1 << " " << (int)(result[i]+0.5) << std::endl;


}