/*
* Author    : Lee JeongHun
* Date      : 2024.11.15(Fri)
* Runtime   : 4 ms
* Memory    : 2020 KB
* Algorithm : Brute Force
*/

#include <iostream>
#include <vector>
#include <stack>

using namespace std;

void permutate(const vector<int>& arr, vector<int>& output, vector<bool>& visited, int depth, int n, int r, int k, int& count);

int main()
{
    // 입력 처리
    int n, k;
    cin >> n >> k;

    vector<int> kits(n);
    for(int i = 0; i < n; ++i)
    {
        cin >> kits[i];
    }

    vector<bool> visited(n);
    vector<int> output(n);
    int count = 0;
    permutate(kits, output, visited, 0, n, n, k, count);

    cout << count << endl;

    return 0;
}

void permutate(const vector<int>& arr, vector<int>& output, vector<bool>& visited, int depth, int n, int r, int k, int& count)
{
    if(depth == r)
    {
        // output 처리
        int weight = 500 + output[0];

        for(int i = 1; i < n; ++i)
        {
            weight -= k;
            if(weight < 500)
            {
                return;
            }
            weight += output[i];
        }

        ++count;
    }

    for(int i = 0; i < n; ++i)
    {
        if(visited[i] == false)
        {
            visited[i] = true;
            output[depth] = arr[i];
            permutate(arr, output, visited, depth + 1, n, r, k, count);
            visited[i] = false;
        }
    }
}