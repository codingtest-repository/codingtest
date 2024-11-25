/*
* Author    : Lee JeongHun
* Date      : 2024.11.21(Thu)
* Runtime   : 0 ms
* Memory    : 2020 KB
* Algorithm : Backtracking
*/

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    // 입력 처리
    int n;
    cin >> n;

    vector<int> arr(n);
    for(int i = 0; i < n; ++i)
    {
        cin >> arr[i];
    }

    vector<int> op;
    op.reserve(n - 1);
    for(int i = 0; i < 4; ++i)
    {
        int count;
        cin >> count;

        for(int j = 0; j < count; ++j)
        {
            op.push_back(i);
        }
    }

    int min, max;
    bool init = true;

    do
    {
        int sum = arr[0];
        
        for(int i = 0; i < op.size(); ++i)
        {
            switch(op[i])
            {
                case 0: // +
                sum += arr[i + 1];
                break;

                case 1: // -
                sum -= arr[i + 1];
                break;

                case 2: // *
                sum *= arr[i + 1];
                break;

                case 3: // /
                sum /= arr[i + 1];
                break;
            }
        }

        if(init)
        {
            max = sum;
            min = sum;
            init = false;
        }
        else if(sum < min)
        {
            min = sum;
        }
        else if(sum > max)
        {
            max = sum;
        }

    } while (next_permutation(op.begin(), op.end()));
    
    // 정답 출력
    cout << max << '\n';
    cout << min << '\n';

    return 0;
}