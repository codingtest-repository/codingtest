#include <iostream>
#include <vector>

using namespace std;

int main()
{
    // 변수 선언 및 초기화
    int n;
    cin >> n;

    vector<vector<int>> map(n, vector<int>(n, 0)); // 지뢰 정보, 지뢰가 존재하는 곳에는 1, 존재하지 않는 곳에는 0으로 표기
    vector<pair<int, int>> user_inputs; // 사용자 입력 정보
    vector<vector<int>> result(n, vector<int>(n, -1)); // 결과 (-1은 나중에 .으로 변환)
    bool should_show_mine = false; // 지뢰 표시 여부

    /* 입력 분석 */
    // 맵 정보 매핑
    for(int i = 0; i < n; i++)
    {
        for(int j = 0; j < n; j++)
        {
            char input;
            cin >> input;

            if(input == '*')
            {
                map[i][j] = 1;
            }
        }
    }

    // 사용자 입력 매핑
    for(int i = 0; i < n; i++)
    {
        for(int j = 0; j < n; j++)
        {
            char input;
            cin >> input;

            if(input == 'x')
            {
                user_inputs.push_back(make_pair(i, j));
            }
        }
    }

    // 주변 지뢰 확인
    // 좌표가 주어지면 인접한 8개의 칸 검사
    for(auto user_input : user_inputs)
    {
        // 지뢰를 건드렸는지 검사
        if(map[user_input.first][user_input.second] == 1)
        {
            should_show_mine = true;
            continue;
        }

        // 지뢰 개수 확인
        int count = 0;

        // 인접한 8개의 좌표 검사
        for(int i = -1; i <= 1; i++)
        {
            for(int j = -1; j <=1; j++)
            {
                // 자기 자신은 제외
                if(i == 0 && j == 0)
                {
                    continue;
                }

                // 좌표 유효성 검사
                pair<int, int> position = make_pair(user_input.first + i, user_input.second + j);
                if(position.first >= 0 && position.first < n && position.second >= 0 && position.second < n)
                {
                    // 지뢰 검사
                    if(map[position.first][position.second] == 1)
                    {
                        ++count;
                    }
                }
            }
        }

        // 결과 기록
        result[user_input.first][user_input.second] = count;
    }

    // 결과 출력
    for(int i = 0; i < n; ++i)
    {
        for(int j = 0; j < n; ++j)
        {
            if(result[i][j] == -1)
            {
                if(should_show_mine && map[i][j] == 1)
                {
                    cout << "*";
                }
                else
                {
                    cout << ".";
                }
            }
            else
            {
                cout << result[i][j];
            }
        }

        cout << endl;
    }

    return 0;
}