#include <iostream>
#include <vector>
#include <string>
// 1 2 3 4 5 6 7 8 9 0
// 1 -> 4 6 9 0 
// 2 -> 8

//7
//4888
//

std::string solve(int num)
{
    std::string n;
    if (num == 1)
        return "0";
    if(num == 0)
        return "1";
    
    if (!(num % 2))
    {
        for (int i = 0; i < num/2; i++)
        {
            n += '8';
        }
    }
    else
    {
        n += '4';
        for (int i = 0; i < (num/2); i++)
        {
            n += '8';
        }
    }
    return n;

}


int main(int argc, char** argv)
{
    int T;
    std::cin >> T;
    std::vector<std::string> result(T);

    for (int i = 0; i < T; i++)
    {
        int num = 0;
        std::cin >> num;
        result[i] = solve(num);
    }
    for (int i = 0; i < T; i++)
        std::cout << result[i] << std::endl;
}