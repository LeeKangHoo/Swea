#include <iostream>
#include <memory>



int fight(int* num)
{
    for (int i = 0; i < 3; i++)
    {
        if (num[i] % 2 == 0)
            return 1;
    }
    return 2;
    
}

int main(int argc, char** argv)
{

    int T;
    std::cin >> T;
    auto result = std::make_unique<int[]>(T);

    for (int i = 0; i < T; i++)
    {
        int num[3] = {0,0,0};
        std::cin >> num[0] >> num[1] >> num[2];        
        result[i] = fight(num);
    }

    for (int i = 0; i < T; i++)
        std::cout << result[i] << std::endl;

}