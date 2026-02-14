#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
//48
using namespace std;

string judge(string v1)
{   
    //짝수
    if(v1.length()%2 == 0)
    {
        int middle = (v1.length()/2);
        string t1 = v1;
        t1.erase(t1.begin()+middle,t1.end());
        string t2 = v1;
        t2.erase(t2.begin(), t2.end()-middle);
        reverse(t2.begin(),t2.end());
        if(t1 == t2)
            return "YES";

    }
    else //홀수
    {
        int middle = (v1.length()/2);
        string t1 = v1;
        t1.erase(t1.begin()+middle,t1.end());
        string t2 = v1;
        t2.erase(t2.begin(), t2.end()-middle);
        reverse(t2.begin(),t2.end());
        if(t1 == t2)
            return "YES";
    }

    return "NO";
    

}
string solve(string v1)
{
    if(v1.length()%2 == 0)
    {
        int middle = (v1.length()/2);
        string t1 = v1;
        t1.erase(t1.begin()+middle,t1.end());
        string t2 = v1;
        t2.erase(t2.begin(), t2.end()-middle);
        reverse(t2.begin(),t2.end());
        if(t1 != t2)
            return "NO";
        if(judge(t1) == "YES"&&judge(t2) == "YES")
            return "YES";
    }
    else //홀수
    {
        int middle = (v1.length()/2);
        string t1 = v1;
        t1.erase(t1.begin()+middle,t1.end());
        string t2 = v1;
        t2.erase(t2.begin(), t2.end()-middle);
        reverse(t2.begin(),t2.end());
        if(t1 != t2)
            return "NO";
        if(judge(t1) == "YES"&&judge(t2) == "YES")
            return "YES";
    }

    return "NO";
    
}

int main()
{
    int T; cin >> T;
    vector<string> result(T);

    for (int i = 0; i < T;i++)
    {
        string tmp;
        cin >> tmp;
        result[i] = solve(tmp);
    }

    for(int i = 0; i < T; i++)
        cout << "#" << i+1 << " " << result[i] << endl;
}