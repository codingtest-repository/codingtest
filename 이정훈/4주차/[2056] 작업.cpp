/*
* Author    : Lee JeongHun
* Date      : 2024.10.26(Sat)
* Runtime   : 352 ms
* Memory    : 6288 KB
* Algorithm : topology sort
*/

#include <iostream>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

int main()
{
    // 입력 분석
    int n;
    cin >> n;

    map<int, int> work_time; // 개별 작업 소요 시간
    map<int, int> final_work_time; // 개별 작업 최종 소요 시간
    map<int, vector<int>> work_list; // 선행 작업 정보
    
    vector<int> work_to_do; // 처리할 작업 목록
    work_to_do.reserve(n);
    for(int i = 0; i < n; i++)
    {
        work_to_do.push_back(i);
    }

    // 매핑
    for(int i = 0; i < n; i++)
    {
        int time, count;
        cin >> time >> count;

        // 개별 작업 소요 시간 매핑
        work_time.insert(make_pair(i, time));

        // 선행 작업 정보 매핑
        vector<int> works;
        works.reserve(count);
        for(int j = 0; j < count; j++)
        {
            int work;
            cin >> work;
            work--;
            
            works.push_back(work);
        }

        if(works.size() > 0)
        {
            work_list.insert(make_pair(i, works));
        }
        else
        {
            final_work_time.insert(make_pair(i, time));
            work_to_do.erase(remove(work_to_do.begin(), work_to_do.end(), i), work_to_do.end());
        }
    }

    // 최종 소요 시간 계산
    while(work_to_do.size() > 0)
    {
        vector<int> new_work_to_do;
        new_work_to_do.reserve(work_to_do.size());

        for(int work : work_to_do)
        {
            // final_work_time에 모든 선행 작업이 등록되어있는지 확인
            bool can_calculate = true;
            int max_work_time = 0;
            for(int finished_work : work_list[work])
            {
                if(final_work_time.find(finished_work) == final_work_time.end())
                {
                    can_calculate = false;
                    break;
                }
                else if(max_work_time < final_work_time[finished_work])
                {
                    max_work_time = final_work_time[finished_work];
                }
            }

            // 모든 선행 작업이 등록된 경우
            if(can_calculate)
            {
                final_work_time[work] = max_work_time + work_time[work];
            }
            else
            {
                new_work_to_do.push_back(work);
            }
        }

        work_to_do = new_work_to_do;
    }

    // 출력
    int answer = 0;
    for(auto p : final_work_time)
    {
        if(answer < p.second)
        {
            answer = p.second;
        }
    }

    cout << answer;

    return 0;
}

// 각 작업 별로 걸리는 최종 시간을 구한 뒤, 그 중 가장 오래 걸린 시간이 모든 작업을 완료하기 위한 최소 시간이다.
// 각 작업 별로 걸리는 최종 시간을 구하는 방법은 선행 작업들 중 가장 오래 걸린 시간 + 해당 작업 시간이다.