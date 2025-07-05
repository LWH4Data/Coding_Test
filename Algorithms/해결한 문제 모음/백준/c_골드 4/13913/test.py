from collections import deque
test = [1, 2, 3]

# append() 메서드는 return을 하지 않는다.
X = test.append(4)

# 객체의 상태를 변화 시키기에 객체를 그대로 출력하면 결과가 나온다.
print(test)

# 그러나 값을 초기화 하면 None을 반환한다.
print(X)