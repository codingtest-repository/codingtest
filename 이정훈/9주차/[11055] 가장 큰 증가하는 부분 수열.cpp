/*
* Author    : Lee JeongHun
* Date      : 2024.11.22(Fri)
* Runtime   : 0 ms
* Memory    : 2020 KB
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

    vector<int> arr(n);
    for(int i = 0; i < n; ++i)
    {
        cin >> arr[i];
    }

    // 풀이
    vector<int> dp(n);
    int sum = dp[0];
    for(int i = 0; i < n; ++i)
    {
        dp[i] = arr[i];

        for(int j = 0; j < i; ++j)
        {
            if(arr[j] < arr[i])
            {
                dp[i] = max(dp[i], arr[i] + dp[j]);
            }
        }

        sum = max(sum, dp[i]);
    }

    // 정답
    cout << sum << '\n';

    return 0;
}