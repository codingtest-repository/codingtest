/*
* Author    : Lee JeongHun
* Date      : 2024.11.09(Sat)
* Runtime   : 36 ms
* Memory    : 3076 KB
* Algorithm : DP
*/

#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>

using namespace std;

int main()
{
    // 입력 처리
    int n;
    cin >> n;

    vector<vector<int>> triangle(n);

    for(int i = 0; i < n; ++i)
    {
        triangle[i].reserve(i);

        for(int j = 0; j <= i; ++j)
        {
            int input;
            cin >> input;
            triangle[i].push_back(input);
        }
    }

    // 점화식
    // j = 0 or i인 경우에는 경로가 하나밖에 존재하지 않습니다.
    // 그 외에는 result[i][j] = max(result[i - 1][j - 1], result[i - 1][j]) + triangle[i][j]입니다.

    for(int i = 1; i < n; ++i)
    {
        for(int j = 0; j <= i; ++j)
        {
            if(j == 0)
            {
                triangle[i][j] += triangle[i - 1][0];
            }
            else if(j == i)
            {
                triangle[i][j] += triangle[i - 1][i - 1];
            }
            else
            {
                triangle[i][j] += max(triangle[i - 1][j - 1], triangle[i - 1][j]);
            }
        }
    }

    // 정답 출력
    int answer = *max_element(triangle[n - 1].begin(), triangle[n - 1].end());

    cout << answer;

    return 0;
}