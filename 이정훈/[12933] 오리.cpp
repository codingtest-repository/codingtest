#include <iostream>
#include <vector>
#include <stack>

using namespace std;

int main()
{
    // 변수 선언 및 초기화
    string input;
    cin >> input;

    string sound = "quack";

    vector<stack<char>> ducks;

    // 입력 분석
    for(auto c : input)
    {
        /* q는 항상 새로운 울음소리의 시작이므로 k를 외친 오리가 있으면 해당 오리의 울음소리이며, 해당하는 오리가 없는 경우에는 새로운 오리의 울음소리이다. */
        if(c == 'q')
        {
            bool should_new_duck = true;

            // 기존 오리 분석
            for(auto& duck : ducks)
            {
                if(duck.top() == 'k')
                {
                    should_new_duck = false;
                    duck.push(c);
                    break;
                }
            }

            // 새로운 오리 추가
            if(should_new_duck)
            {
                stack<char> new_duck;
                new_duck.push(c);
                ducks.push_back(new_duck);
            }
        }
        else
        {
            /* q 이외의 소리는 반드시 기존 오리들의 울음소리여야 한다. 그렇지 않다면 녹음한 소리가 올바르지 않은 경우이므로 -1을 출력한다. */
            // 앞 글자 확인
            char target;
            
            // 울음 소리가 잘못된 경우
            if(sound.find(c) == string::npos)
            {
                cout << -1;
                return 0;
            }
            else
            {
                target = sound[sound.find(c) - 1];
            }

            // 기존 오리 존재 유무
            bool should_new_duck = true;

            // 기존 오리 분석
            for(auto& duck : ducks)
            {
                if(duck.top() == target)
                {
                    should_new_duck = false;
                    duck.push(c);
                    break;
                }
            }

            // 기존 오리가 존재하지 않는 경우 울음 소리가 잘못 되었습니다.
            if(should_new_duck)
            {
                cout << -1;
                return 0;
            }
        }
    }

    // 모든 울음소리는 k로 끝나야합니다.
    for(auto duck : ducks)
    {
        if(duck.top() != 'k')
        {
            cout << -1;
            return 0;
        }
    }

    // 결과 출력
    cout << ducks.size();

    return 0;
}