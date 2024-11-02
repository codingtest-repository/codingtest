/*
* Author    : Lee JeongHun
* Date      : 2024.11.02(Sat)
* Runtime   : 0 ms
* Memory    : 2020 KB
* Algorithm : Greedy Algorithm
*/

#include <iostream>

using namespace std;

int main()
{
    // 입력 처리
    int a, b, c, m;
    cin >> a >> b >> c >> m;

    // 변수 선언
    int fatigue = 0;
    int work = 0;

    for(int i = 0; i < 24; ++i)
    {
        // 지금 일을 할 수 있는 상태인지 검사
        if(fatigue + a <= m)
        {
            // 일 처리
            fatigue += a;
            work += b;
        }
        else
        {
            // 휴식
            fatigue -= c;
            if(fatigue < 0) fatigue = 0;
        }
    }

    // 정답 출력
    cout << work;

    return 0;
}