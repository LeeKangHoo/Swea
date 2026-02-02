#include <iostream>
#include <vector>
#include <string>

// 5
//(0) 1 2 3 4 5
//AAA
//1 2
// 3

std::string solve(int num)
{
    if (num % 3 == 1)
        return "impossible";
    std::string r(num, 'B');
    std::vector<long long> f(num+1);


    f[1] = 1; 
    if(num >= 2) 
        f[2] = 1;
    long long sum = f[1] + (num >= 2? f[2] : 0);

    for (int i = 3; i <= num; i++)
    {
        f[i] = f[i - 1] + f[i - 2];
        sum += f[i];
    }
    
    if ( sum % 2 != 0)
        return "impossible";

        
    long long target = sum/2;

    for (int i = num; i >= 1; i--)
    {
        if (f[i] <= target)
        {
            r[i-1] = 'A';
            target -= f[i];
        }
        
    }
    if (target != 0)
        return "impossible";
    
    return r;

}

int main()
{
    int T;
    std::cin >> T;
    std::vector<std::string> result(T);

    for (int i = 0; i < T; i++)
    {
        int num;
        std::cin >> num;
        result[i] = solve(num);
    }

    for(std::string r : result)
        std::cout << r << std::endl;
}