/*
* Author    : Lee JeongHun
* Date      : 2024.11.21(Thu)
* Runtime   : 64 ms
* Memory    : 2020 KB
* Algorithm : Backtracking
*/

#include <iostream>
#include <vector>

using namespace std;

int count = 0;

void combination(const vector<int>& arr, vector<bool>& visited, int index, int depth, const int& s)
{
    if(depth > 0)
    {
        int sum = 0;
        int size = 0;
        for(int i = 0; i < arr.size(); ++i)
        {
            if(visited[i])
            {
                sum += arr[i];
                ++size;

                if(size == depth)
                {
                    break;
                }
            }
        }

        if(sum == s)
        {
            ++count;
        }
    }

    for(int i = index; i < arr.size(); ++i)
    {
        if(visited[i]) continue;

        visited[i] = true;
        combination(arr, visited, i, depth + 1, s);
        visited[i] = false;
    }
}

int main()
{
    // 입력 처리
    int n, s;
    cin >> n >> s;

    vector<int> arr(n);
    for(int i = 0; i < n; ++i)
    {
        cin >> arr[i];
    }

    vector<bool> visited(n);
    combination(arr, visited, 0, 0, s);
    
    // 정답 출력
    cout << count << '\n';

    return 0;
}