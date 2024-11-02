/*
* Author    : Lee JeongHun
* Date      : 2024.11.02(Sat)
* Runtime   : 8 ms
* Memory    : 2024 KB
* Algorithm : brute force
*/

#include <iostream>
#include <string>

using namespace std;

bool check(string target, int k);

int main()
{
    // 변수 선언 및 초기화
    int n, k;
    cin >> n >> k;

    int count = 0;

    int max = n * 3600 + 59 * 60 + 59; // N시 59분 59초를 초 단위로 환산

    for(int i = 0; i <= max; ++i)
    {
        // 시 분 초로 환산
        int hour = i / 3600;
        int minute = (i % 3600) / 60;
        int second = i % 60;

        string hour_str = hour < 10 ? "0" + to_string(hour) : to_string(hour);
        string minute_str = minute < 10 ? "0" + to_string(minute) : to_string(minute);
        string second_str = second < 10 ? "0" + to_string(second) : to_string(second);

        if(check(hour_str, k) || check(minute_str, k) || check(second_str, k))
        {
            ++count;
        }
    }

    // 정답 출력
    cout << count << endl;

    return 0;
}

bool check(string target, int k)
{
    return target.find(to_string(k)) != string::npos;
}