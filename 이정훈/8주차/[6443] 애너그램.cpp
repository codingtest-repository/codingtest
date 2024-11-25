/*
* Author    : Lee JeongHun
* Date      : 2024.11.21(Thu)
* Runtime   : 28 ms
* Memory    : 2024 KB
* Algorithm : Backtracking
*/

#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

int main()
{
    // 입력 처리
    int n;
    cin >> n;

    for(int i = 0; i < n; ++i)
    {
        string word;
        cin >> word;

        // 애너그램 출력
        sort(word.begin(), word.end());

        do
        {
            cout << word << '\n';
        } while (next_permutation(word.begin(), word.end()));
        
    }

    return 0;
}