/*
* Author    : Lee JeongHun
* Date      : 2024.10.26(Sat)
* Runtime   : 524 ms
* Memory    : 4936 KB
* Algorithm : topology sort
*/

#include <iostream>
#include <map>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    int N, M;
    cin >> N >> M;

    vector<int> answer(N, 0);

    // 선수과목 조건 기록
    map<int, vector<int>> table;

    for(int i = 0; i < M; i++)
    {
        int a, b;
        cin >> a >> b;

        a--;
        b--;
        
        if(table.find(b) == table.end())
        {
            table.insert(make_pair(b, vector<int>(1, a)));
        }
        else
        {
            table[b].push_back(a);
        }
    }

    // 수강하지 않은 과목 목록
    vector<int> subjects;
    subjects.reserve(N);
    for(int i = 0; i < N; i++)
    {
        subjects.push_back(i);
    }

    // 수강하지 않은 과목이 남아있는 경우 학기 진행
    while(subjects.size() > 0)
    {
        // 이번 학기에 들을 과목 목록
        vector<int> finished_subjects;

        // 선수과목 조건 확인
        for(auto subject : subjects)
        {
            // 선수과목이 존재하지 않는 경우
            if(table.find(subject) == table.end())
            {
                finished_subjects.push_back(subject);
            }

            // 학기 기록
            answer[subject]++;
        }

        // 이번 학기에 들을 과목 반영
        for(auto finished_subject : finished_subjects)
        {
            // 수강하지 않은 과목 목록 갱신
            subjects.erase(remove(subjects.begin(), subjects.end(), finished_subject), subjects.end());

            // 선수과목 조건 갱신
            for(auto it = table.begin(); it != table.end();)
            {
                it->second.erase(remove(it->second.begin(), it->second.end(), finished_subject), it->second.end());
                if(it->second.size() == 0)
                {
                    table.erase(it++);
                }
                else
                {
                    ++it;
                }
            }
        }
    }

    // 정답 출력
    for(auto e : answer)
    {
        cout << e << " ";
    }

    return 0;
}