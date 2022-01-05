'''
2. 재귀함수
   2)재귀함수 연습
        (2) 숫자합 : n번째 삼각수(triangle number)는 자연수 1부터 n까지의 합입니다. 
        파라미터로 정수값 n을 받고 n번째 삼각수를 리턴해주는 재귀 함수 triangle_number를 쓰세요. 

n번째 삼각수(triangle number)는 자연수 1부터 n까지의 합입니다. 파라미터로 정수값 n을 받고 n번째 
삼각수를 리턴해주는 재귀 함수 triangle_number를 쓰세요. n은 1이상의 자연수라고 가정합시다.
함수 안에 반복문은 쓰면 안됩니다!

# 1부터 n까지의 합을 리턴
n번째 삼각수(triangle number)는 자연수 1부터 n까지의 합입니다. 파라미터로 정수값 n을 받고 n번째 삼각수를 리턴해주는 재귀 함수 
[답안]
1
3
6
10
15
21
28
36
45
55
'''
# 1부터 n까지의 합을 리턴
# 내 답안
def triangle_number(n):
    if n ==1: return 1
    else: return triangle_number(n-1)+ n

# 윤아 언니 답안
def triangle_number(n):
    if n ==1 : 
        return 1
    else:
        return triangle_number(n-1)+n

# 어떤 사람 답
def sum_generator(N):
    return sum(n for n in range(1, N+1))


# 테스트: triangle_number(1)부터 triangle_number(10)까지 출력
for i in range(1, 11):
    print(triangle_number(i))