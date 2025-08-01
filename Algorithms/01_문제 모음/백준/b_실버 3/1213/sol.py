import sys, time
sys.stdin = open('input.txt')
start_time = time.time()

#======================================================
T = int(input())

for tc in range(1, T + 1):
    from collections import Counter
    '''
    < Counter >
    - iterable한 자료 구조의 각 원소가 몇 번 등장했는지 세어주는 dict 형태의 클래스이다.
    - 예
        ex =  "AABBCCCD"
        c = Counter(s)
        print(c)
        -> Counter({'C' : 3, 'A' : 2, 'B' : 2, 'D' : 1})
    - 없는 문자를 찾는 경우에도 keyError가 발생하지 않도록 0을 반환한다.
    '''

    word = input().strip()

    # word의 각 원소의 수를 초기화
    counter = Counter(word)

    # 홀수 개인 글자를 위한 설정
    odd_cnt = 0
    odd_char = ''
    half = []

    # 회문인지 확인
    # 사전순으로 정렬하기에 sorted()를 적용한 뒤 확인
    for char in sorted(counter):

        # 해당 원소의 글자의 수를 count로 초기화
        count = counter[char]

        # 만약 홀수라면 홀수 글자수 +1
        if count % 2 == 1:
            odd_cnt += 1

            # 만약 홀수인 글자 수가 2개 이상이면 회문이 안돼기에 
            # "I'm Sorry Hansoo"를 출력 후 종료
            if odd_cnt > 1:
                print("I'm Sorry Hansoo")
                break

            # 아니라면 홀수인 글자를 저장하고 넘어감.
            odd_char = char
        
        # 각 글자들을 리스트로 추가. 
        # 몫만큼 추가하면 좌우 대칭으로 구성할 수 있다.
        half.extend([char] * (count // 2))
    
    # 회문 좌측 초기화
    left = ''.join(half)

    # 홀수인 글자가 있다면 중앙에 위치시킨다.
    if odd_cnt == 1:
        center = odd_char
    else:
        center = ''
    
    # 회문 우측은 역순 정렬해야 대칭이 된다.
    right = left[ : : -1]

    # 각 영역을 합친 뒤 출력
    print(left + center + right)
#======================================================

end_time = time.time()
print('time: ', end_time - start_time)