#include <iostream>
#include <vector>

//검은색 공과 상자 B
//흰색 공과 상자 W

//검검 점수 X
//흰흰 점수 Y
//이외 점수 Z

//45:12

int solve(int B, int W, int X, int Y, int Z)
{

int b = std::max(B,W);
int s = std::min(B,W);

    if (Y >= X)
    {
        if(X + Y < Z*2)
        {
            return (s * 2)* Z + (b - s) * ((std::max(B,W) == B)? X:Y);
        }
        return (W * Y) + (B * X);
    }
    else if( X > Y)
    {
        if(X + Y < Z*2)
        {
            return (s * 2)* Z + (b - s) * ((std::max(B,W) == B)? X:Y);
        }
        return (B * X) + (W * Y);
    }
    return 0;
}

int main(int argc,char** argv)
{
    int T;
    std::cin >> T;

    std::vector<int> result(T);

    for (int i = 0; i < T; i++)
    {
        int B , W , X, Y, Z = 0;
        std::cin >> B >> W >> X >> Y >> Z;
        result[i] = solve(B,W,X,Y,Z);
    }

    for (int i : result)
        std::cout << i << std::endl;
}