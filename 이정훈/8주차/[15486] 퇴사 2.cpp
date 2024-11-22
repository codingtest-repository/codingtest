/*
* Author    : Lee JeongHun
* Date      : 2024.11.22(Fri)
* Runtime   : 192 ms
* Memory    : 19600 KB
* Algorithm : DP
*/

#include <iostream>
#include <vector>

using namespace std;

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    // 입력
    int n;
    cin >> n;

    vector<pair<int, int>> works(n + 1);
    for(int i = 1; i <= n; ++i)
    {
        int t, p;
        cin >> t >> p;
        works[i] = make_pair(t, p);
    }

    // 풀이

    vector<int> dp(n + 1);
    for(int i = 1; i <= n; ++i)
    {
        int t, p;
        t = works[i].first;
        p = works[i].second;

        dp[i] = max(dp[i], dp[i - 1]);

        if(t == 1)
        {
            dp[i] = max(dp[i], dp[i - 1] + p);   
        }
        else if(i + t - 1 <= n)
        {
            dp[i + t - 1] = max(dp[i + t - 1], dp[i - 1] + p);
        }
    }

    // 출력
    cout << dp[n] << '\n';

    return 0;
}