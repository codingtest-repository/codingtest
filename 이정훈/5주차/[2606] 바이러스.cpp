/*
* Author    : Lee JeongHun
* Date      : 2024.11.02(Sat)
* Runtime   : 0 ms
* Memory    : 2028 KB
* Algorithm : BFS
*/

#include <iostream>
#include <map>
#include <vector>
#include <set>

using namespace std;

void check(map<int, vector<int>>& map, set<int>& table, int index);

int main()
{
    // 입력 처리
    int n, m;
    cin >> n >> m;

    // 네트워크 맵 작성
    map<int, vector<int>> network_map;

    for(int i = 0; i < m; ++i)
    {
        int lh, rh;
        cin >> lh >> rh;
        --lh;
        --rh;

        // lh 컴퓨터 연결 상대에 rh 컴퓨터 등록
        if(network_map.find(lh) != network_map.end())
        {
            network_map[lh].push_back(rh);
        }
        else
        {
            network_map.insert(make_pair(lh, vector<int>(1, rh)));
        }

        // rh 컴퓨터 연결 상대에 lh 컴퓨터 등록
        if(network_map.find(rh) != network_map.end())
        {
            network_map[rh].push_back(lh);
        }
        else
        {
            network_map.insert(make_pair(rh, vector<int>(1, lh)));
        }
    }

    // 감염된 컴퓨터 파악
    set<int> infected_computers;
    infected_computers.insert(0);
    check(network_map, infected_computers, 0);

    // 정답 출력
    cout << infected_computers.size() - 1; // 1번 컴퓨터 제외

    return 0;
}

void check(map<int, vector<int>>& network_map, set<int>& table, int index)
{
    vector<int> indices_to_check;
    indices_to_check.reserve(network_map[index].size());
    for(int e : network_map[index])
    {
        if(table.find(e) == table.end())
        {
            indices_to_check.push_back(e);
            table.insert(e);
        }
    }

    for(int e : indices_to_check)
    {
        check(network_map, table, e);
    }
}