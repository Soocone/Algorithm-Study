'''
실습과제
‘이진 탐색(Binary Search)’ 알고리즘을 사용해서 어떤 원소가 리스트 안에 
포함되어 있는지 확인하려고 합니다. 이진 탐색 알고리즘은 선형 탐색 알고리즘과 달리, 
정렬된 리스트를 전제로 합니다. 정렬된 리스트가 아니면 이 알고리즘은 적용이 불가능합니다.

왜 이 알고리즘의 이름이 ‘이진 탐색’일까요? 1회 비교를 거칠 때마다 탐색 범위가 (대략) 절반으로 줄어들기 때문입니다.

예시
예를 들어 [1, 2, 3, 5, 8, 13, 21, 34, 55]에서 3을 찾는 경우, 알고리즘의 진행 방식은 다음과 같습니다:

시도 1
리스트의 첫 번째 인덱스와 마지막 인덱스의 값을 합하여 2로 나눈 후, 중간 인덱스로 지정합니다. 
그리고 그 인덱스에 해당하는 값이 3인지 확인해봅니다.

이 경우 리스트의 첫 번째 인덱스는 0이고 마지막 인덱스는 8이기 때문에, 중간 인덱스는 4이고 해당 원소는 8입니다.
찾고자 하는 원소(3)는 중간 원소(8)에 비해 작습니다. 리스트는 정렬되어 있으니, 
이제 인덱스 4~8은 탐색 범위에서 제외시킬 수 있습니다. 탐색 범위가 절반으로 줄어든 것이죠.
'''

#내 답안(힌트 참조했음 ㅠㅠ 너무 어렵)
def binary_search(element, some_list):
    fidx = 0
    eidx = len(some_list)-1
    
    while fidx<=eidx:
        midx = (fidx + eidx)//2
        if some_list[midx] == element:
            return midx
        elif some_list[midx] > element:
            eidx = midx - 1
            continue
        else:
            fidx = midx + 1
            continue


#해답
'''
def binary_search(element, some_list):
    start_index = 0
    end_index = len(some_list) - 1
    
    while start_index <= end_index:
        midpoint = (start_index + end_index) // 2
        if some_list[midpoint] == element:
            return midpoint
        elif some_list[midpoint] > element:
            end_index = midpoint - 1
        else:
            start_index = midpoint + 1
    return None
'''
print(binary_search(2, [2, 3, 5, 7, 11]))
print(binary_search(0, [2, 3, 5, 7, 11]))
print(binary_search(5, [2, 3, 5, 7, 11]))
print(binary_search(3, [2, 3, 5, 7, 11]))
print(binary_search(11, [2, 3, 5, 7, 11]))