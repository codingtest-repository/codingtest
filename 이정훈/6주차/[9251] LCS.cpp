/*
* Author    : Lee JeongHun
* Date      : 2024.11.09(Sat)
* Runtime   : 4 ms
* Memory    : 5984 KB
* Algorithm : DP
*/

#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

int main()
{
    // 입력 처리
    string first;
    string second;

    cin >> first >> second;

    // 변수 선언 및 초기화
    int answer = 0;
    vector<vector<int>> lcs(first.size() + 1, vector<int>(second.size() + 1));

    for(int i = 1; i < first.size() + 1; ++i)
    {
        for(int j = 1; j < second.size() + 1; ++j)
        {
            if(first[i - 1] == second[j - 1])
            {
                lcs[i][j] = lcs[i - 1][j - 1] + 1;
            }
            else
            {
                lcs[i][j] = max(lcs[i - 1][j], lcs[i][j - 1]);
            }

            answer = max(answer, lcs[i][j]);
        }
    }

    cout << answer;

    return 0;
}