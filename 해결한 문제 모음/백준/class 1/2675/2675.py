import sys
sys.stdin = open('input_2675.txt')

T = int(input())

for tc in range(1, T + 1):
    num, word = input().split()
    num = int(num)
    word = list(word)
    new_word = []
    ans = []

    for i in range(len(word)):
        new_word.append(word[i] * num)

    for i in range(1, len(new_word)):
        new_word[0] += new_word[i]
    
    print(new_word[0])