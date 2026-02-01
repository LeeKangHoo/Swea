#include <iostream>
#include <vector>
#include <string>

//같은 색 E 0
//인접한 색 A 1 ,-1
// 반대 색 C 0
// 다 아니면 X

char solve(std::string* color)
{
    std::string c[18] = {"red","orange","yellow","green", "blue", "purple","red","orange","yellow","green", "blue", "purple","red","orange","yellow","green", "blue", "purple"};

    if (color[0] != color[1])
    {
        for (int i = 0; i < 6; i++)
        {
            if(color[0] == c[i+6])
            {
                if(color[1] == c[i-5] || color[1] == c[i+7])
                    return 'A';
                if(color[1] == c[i-3] || color[1] == c[i+9])
                    return 'C';
            }
        }
        
    }
    else
    {
        return 'E';
    }
    return 'X';
    
}


int main(int argc, char** argv)
{
    int T;
    std::cin >> T;
    std::vector<char> result(T);

    for ( int i = 0; i < T;i++)
    {
        std::string color[2];

        std::cin >> color[0] >> color[1];
        std::cout << color[0] << ", " << color[1] << std::endl;

        result[i] = solve(color);
    }
    for (char i : result)
        std::cout << i << std::endl;
}