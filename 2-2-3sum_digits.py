'''
파라미터로 정수값 n을 받고 n의 각 자릿수의 합을 리턴해주는 재귀함수 sum_digits를 쓰세요. 
반복문을 쓰지 말고, 재귀(recursion)의 개념을 활용해주세요!
출력 결과
14
15
16
11
20
'''

# n의 각 자릿수의 합을 리턴
def sum_digits(n):
    length = len(str(n))-1
    
    if n<10: return n
    else: return sum_digits(n-(n//(10**length))*(10**length))+(n//(10**length))


# 해답
def sum_digits(n):
    # base case
    if n < 10:
        return n

    # recursive case
    return n % 10 + sum_digits(n // 10)


# 테스트
print(sum_digits(22541))
print(sum_digits(92130))
print(sum_digits(12634))
print(sum_digits(704))
print(sum_digits(3755))
