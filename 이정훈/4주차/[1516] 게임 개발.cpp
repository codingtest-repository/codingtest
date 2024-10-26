#include <iostream>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

int main()
{
    // 변수 선언 및 초기화
    int n;
    cin >> n;

    map<int, int> build_time_table; // 개별 건물 건설 시간
    map<int, vector<int>> pre_build_table; // 먼저 지어져야 하는 건물 목록
    map<int, int> final_build_time_table; // 개별 건물 최종 건설 시간
    
    vector<int> list_to_build; // 건설 목록
    list_to_build.reserve(n);
    for(int i = 0; i < n; i++)
    {
        list_to_build.push_back(i);
    }

    // 입력 분석
    for(int i = 0; i < n; i++)
    {
        // 개별 건물 건설 시간 매핑
        int t;
        cin >> t;
        build_time_table.insert(make_pair(i, t));

        // 먼저 지어져야 하는 건물 번호 매핑
        vector<int> pre_build_list;
        while(true)
        {
            int input;
            cin >> input;
            if(input == -1)
            {
                break;
            }

            pre_build_list.push_back(--input);
        }

        // 즉시 건설 가능한 건물 처리
        if(pre_build_list.size() == 0)
        {
            final_build_time_table.insert(make_pair(i, t));
            list_to_build.erase(remove(list_to_build.begin(), list_to_build.end(), i), list_to_build.end());
        }
        else
        {
            pre_build_table.insert(make_pair(i, pre_build_list));
        }
    }

    // 최종 건설 시간 계산
    while(list_to_build.size() > 0)
    {
        vector<int> new_list_to_build;
        new_list_to_build.reserve(list_to_build.size());
        for(auto building : list_to_build)
        {
            // 건설 가능 조건 확인
            bool can_build = true;
            int max_build_time = 0;
            for(auto e : pre_build_table[building])
            {
                // 먼저 지어져야하는 건물이 아직 건설되지 않은 경우
                if(final_build_time_table.find(e) == final_build_time_table.end())
                {
                    can_build = false;
                    break;
                }
                else if(max_build_time < final_build_time_table[e])
                {
                    max_build_time = final_build_time_table[e];
                }
            }

            // 건설이 가능한 경우 최종 건설 시간 기록 및 건설 목록에서 제외
            if(can_build)
            {
                final_build_time_table[building] = max_build_time + build_time_table[building];
            }
            else
            {
                new_list_to_build.push_back(building);
            }
        }

        // 건설 목록 갱신
        list_to_build = new_list_to_build;
    }

    // 정답 출력
    for(auto p : final_build_time_table)
    {
        cout << p.second << endl;
    }

    return 0;
}