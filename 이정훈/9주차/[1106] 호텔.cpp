/*
* Author    : Lee JeongHun
* Date      : 2024.11.22(Fri)
* Runtime   : 0 ms
* Memory    : 2020 KB
* Algorithm : DP
*/

#include <iostream>
#include <vector>
#include <map>

using namespace std;

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    // 입력
    int c, n;
    cin >> c >> n;

    map<int, int> table;
    for(int i = 0; i < n; ++i)
    {
        int cost, num;
        cin >> cost >> num;
        
        for(int j = 1; j <= c / num; ++j)
        {
            int key = num * j;
            int value = cost * j;

            if(table.find(key) == table.end() || table[key] > value)
            {
                table.insert(make_pair(key, value));
            }
        }
    }

    // 풀이
    vector<vector<int>> dp();

    return 0;
}