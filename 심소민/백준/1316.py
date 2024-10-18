'''
* Author    : SHIM SOMIN
* Date      : 2024.10.17 (Fri)
* Runtime   : 40 ms
* Memory    : 31120 KB
* Algorithm : 탐색 
'''
n = int(input())
cnt = 0

for _ in range(n):
    word = input().strip()
    seen = set()
    prev_char = ''
    is_group_word = True

    for char in word:
        if char != prev_char:
            if char in seen:
                is_group_word = False
                break
            seen.add(char)
        prev_char = char

    if is_group_word:
        cnt += 1

print(cnt)