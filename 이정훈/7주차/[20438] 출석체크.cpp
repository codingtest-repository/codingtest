/*
* Author    : Lee JeongHun
* Date      : 2024.11.15(Fri)
* Runtime   : 8 ms
* Memory    : 2160 KB
* Algorithm : Prefix Sum
*/

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

void send(const vector<int>& sleepings, vector<bool>& visited, int index);

int main()
{
    ios::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);
    
    // 입력 처리
    int n, k, q, m;
    cin >> n >> k >> q >> m;

    // 졸고 있는 학생의 입장 번호
    vector<int> sleepings(k);
    for(int i = 0; i < k; ++i)
    {
        cin >> sleepings[i];
    }

    // 지환이가 출석 코드를 보낼 입장 번호
    vector<bool> visited(n + 3);
    for(int i = 0; i < q; ++i)
    {
        int input;
        cin >> input;
        send(sleepings, visited, input);
    }

    // 누적합
    vector<int> sum(n + 3);
    for(int i = 3; i < n + 3; ++i)
    {
        sum[i] = visited[i] == false ? sum[i - 1] + 1 : sum[i - 1];
    }

    // 정답 출력
    for(int i = 0; i < m; ++i)
    {
        int s, e;
        cin >> s >> e;

        cout << sum[e] - sum[s - 1] << '\n';
    }

    return 0;
}

void send(const vector<int>& sleepings, vector<bool>& visited, int index)
{
    // 이미 방문했거나 졸고 있는 학생의 경우에는 코드 전송을 중단
    if(visited[index] == true || find(sleepings.begin(), sleepings.end(), index) != sleepings.end())
    {
        return;
    }

    // 출석 체크
    visited[index] = true;

    // 다른 학생에게 코드 전송
    int n = visited.size();
    for(int i = index * 2; i < n + 3; i += index)
    {
        send(sleepings, visited, i);
    }
}