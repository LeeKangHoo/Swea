#include <iostream>
#include <string>
#include <cstdio>

struct Date
{
    int y;
    int m;
    int d;
};


std::string calc(Date date)
{
    std::string r;

    if (date.m % 2 == 0 && date.m > 0 && 12 >= date.m && 31 >= date.d && date.d > 0)
    {
        if (date.m == 2 && date.d > 28)
            return "-1";
        if (date.m < 8 && date.d > 30)
            return "-1";
        char buf[20];
        sprintf(buf,"%04d/%02d/%02d",date.y,date.m,date.d);
        return std::string(buf);
    }
    else if (date.m % 2 == 1 && date.m > 0 && 12 >= date.m && 32 >= date.d && date.d > 0)
    {
        if (date.m > 7 && date.d > 30)
            return "-1";
        char buf[20];
        sprintf(buf,"%04d/%02d/%02d",date.y,date.m,date.d);
        return std::string(buf);
    }
    return "-1";
}

Date parse(int num)
{
    Date date;
    date.y = num / 10000;
    date.m = num / 100 % 100;
    date.d = num % 100;
    
    return date;

}

int main(int argc, char** argv)
{
    int count;
    std::cin >> count;
    int num[count];
    std::string result[count];

    
    for (int i = 0; i < count; i++)
    {
        std::cin >> num[i];
        Date date = parse(num[i]);
        result[i] = calc(date);
        // std::cout << "#" << i+1 << " " << calc(date) << std::endl;
    }
    for (int z = 0; z < count; z++)
    {
        std::cout << "#" << z+1 << " " << result[z] << std::endl;
    }


}