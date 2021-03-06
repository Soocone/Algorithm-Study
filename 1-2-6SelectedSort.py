'''
선택정렬

1. 알고리즘의 정석
   2)하나의 문제 여러가지 알고리즘
        (6) 선택정렬 : 현재 위치에 들어갈 데이터를 찾아 선택하는 알고리즘
            => 첫번째 데이터와 나머지 데이터를 하나씩 비교하여 가장 작은 값을 찾아 자리를 바꾸고
            또 두번째 데이터와 나머지 데이터를 비교하여 가장 작은 값과 자리를 바꾸는 것을 반복하여 순서대로 정렬한다.

'''

def selected(lists):
    
    for i in range(0, 6):
        for j in range(0, 6-i):
            if lists[j] > lists[j+1]:
                temp = lists[j]
                lists[j] = lists[j+1]
                lists[j+1] = temp
            else: j+1
        i+1
    return lists

print(selected([4,6,2,8,1,9,3]))
