"""
* Author    : SHIM SOMIN
* Date      : 2024.10.04 (Fri)
* Runtime   : 680 ms 
* Memory    : 42300 KB  
* Algorithm : 스택
 """

input_str = input()
bomb_str = input()
bomb_len = len(bomb_str)
stack = []

for char in input_str:
    stack.append(char)
    
    # 스택의 마지막 부분이 폭발 문자열과 일치하면 제거
    if len(stack) >= bomb_len and ''.join(stack[-bomb_len:]) == bomb_str:
        del stack[-bomb_len:]

# 스택에 남은 문자들을 하나로 합침
result = ''.join(stack)

if len(result) == 0:
    print('FRULA')
else:
    print(result)
