/*
* Author    : Lee JeongHun
* Date      : 2024.11.15(Fri)
* Runtime   : 0 ms
* Memory    : 2020 KB
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

    vector<int> wall(n - 1, 1); // 0은 무너진 벽을 나타낸다

    for (int i = 0; i < m; ++i)
    {
        int start, end;
        cin >> start >> end;

        start -= 1;
        end -= 1;
        
        for(int j = start; j < end; ++j)
        {
            wall[j] = 0;
        }
    }

    int count = 1;
    for(int e : wall)
    {
        if(e == 1)
        {
            ++count;
        }
    }

    // 정답 출력
    cout << count << endl;

    return 0;
}