/*
* Author    : Lee JeongHun
* Date      : 2024.11.22(Fri)
* Runtime   : 0 ms
* Memory    : 2180 KB
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
    int n, k;
    cin >> n >> k;

    vector<int> coins(n + 1);
    for(int i = 1; i <= n; ++i)
    {
        cin >> coins[i];
    }

    // 문제 풀이
    vector<int> dp(k + 1, 10001); // 1 <= k <= 10,000
    dp[0] = 0;

    for(int i = 1; i <= n; ++i)
    {
        for(int j = coins[i]; j <= k; ++j)
        {
            dp[j] = min(dp[j], dp[j - coins[i]] + 1);
        }
    }

    // 정답 출력
    int answer = dp[k] == 10001 ? -1 : dp[k];
    cout << answer << '\n';

    return 0;
}