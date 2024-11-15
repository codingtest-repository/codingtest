/*
* Author    : Lee JeongHun
* Date      : 2024.11.15(Fri)
* Runtime   : 32 ms
* Memory    : 2284 KB
* Algorithm : Implementation
*/

#include <iostream>
#include <vector>

using namespace std;

int main()
{
    // 입력 처리
    int r, c, n;
    cin >> r >> c >> n;

    // 빈 땅은 0, 폭탄이 있는 땅은 1로 표기
    vector<vector<pair<int, int>>> map(r, vector<pair<int, int>>(c));
    for(int i = 0; i < r; ++i)
    {
        for(int j = 0; j < c; ++j)
        {
            char input;
            cin >> input;

            if(input == 'O')
            {
                map[i][j] = make_pair(1, 2); // 초기 폭탄 설치
            }
        }
    }

    // n 초 경과
    for(int t = 2; t <= n; ++t)
    {
        for(int i = 0; i < r; ++i)
        {
            for(int j = 0; j < c; ++j)
            {
                // 폭탄이 설치된 경우 폭탄 타이머 설정
                if(map[i][j].first == 1)
                {
                    int timer = map[i][j].second - 1;
                    if(timer == 0)
                    {
                        // 폭발
                        map[i][j] = make_pair(0, 0);

                        int row, column;
                        
                        // 상
                        row = i - 1;
                        column = j;

                        if(row >= 0)
                        {
                            if(map[row][column].first == 1 && map[row][column].second != 0)
                            {
                                map[row][column] = make_pair(0, 0);
                            }
                        }

                        // 하
                        row = i + 1;
                        column = j;

                        if(row < map.size())
                        {
                            if(map[row][column].first == 1 && map[row][column].second != 1)
                            {
                                map[row][column] = make_pair(0, 0);
                            }
                        }

                        // 좌
                        row = i;
                        column = j - 1;

                        if(column >= 0)
                        {
                            if(map[row][column].first == 1 && map[row][column].second != 0)
                            {
                                map[row][column] = make_pair(0, 0);
                            }
                        }

                        // 우
                        row = i;
                        column = j + 1;

                        if(column < map[0].size())
                        {
                            if(map[row][column].first == 1 && map[row][column].second != 1)
                            {
                                map[row][column] = make_pair(0, 0);
                            }
                        }
                    }
                    else
                    {
                        map[i][j] = make_pair(1, timer);
                    }
                }

                // 폭탄 설치
                if(t % 2 == 0)
                {
                    if(map[i][j].first == 0)
                    {
                        map[i][j] = make_pair(1, 3);
                    }
                }
            }
        }
    }

    // 정답 출력
    for(int i = 0; i < r; ++i)
    {
        for(int j = 0; j < c; ++j)
        {
            if(map[i][j].first == 1)
            {
                cout << "O";
            }
            else
            {
                cout << ".";
            }
        }

        cout << endl;
    }

    return 0;
}