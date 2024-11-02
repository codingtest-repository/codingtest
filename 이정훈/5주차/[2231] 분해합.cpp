/*
* Author    : Lee JeongHun
* Date      : 2024.11.02(Sat)
* Runtime   : 20 ms
* Memory    : 2020 KB
* Algorithm : brute force
*/

#include <iostream>
#include <string>

using namespace std;

int main()
{
    // 입력 처리
    int n;
    cin >> n;

    // 변수 선언
    int constructor = 0;
    
    // 생성자는 n 보다 작다
    for(int i = 0; i < n; ++i)
    {
        int sum = i;
        string target = to_string(i);
        for(char c : target)
        {
            sum += c - '0';
        }

        if(sum == n)
        {
            constructor = i;
            break;
        }
    }

    // 정답 출력
    cout << constructor;

    return 0;
}