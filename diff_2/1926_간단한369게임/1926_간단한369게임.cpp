#include <iostream>
#include <string>

int judge(int n)
{
    std::string num = std::to_string(n);
    int count = 0;

    for (int i = 0; i < num.length(); i++)
    {
        if (num[i] == '3' || num[i] == '6' || num[i] ==  '9') count++;
    }
    return count;

}

int main(int argc, char** argv)
{
    int num;
    std::cin >> num;

    for (int i = 1; i < num + 1; i++)
    {
        if (judge(i) == 0 )
        {
            std::cout << i << " ";
        }
        else
        {
            for (int j = 0; j < judge(i); j++)
            {
                std::cout << "-";
            }
            std::cout << " ";
        }
    }
    std::cout << std::endl;
    return 0;
}