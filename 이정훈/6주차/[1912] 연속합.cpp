/*
* Author    : Lee JeongHun
* Date      : 2024.11.09(Sat)
* Runtime   : 24 ms
* Memory    : 2412 KB
* Algorithm : DP
*/

#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

int main()
{
    // 입력 처리
    int n;
    cin >> n;

    vector<int> array;
    array.reserve(n);
    for(int i = 0; i < n; ++i)
    {
        int input;
        cin >> input;

        array.push_back(input);
    }

    int sum = array[0];
    int answer = sum;
    for(int i = 1; i < n; ++i)
    {
        sum = sum < 0 ? array[i] : sum + array[i];
        answer = max(answer, sum);
    }

    // 정답 출력
    cout << answer;

    return 0;
}