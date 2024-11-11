/*
* Author    : Lee JeongHun
* Date      : 2024.11.09(Sat)
* Runtime   : 308 ms
* Memory    : 2680 KB
* Algorithm : Implementation
*/

#include <iostream>
#include <vector>

using namespace std;

int main()
{
    // 입력 처리
    int n, m;
    cin >> n >> m;

    vector<vector<int>> array(n, vector<int>(m));

    for(int i = 0; i < n; ++i)
    {
        for(int j = 0; j < m; ++j)
        {
            cin >> array[i][j];
        }
    }

    // dp[i][j]는 (0,0) ~ (i,j)까지의 합을 나타냅니다.
    vector<vector<int>> dp(n, vector<int>(m));

    // 점화식
    for(int i = 0; i < n; ++i)
    {
        for(int j = 0; j < m; ++j)
        {
            if(i == 0 && j == 0)
            {
                dp[0][0] = array[0][0];
            }
            else if(i == 0)
            {
                dp[0][j] = dp[0][j - 1] + array[0][j];
            }
            else if(j == 0)
            {
                dp[i][0] = dp[i - 1][0] + array[i][0];
            }
            else
            {
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1] + array[i][j];
            }
        }
    }

    // 정답 출력
    int k;
    cin >> k;

    for(int i = 0; i < k; ++i)
    {
        int a, b, x, y;
        cin >> a >> b >> x >> y;
        --a;
        --b;
        --x;
        --y;

        int sum;

        if(a == 0 && b == 0)
        {
            sum = dp[x][y];
        }
        else if(a == 0)
        {
            sum = dp[x][y] - dp[x][b -1];
        }
        else if(b == 0)
        {
            sum = dp[x][y] - dp[a - 1][y];
        }
        else
        {
            sum = dp[x][y] - dp[a - 1][y] - dp[x][b - 1] + dp[a - 1][b - 1];
        }

        cout << sum << endl;
    }

    return 0;
}