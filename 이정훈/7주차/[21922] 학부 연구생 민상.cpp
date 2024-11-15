/*
* Author    : Lee JeongHun
* Date      : 2024.11.15(Fri)
* Runtime   : 728 ms
* Memory    : 33436 KB
* Algorithm : Graph Search
*/

#include <iostream>
#include <vector>

using namespace std;

enum Direction
{
    Up,
    Down,
    Left,
    Right
};

void process(const vector<vector<int>>& map, vector<vector<int>>& visit, int row, int column, Direction dir);

int main()
{
    // 입력 처리
    int n, m;
    cin >> n >> m;

    vector<pair<int, int>> starts;
    vector<vector<int>> map(n, vector<int>(m));
    for(int i = 0; i < n; ++i)
    {
        for(int j = 0; j < m; ++j)
        {
            cin >> map[i][j];

            if(map[i][j] == 9)
            {
                starts.push_back(make_pair(i, j));
            }
        }
    }

    // 앉을 수 있는 자리는 1로 표기
    vector<vector<int>> visit(n, vector<int>(m));

    for(auto p : starts)
    {
        int row = p.first;
        int column = p.second;

        visit[row][column] = 1;

        process(map, visit, row, column, Up);
        process(map, visit, row, column, Down);
        process(map, visit, row, column, Left);
        process(map, visit, row, column, Right);
    }

    // 정답 출력
    int count = 0;
    for (int i = 0; i < n; ++i)
    {
        for (int j = 0; j < m; ++j)
        {
            if(visit[i][j] == 1)
            {
                ++count;
            }
        }
    }

    cout << count << endl;
    
    return 0;
}

void process(const vector<vector<int>>& map, vector<vector<int>>& visit, int row, int column, Direction dir)
{
    switch(dir)
    {
        case Up:

        // 진행
        --row;

        // 유효하지 않은 위치
        if(row < 0)
        {
            return;
        }

        // 방문 처리
        visit[row][column] = 1;

        // 물건에 따른 처리 (Up)
        switch(map[row][column])
        {
            case 0:
            process(map, visit, row, column, dir);
            break;

            case 1:
            process(map, visit, row, column, dir);
            break;

            case 2: 
            return;
            break;

            case 3:
            process(map, visit, row, column, Right);
            break;

            case 4:
            process(map, visit, row, column, Left);
            break;

            case 9:
            return;
            break;
        }

        break;

        case Down:

        // 진행
        ++row;

        // 유효하지 않은 위치
        if(row >= map.size())
        {
            return;
        }

        // 방문 처리
        visit[row][column] = 1;

        // 물건에 따른 처리 (Down)
        switch(map[row][column])
        {
            case 0:
            process(map, visit, row, column, dir);
            break;

            case 1:
            process(map, visit, row, column, dir);
            break;

            case 2:
            return;
            break;

            case 3:
            process(map, visit, row, column, Left);
            break;

            case 4:
            process(map, visit, row, column, Right);
            break;

            case 9:
            return;
            break;
        }

        break;

        case Left:

        // 진행
        --column;

        // 유효하지 않은 위치
        if(column < 0)
        {
            return;
        }

        // 방문 처리
        visit[row][column] = 1;

        // 물건에 따른 처리 (Left)
        switch(map[row][column])
        {
            case 0:
            process(map, visit, row, column, dir);
            break;

            case 1:
            return;
            break;

            case 2:
            process(map, visit, row, column, dir);
            break;

            case 3:
            process(map, visit, row, column, Down);
            break;

            case 4:
            process(map, visit, row, column, Up);
            break;

            case 9:
            return;
            break;
        }

        break;

        case Right:

        // 진행
        ++column;

        // 유효하지 않은 위치
        if(column >= map[0].size())
        {
            return;
        }

        // 방문 처리
        visit[row][column] = 1;

        // 물건에 따른 처리 (Right)
        switch(map[row][column])
        {
            case 0:
            process(map, visit, row, column, dir);
            break;

            case 1:
            return;
            break;

            case 2:
            process(map, visit, row, column, dir);
            break;

            case 3:
            process(map, visit, row, column, Up);
            break;

            case 4:
            process(map, visit, row, column, Down);
            break;

            case 9:
            return;
            break;
        }

        break;
    }
}